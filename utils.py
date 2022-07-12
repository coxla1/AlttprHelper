import json
import requests
import logging as lg
import random as rd

import os
import shutil
import clipboard
import psutil
import threading
import subprocess

import webbrowser
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from grpc._channel import _InactiveRpcError

import fxpak


msupacks = ['Default']


# Thread class with a command line in argument
class Thread(threading.Thread):
    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd
        self.daemon = True
        self.exc = None

    def run(self):
        subprocess.call(self.cmd)


# Config file load and save function
def config(variables, mode):
    if mode == 0:  # Load
        try:
            with open('config.json', 'r') as cfgfile:
                cfg = json.load(cfgfile)
        except FileNotFoundError:
            cfg = {}
    else:  # Save
        cfg = {}

    if not cfg:
        for var in variables:
            if var != 'seed' and var != 'uri':
                if isinstance(variables[var], dict):
                    cfg[var] = {}
                    for y in variables[var]:
                        cfg[var][y] = variables[var][y].get()

                else:
                    cfg[var] = variables[var].get()

    if mode == 0:  # Load
        for var in cfg:
            try:
                if isinstance(cfg[var], dict):
                    for y in cfg[var]:
                        variables[var][y].set(cfg[var][y])

                else:
                    variables[var].set(cfg[var])
            except KeyError:
                pass
    else:  # Save
        with open('config.json', 'w') as cfgfile:
            json.dump(cfg, cfgfile, indent=4)


# Default texts functions
def set_default_text(entry, text):
    def on_entry_click(e):
        if e.cget('fg') == 'grey':
            e.delete(0, 'end')
            e.insert(0, '')
            e.config(fg='black')

    def on_focusout(e, default):
        if e.get() == '':
            e.insert(0, default)
            e.config(fg='grey')

    entry.bind('<FocusIn>', lambda event: on_entry_click(entry))
    entry.bind('<FocusOut>', lambda event: on_focusout(entry, text))
    if entry.get() == '':
        entry.insert(0, text)
    if entry.get() == text:
        entry.config(fg='grey')


# File dialogs and setting entry path function
def set_path(var, entry, mode):
    entry.focus()
    if mode == 0:  # File
        path = fd.askopenfilename()
    else:  # Folder
        path = fd.askdirectory()
    var.set(path)


# Switch active frame function
def switch_frame(enable_children, disable_children):
    for child in enable_children:
        child.configure(state='normal')
    for child in disable_children:
        child.configure(state='disabled')


# Refresh list of MSU function
def refresh(variables, msu_list, log):
    global msupacks
    msupacks = []

    if variables['mode'].get() == 0:  # USB transfer
        try:
            msupacks = fxpak.dir_content(variables['uri'].get(), variables['fxpak-path'].get(), 0)
        except _InactiveRpcError as e:
            lg.error(f'Could not find the MSU directory: {e}')
            log.config(text='Could not find the MSU directory, reboot SNES, then detect and refresh again')
            return -1

    else:  # Copy file
        try:
            path = variables['folder-path'].get()
            msupacks = [msu for msu in os.listdir(path) if os.path.isdir(os.path.join(path, msu))]
        except FileNotFoundError as e:
            lg.error(f'Could not find the MSU directory: {e}')
            log.config(text='Could not find the MSU directory, check your path')
            return -1

    msupacks.sort()

    msu_list.children['menu'].delete(0, 'end')
    for msu in ['Default', 'Random']:
        msu_list.children['menu'].add_command(label=msu, command=lambda y=msu: variables['msu'].set(y))

    for msu in msupacks:
        msu_list.children['menu'].add_command(label=msu, command=lambda y=msu: variables['msu'].set(y))

    lg.info(f'Found {len(msupacks)} MSU packs')
    log.config(text=f'Found {len(msupacks)} MSU packs')

    msupacks.append('Default')


