import json
import threading
import subprocess

from tkinter import filedialog as fd


# Thread class with a command line in argument
class Thread(threading.Thread):
    def __init__(self, cmd):
        super().__init__()
        self.cmd = cmd
        self.daemon = True

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
