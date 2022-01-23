import json
import threading
import subprocess
import os
import shutil
import logging as lg
import requests
import random as rd
import urllib.request
from tkinter import filedialog as fd

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
        try:
            subprocess.call(self.cmd)
        except Exception as e:
            self.exc = e

    def join(self, **kwargs):
        threading.Thread.join(self)
        if self.exc:
            raise self.exc
        return -1


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
            if isinstance(cfg[var], dict):
                for y in cfg[var]:
                    variables[var][y].set(cfg[var][y])

            else:
                variables[var].set(cfg[var])
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
        except Exception as e:
            lg.error(f'Could not find the MSU directory : {e}')
            log.config(text='Could not find the MSU directory')
            return -1

    else:  # Copy file
        try:
            path = variables['folder-path'].get()
            msupacks = [msu for msu in os.listdir(path) if os.path.isdir(os.path.join(path, msu))]
        except FileNotFoundError as e:
            lg.error(f'Could not find the MSU directory : {e}')
            log.config(text='Could not find the MSU directory')
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


# TODO : rewrite
def dunka_url(vars, log, settings={'spoilers': 'mystery'}):
    # Determine URL format
    with urllib.request.urlopen('https://raw.githubusercontent.com/bigdunka/alttptracker/master/js/index.js') as u:
        trackerjs = u.read().decode('utf-8')

    i = len('trackerWindow = window.open(')
    j = trackerjs.index('trackerWindow')
    k = trackerjs[j:].index('\n')
    urlformat = 'f' + trackerjs[j + i:j + k]

    # Define variables
    if settings['spoilers'] == 'mystery':
        tracker = 'tracker'
        type = 'O'
        entrance = 'N'
        boss = 'S'
        enemy = 'S'
        glitches = {'No Glitches': 'N', 'OWG': 'O', 'MG/No Logic': 'M'}[vars['dunkatracker']['maplogic'].get()]
        item = 'A'
        goal = 'G'
        tower = 'R'
        towercrystals = '7'
        ganon = 'R'
        ganoncrystals = '7'
        swords = 'R'
        map = {'None': 'N', 'Normal': 'M', 'Compact': 'C'}[vars['dunkatracker']['mapdisplay'].get()]
        spoiler = 'N'
        sphere = {0: 'N', 1: 'Y'}[vars['dunkatracker']['sphere'].get()]
        mystery = 'S'
        door = {'None': 'N', 'Basic': 'B', 'Crossed/Keydrop': 'C'}[vars['dunkatracker']['door'].get()]
        shuffledmaps = '1'
        shuffledcompasses = '1'
        shuffledsmallkeys = '1'
        shuffledbigkeys = '1'
        shopsanity = 'N'
        ambrosia = 'N'
        overworld = {'None': 'N', 'Mixed/Crossed/Misc': 'O', 'Parallel': 'P', 'Full': 'F'}[
            vars['dunkatracker']['overworld'].get()]
        autotracking = {0: 'N', 1: 'Y'}[vars['dunkatracker']['autotracker'].get()]
        trackingport = '8080'
        sprite = 'Link'
        compact = '&map=C' if map == 'C' else ''
        startingboots = 'N'
        startingflute = 'N'
        startinghookshot = 'N'
        startingicerod = 'N'

    else:
        tracker = 'entrancetracker' if 'shuffle' in settings else 'tracker'
        type = {'open': 'O', 'standard': 'S', 'inverted': 'I', 'retro': 'R'}[settings['mode']]
        entrance = 'S' if 'shuffle' in settings else 'N'
        boss = 'N' if settings['enemizer.boss_shuffle'] == 'none' else 'S'
        enemy = 'N' if settings['enemizer.enemy_shuffle'] == 'none' else 'S'
        glitches = {'No Glitches': 'N', 'OWG': 'O', 'MG/No Logic': 'M'}[vars['dunkatracker']['maplogic'].get()]
        item = 'A'
        goal = {'ganon': 'G', 'fast_ganon': 'F', 'pedestal': 'P', 'dungeons': 'A', 'triforce-hunt': 'O'}[
            settings['goal']]
        tower = 'R' if settings['entry_crystals_tower'] == 'random' else 'C'
        towercrystals = '7' if settings['entry_crystals_tower'] == 'random' else settings['entry_crystals_tower']
        ganon = 'R' if settings['entry_crystals_ganon'] == 'random' else 'C'
        ganoncrystals = '7' if settings['entry_crystals_tower'] == 'random' else settings['entry_crystals_ganon']
        swords = {'randomized': 'R', 'assured': 'A', 'vanilla': 'V', 'swordless': 'S'}[settings['weapons']]
        map = {'None': 'N', 'Normal': 'M', 'Compact': 'C'}[vars['dunkatracker']['mapdisplay'].get()]
        spoiler = 'N'
        sphere = {0: 'N', 1: 'Y'}[vars['dunkatracker']['sphere'].get()]
        mystery = 'S'
        door = {'None': 'N', 'Basic': 'B', 'Crossed/Keydrop': 'C'}[vars['dunkatracker']['door'].get()]

        shuffledmaps, shuffledcompasses, shuffledsmallkeys, shuffledbigkeys = \
        {'standard': ('0', '0', '0', '0'), 'mc': ('1', '1', '0', '0'), 'mcs': ('1', '1', '1', '0'),
         'full': ('1', '1', '1', '1')}[settings['dungeon_items']]
        shopsanity = {0: 'N', 1: 'Y'}[vars['dunkatracker']['shopsanity'].get()]

        if 'name' in settings:
            if 'Potpourri' in settings['name']:
                shuffledmaps, shuffledcompasses, shuffledsmallkeys, shuffledbigkeys = '0', '0', '1', '1'
            log.config(text='You may have to adjust settings using the flag icon in the top-left corner')

        if settings['logic'] == 'NoLogic':
            shuffledmaps, shuffledcompasses, shuffledsmallkeys, shuffledbigkeys = '1', '1', '1', '1'

        ambrosia = 'N'
        overworld = {'None': 'N', 'Mixed/Crossed/Misc': 'O', 'Parallel': 'P', 'Full': 'F'}[
            vars['dunkatracker']['overworld'].get()]
        autotracking = {0: 'N', 1: 'Y'}[vars['dunkatracker']['autotracker'].get()]
        trackingport = '8080'
        sprite = 'Link'
        compact = '&map=C' if map == 'C' else ''
        startingboots = 'N'
        startingflute = 'N'
        startinghookshot = 'N'
        startingicerod = 'N'

    # This should work if Dunka adds a new variable
    flag = True
    newvar = []
    while flag:
        try:
            url = 'https://alttprtracker.dunka.net/{:}'.format(eval(urlformat))
            flag = False
        except NameError as e:
            varname = str(e)[6:]
            i = varname.index('\'')
            newvar.append(varname[:i])
            exec('{:} = \'N\''.format(varname[:i]))

    for x in newvar:
        print(f'Dunka\'s tracker new variable: {x}')
    if newvar:
        log.config(text='New variable found for Dunka\'s tracker! Please advise Coxla#2119 on Discord')

    width = 1340 if map == 'M' else 448
    height = (988 if map == 'C' else 744) if sphere == 'Y' else (692 if map == 'C' else 448)

    return url, width + 15, height + 15 + 20