# Main function
def run(variables, defaults, log):
    global msupacks

    # The path will always be formatted to not have a / at the end of the str

    # Return if a text is a default one or not
    def check_default_text(text, default_text):
        return text == default_text

    # Returns the hash of a seed file or URL
    def seed_hash(seed):
        if '.sfc' in seed:  # Input: file
            with open(seed, 'rb') as f:
                f.read(32704)
                h = bytearray.fromhex(f.read(13).hex()).decode()
            h = str(h[3:]) if h[:2] == 'VT' else None
        else:  # Input: URL or seedhash
            if '/' in seed:
                seed = seed[::-1]
                h = seed[:seed.find('/')][::-1]
            else:
                h = seed

        if h:
            url = f'https://alttpr-patch-data.s3.us-east-2.amazonaws.com/{h}.json'
            with requests.get(url) as r:
                build = r.json()['spoiler']['meta']['build']
            h = None if build[:4] < '2021' else h

        return h

    # Return the filename format of an MSU, without extension
    def get_filename(path, mode, uri):
        if mode == 0:  # USB transfer
            content = fxpak.dir_content(uri, path, 1)
        else:  # Copy file
            content = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]

        flag, i = False, 0
        while not flag and i < len(content):
            file = content[i]
            flag = file[-4:] == '.pcm'
            i += 1

        if not flag:
            raise FileNotFoundError

        i = file[::-1].index('-')
        return file[::-1][i + 1:][::-1]

    # Create a .msu file
    def create_dotmsu(path, filename, mode, uri):
        open(f'{filename}.msu', 'w').close()
        if mode == 0:  # USB transfer
            fxpak.send_file(uri,
                            f'{path}/{filename}.msu',
                            open(f'{filename}.msu', 'rb').read()
                            )
        else:  # Copy file
            shutil.copy(f'{filename}.msu', f'{path}/{filename}.msu')

        os.remove(f'{filename}.msu')

    # Create a manifest.bml file
    def create_manifest(name, path):
        f = open(f'{path}/manifest.bml', 'w')

        f.write('cartridge region=NTSC\n')
        f.write(f'  rom name={name}.sfc size=0x200000\n')
        f.write(f'  ram name={name}.srm size=0x8000\n')
        f.write('  map id=rom address=00-3f,80-bf:8000-ffff mask=0x8000\n')
        f.write('  map id=rom address=40-6f,c0-ef:0000-7fff mask=0x8000\n')
        f.write('  map id=ram address=70-7d,f0-ff:0000-ffff\n\n')

        f.write('  msu1\n')
        f.write(f'    rom name={name}.name size=0x0000\n')
        f.write(f'    map id=io address=00-3f,80-bf:2000-2007\n')

        for x in range(1, 62):
            f.write(f'    track number={x} name={name}-{x}.pcm\n')

        f.write('\ninformation\n')
        f.write('  title: A Link to the Past Randomizer v31\n')
        f.write('  configuration\n')
        f.write(f'    rom name={name}.sfc size=0x200000\n')
        f.write(f'    ram name={name}.srm size=0x2000')

        f.close()

    # Check if an executable is already running
    def check_process(path, kill):
        name = path[::-1]
        try:
            i = name.index('/')
            name = name[:i][::-1]
        except Exception as e:
            name = ''
            lg.warning(f'No process found: {e}')

        for x in psutil.process_iter():
            if name == x.name():
                if kill:
                    x.kill()
                return True
        return False

    log.config(text='')
    h = None

    if variables['seed'].get():
        # Hash
        h = seed_hash(variables['seed'].get())
        lg.info(f'Seed hash: {h}')

        # MSU Pack
        msu = variables['msu'].get()
        if msu == 'Random':
            msu = msupacks[rd.randint(0, len(msupacks) - 1)]
            variables['msu'].set(msu)

        if variables['mode'].get() == 0:  # USB transfer
            destination_folder = variables['fxpak-path'].get()
        else:  # Copy file
            destination_folder = variables['folder-path'].get()
        destination_folder = destination_folder[:-1] if destination_folder[-1] == '/' else destination_folder

        if msu != 'Default':
            destination_folder = f'{destination_folder}/{msu}'
            try:
                filename = get_filename(destination_folder, variables['mode'].get(), variables['uri'].get())
            except FileNotFoundError:
                lg.error('No track found in this MSU')
                log.config(text='Could not find a track in this MSU')
                return -1

            create_dotmsu(destination_folder,
                          filename,
                          variables['mode'].get(),
                          variables['uri'].get()
                          )
            if (not check_default_text(variables['emulator'].get(), defaults['emulator'])
                    and 'retroarch' in variables['emulator'].get()):
                create_manifest(filename, destination_folder)
        else:
            filename = 'seed'

        lg.info(f'MSU: {msu}')
        lg.info('Transfer type: {:}'.format('Copy' if variables['mode'].get() else 'USB'))
        lg.info(f'Destination folder: {destination_folder}')
        lg.info(f'Filename: {filename}')

        if variables['mode'].get() == 0:  # USB transfer
            try:
                fxpak.send_file(variables['uri'].get(),
                                f'{destination_folder}/{filename}.sfc',
                                open(variables['seed'].get(), 'rb').read()
                                )
            except Exception as e:
                lg.error(f'Oops upload to FXPak did not went really well: {e}')
                log.config(text='Could not send the seed to FXPak')

        else:  # Copy file
            shutil.copy(variables['seed'].get(),
                        f'{destination_folder}/{filename}.sfc'
                        )

        # Boot ROM
        if variables['autostart']['boot'].get():
            if variables['mode'].get() == 0:  # USB transfer
                fxpak.boot_rom(variables['uri'].get(), f'{destination_folder}/{filename}.sfc')

            elif (variables['mode'].get() == 1
                  and not check_default_text(variables['emulator'].get(), defaults['emulator'])):  # Copy file
                if ('retroarch' in variables['emulator'].get().lower()  # RetroArch with a core
                        and not check_default_text(variables['retroarch-core'].get(), defaults['retroarch-core'])):
                    if msu == 'Default':
                        t_emulator = Thread(
                            '"{:}" -L "{:}" "{:}"'.format(
                                variables['emulator'].get(),
                                variables['retroarch-core'].get(),
                                f'{destination_folder}/{filename}.sfc'))
                    else:
                        t_emulator = Thread(
                            '"{:}" -L "{:}" "{:}"'.format(
                                variables['emulator'].get(),
                                variables['retroarch-core'].get(),
                                f'{destination_folder}/manifest.bml'))

                else:  # Not RetroArch or RetroArch without a core specified
                    t_emulator = Thread(f'"{variables["emulator"].get()}" "{destination_folder}/{filename}.sfc"')

                t_emulator.start()

    # Autostart timer
    if (variables['autostart']['timer'].get()
            and not check_default_text(variables['timer'].get(), defaults['timer'])
            and not check_process(variables['timer'].get(), 0)):
        t_timer = Thread(variables['timer'].get())
        t_timer.start()

    # Autostart USB interface
    if (variables['autostart']['usb-interface'].get()
            and not check_default_text(variables['usb-interface'].get(), defaults['usb-interface'])
            and not check_process(variables['usb-interface'].get(), 0)):
        t_usbinterface = Thread(variables['usb-interface'].get())
        t_usbinterface.start()

    # Autostart Input viewer
    if (variables['autostart']['input-viewer'].get()
            and not check_default_text(variables['input-viewer'].get(), defaults['input-viewer'])
            and not check_process(variables['input-viewer'].get(), 0)):
        t_inputviewer = Thread(variables['input-viewer'].get())
        t_inputviewer.start()

    # Autostart tracker
    if (variables['autostart']['tracker'].get()
            and not check_default_text(variables['tracker'].get(), defaults['tracker'])):
        if '://' in variables['tracker'].get():
            webbrowser.open(variables['tracker'].get())
        else:
            t_tracker = Thread(variables['tracker'].get())
            t_tracker.start()

    # Autostart entrance tracker
    if (variables['autostart']['entrance-tracker'].get()
            and not check_default_text(variables['entrance-tracker'].get(), defaults['entrance-tracker'])):
        if '.htm' or '://' in variables['entrance-tracker'].get():
            prefix = 'file:///' if '.htm' in variables['entrance-tracker'].get() else ''
            webbrowser.open(f'{prefix}{variables["entrance-tracker"].get()}')
        else:
            t_entrancetracker = Thread(variables['entrance-tracker'].get())
            t_entrancetracker.start()

    # Autostart door tracker
    if (variables['autostart']['door-tracker'].get()
            and not check_default_text(variables['door-tracker'].get(), defaults['door-tracker'])):
        if '.htm' or '://' in variables['door-tracker'].get():
            prefix = 'file:///' if '.htm' in variables['door-tracker'].get() else ''
            webbrowser.open(f'{prefix}{variables["door-tracker"].get()}')
        else:
            t_doortracker = Thread(variables['door-tracker'].get())
            t_doortracker.start()

    if h and variables['seed'].get():
        clipboard.copy(h)
        log.config(text='Seed hash copied to clipboard')
        if variables['mode'].get() == 0 and variables['autostart']['boot'].get():
            warn = 'If your autotracker doesn\'t detect your console, disconnect your SNES from SNI dropdown menu\n'
            warn += 'If that still not works, restart both your console and SNI and/or disable boot ROM.'
            mb.showwarning('Boot ROM', warn)
    else:
        log.config(text=f'No hash found (likely if the game was not generated on alttpr.com)')

    # Keydrop information
    if variables['autostart']['keydrop'].get():
        keycount = 'Number of keys in each dungeons\n'
        keycount += '(Does not apply if crossed door turned on)\n'
        keycount += 'Dungeon | Drops | Chests | # of checks w/ keydropsanity\n'
        keycount += '-------------------------------------------------------------------------\n'
        keycount += '      HC      |     3     |      1      |                      12\n'
        keycount += '      CT       |     2     |      2      |                       4\n'
        keycount += '      EP       |     2     |      0      |                       8\n'
        keycount += '      DP      |     3     |      1      |                       9\n'
        keycount += '     ToH     |     0     |      1      |                       6\n'
        keycount += '     PoD     |     0     |      6      |                      14\n'
        keycount += '      SP       |     5     |      1      |                      15\n'
        keycount += '     SW      |     2     |      3      |                      10\n'
        keycount += '      TT       |     2     |      1      |                      10\n'
        keycount += '      IP        |     4     |      2      |                      12\n'
        keycount += '    MM      |     3     |      3      |                       11\n'
        keycount += '      TR      |     2     |      4      |                       14\n'
        keycount += '      GT      |     4     |      4      |                       31\n'
        mb.showinfo('Keydrop keys count', keycount)