# Main function
def run(variables, defaults, log):
    global msupacks

    # The path will always be formatted to not have a / at the end of the str

    # Return if a text is a default one or not
    def check_default_text(text, default_text):
        return text == default_text

    # TODO : could be better, some edge cases may break it (e.g. kara fork)
    # Returns the hash of a seed file or URL
    def seed_hash(seed):
        if '.sfc' in seed:  # Input : file
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
        return h

    # Return the settings of a seed with hash h
    def seed_settings(h):
        if h:
            url = f'https://alttpr-patch-data.s3.us-east-2.amazonaws.com/{h}.json'
            with requests.get(url) as r:
                settings = r.json()['spoiler']
            if settings['meta']['build'][:4] < '2021':
                settings = None
        else:
            settings = None
        return settings

    # Return the filename format of an MSU, without extension
    def get_filename(path, mode, uri):
        if mode == 0:  # USB transfer
            content = fxpak.dir_content(uri, path, 1)
        else:  # Copy file
            content = [x for x in os.listdir(x) if os.path.isfile(os.path.join(path, x))]

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

    log.config(text='')

    if variables['seed'].get():
        # Hash
        h = seed_hash(variables['seed'].get())
        lg.info(f'Seed hash : {h}')

        # Settings
        try:
            settings = seed_settings(h)
        except Exception:
            settings = None
            lg.warning('Could not find settings for this seed')

        if settings:
            lg.info('Found settings')
            for x in settings['meta']:
                lg.info(f'{x} : {settings["meta"][x]}')

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

        lg.info(f'MSU : {msu}')
        lg.info('Transfer type : {:}'.format('Copy' if vars['mode'].get() else 'USB'))
        lg.info(f'Destination folder : {destination_folder}')
        lg.info(f'Filename : {filename}')

        if variables['mode'].get() == 0:  # USB transfer
            try:
                fxpak.send_file(variables['uri'].get(),
                                f'{destination_folder}/{filename}.sfc',
                                open(variables['seed'].get(), 'rb').read()
                                )
            except Exception as e:
                lg.error(f'Oops upload to FXPak did not went really well : {e}')
                log.config(text='Could not send the seed to FXPak')
        else:  # Copy file
            shutil.copy(variables['seed'].get(),
                        f'{destination_folder}/{filename}.sfc'
                        )
    # Autostart
