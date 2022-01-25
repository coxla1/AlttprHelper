import tkinter as tk
import logging as lg

import utils
import fxpak

# TODO : debug print picked options when this will be back
# TODO : sprites
# TODO : window too big now, use tabs

m, n = 0, 0

LBL_WIDTH = 14
ENTRY_WIDTH = 64
BTN_WIDTH = 14
SPIN_WIDTH = 5

frames = {}
labels = {}
inputs = {}
buttons = {}
variables = {}
defaults = {}

lg.basicConfig(
    filename='helper.log',
    encoding='utf-8',
    level=lg.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s')

window = tk.Tk()

# Window settings
window.title('ALTTPR Helper')
window.resizable(width=False, height=False)
window.iconbitmap('resources/icon.ico')

# Main frame
frames['main'] = tk.LabelFrame(
    window,
    text='Main',
    bd=2
)
frames['main'].grid(row=n, sticky=tk.W + tk.E)

# - Seed path / (URL)
labels['seed'] = tk.Label(
    frames['main'],
    text='Seed path',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['seed'].grid(row=m, column=0)

variables['seed'] = tk.StringVar()
inputs['seed'] = tk.Entry(
    frames['main'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['seed']
)
inputs['seed'].grid(row=m, column=1)

buttons['seed'] = tk.Button(
    frames['main'],
    text='...',
    width=BTN_WIDTH
)
buttons['seed'].grid(row=m, column=2)

m += 1

# - JP1.0 path
labels['rom'] = tk.Label(
    frames['main'],
    text='JP1.0 ROM path',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['rom'].grid(row=m, column=0)

variables['rom'] = tk.StringVar()
inputs['rom'] = tk.Entry(
    frames['main'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['rom']
)
inputs['rom'].grid(row=m, column=1)

buttons['rom'] = tk.Button(
    frames['main'],
    text='...',
    width=BTN_WIDTH
)
buttons['rom'].grid(row=m, column=2)

m += 1

# - FXPak / Copy file mode
labels['mode'] = tk.Label(
    frames['main'],
    text='Mode',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['mode'].grid(row=m, column=0)

frames['mode'] = tk.Frame(
    frames['main'],
    bd=2
)
frames['mode'].grid(row=m, column=1, sticky=tk.W)

variables['mode'] = tk.IntVar()
inputs['mode'] = [None, None]
inputs['mode'][0] = tk.Radiobutton(
    frames['mode'],
    text='USB transfer (FXPak / SD2SNES)',
    variable=variables['mode'],
    value=0
)
inputs['mode'][0].grid(row=0, column=0)

inputs['mode'][1] = tk.Radiobutton(
    frames['mode'],
    text='Copy file',
    variable=variables['mode'],
    value=1
)
inputs['mode'][1].grid(row=0, column=1)

m, n = 0, n + 1

# USB transfer frame
frames['transfer'] = tk.LabelFrame(
    window,
    text='USB transfer (FXPak / SD2SNES)',
    bd=2
)
frames['transfer'].grid(row=n, sticky=tk.W + tk.E)

# - FXPak path + detection
labels['fxpak-path'] = tk.Label(
    frames['transfer'],
    text='MSU folder',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['fxpak-path'].grid(row=m, column=0)

variables['fxpak-path'] = tk.StringVar()
defaults['fxpak-path'] = 'e.g. /alttp/msu, not case sensitive'
inputs['fxpak-path'] = tk.Entry(
    frames['transfer'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['fxpak-path']
)
inputs['fxpak-path'].grid(row=m, column=1)

variables['uri'] = tk.StringVar()
buttons['detect'] = tk.Button(
    frames['transfer'],
    text='Detect FXPak',
    width=LBL_WIDTH
)
buttons['detect'].grid(row=m, column=2)

m, n = 0, n + 1

# Copy file frame
frames['copy'] = tk.LabelFrame(
    window,
    text='Copy file',
    bd=2
)
frames['copy'].grid(row=n, sticky=tk.W + tk.E)

# - Emulator
labels['emulator'] = tk.Label(
    frames['copy'],
    text='Emulator',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['emulator'].grid(row=m, column=0)

variables['emulator'] = tk.StringVar()
defaults['emulator'] = 'Optional'
inputs['emulator'] = tk.Entry(
    frames['copy'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['emulator']
)
inputs['emulator'].grid(row=m, column=1)

buttons['emulator'] = tk.Button(
    frames['copy'],
    text='...',
    width=BTN_WIDTH
)
buttons['emulator'].grid(row=m, column=2)

m += 1

# - MSU
labels['folder-path'] = tk.Label(
    frames['copy'],
    text='MSU folder',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['folder-path'].grid(row=m, column=0)

variables['folder-path'] = tk.StringVar()
defaults['folder-path'] = 'Seed will be written there if default music is used'
inputs['folder-path'] = tk.Entry(
    frames['copy'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['folder-path']
)
inputs['folder-path'].grid(row=m, column=1)

buttons['folder-path'] = tk.Button(
    frames['copy'],
    text='...',
    width=BTN_WIDTH
)
buttons['folder-path'].grid(row=m, column=2)

m += 1

# - RetroArch core
labels['retroarch-core'] = tk.Label(
    frames['copy'],
    text='RetroArch Core',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['retroarch-core'].grid(row=m, column=0)

variables['retroarch-core'] = tk.StringVar()
defaults['retroarch-core'] = 'Required if using RetroArch, bsnes-mercury compatible with autotracking and MSUs'
inputs['retroarch-core'] = tk.Entry(
    frames['copy'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['retroarch-core']
)
inputs['retroarch-core'].grid(row=m, column=1)

buttons['retroarch-core'] = tk.Button(
    frames['copy'],
    text='...',
    width=BTN_WIDTH
)
buttons['retroarch-core'].grid(row=m, column=2)

m, n = 0, n + 1

# Misc frame
frames['misc'] = tk.LabelFrame(
    window,
    text='Miscellaneous',
    bd=2
)
frames['misc'].grid(row=n, sticky=tk.W + tk.E)

# - Timer
labels['timer'] = tk.Label(
    frames['misc'],
    text='Timer',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['timer'].grid(row=m, column=0)

variables['timer'] = tk.StringVar()
defaults['timer'] = 'Optional'
inputs['timer'] = tk.Entry(
    frames['misc'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['timer']
)
inputs['timer'].grid(row=m, column=1)

buttons['timer'] = tk.Button(
    frames['misc'],
    text='...',
    width=BTN_WIDTH
)
buttons['timer'].grid(row=m, column=2)

m += 1

# - SNI / QUSB2SNES
labels['usb-interface'] = tk.Label(
    frames['misc'],
    text='SNI / QUSB2SNES',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['usb-interface'].grid(row=m, column=0)

variables['usb-interface'] = tk.StringVar()
defaults['usb-interface'] = 'SNI required if USB transfer. Any interface required if using autotracker'
inputs['usb-interface'] = tk.Entry(
    frames['misc'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['usb-interface']
)
inputs['usb-interface'].grid(row=m, column=1)

buttons['usb-interface'] = tk.Button(
    frames['misc'],
    text='...',
    width=BTN_WIDTH,
)
buttons['usb-interface'].grid(row=m, column=2)

m += 1

# - Tracker
labels['tracker'] = tk.Label(
    frames['misc'],
    text='Tracker',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['tracker'].grid(row=m, column=0)

variables['tracker'] = tk.StringVar()
defaults['tracker'] = 'Optional. Supports URL'
inputs['tracker'] = tk.Entry(
    frames['misc'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['tracker']
)
inputs['tracker'].grid(row=m, column=1)

buttons['tracker'] = tk.Button(
    frames['misc'],
    text='...',
    width=BTN_WIDTH
)
buttons['tracker'].grid(row=m, column=2)

m += 1

# - Entrance tracker
labels['entrance-tracker'] = tk.Label(
    frames['misc'],
    text='Entrance tracker',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['entrance-tracker'].grid(row=m, column=0)

variables['entrance-tracker'] = tk.StringVar()
defaults['entrance-tracker'] = 'Optional. Supports URL'
inputs['entrance-tracker'] = tk.Entry(
    frames['misc'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['entrance-tracker']
)
inputs['entrance-tracker'].grid(row=m, column=1)

buttons['entrance-tracker'] = tk.Button(
    frames['misc'],
    text='...',
    width=BTN_WIDTH
)
buttons['entrance-tracker'].grid(row=m, column=2)

m += 1

# - Door tracker
labels['door-tracker'] = tk.Label(
    frames['misc'],
    text='Door tracker',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['door-tracker'].grid(row=m, column=0)

variables['door-tracker'] = tk.StringVar()
defaults['door-tracker'] = 'Optional. Supports URL'
inputs['door-tracker'] = tk.Entry(
    frames['misc'],
    width=ENTRY_WIDTH,
    exportselection=False,
    textvariable=variables['door-tracker']
)
inputs['door-tracker'].grid(row=m, column=1)

buttons['door-tracker'] = tk.Button(
    frames['misc'],
    text='...',
    width=BTN_WIDTH
)
buttons['door-tracker'].grid(row=m, column=2)

m, n = 0, n + 1

# Autostart frame
frames['autostart'] = tk.LabelFrame(
    window,
    text='Autostart options',
    bd=2
)
frames['autostart'].grid(row=n, sticky=tk.W + tk.E)

inputs['autostart'] = {}
variables['autostart'] = {}

# - Boot ROM
variables['autostart']['boot'] = tk.IntVar()
inputs['autostart']['boot'] = tk.Checkbutton(
    frames['autostart'],
    text='Boot ROM',
    variable=variables['autostart']['boot'],
    onvalue=1,
    offvalue=0
)
inputs['autostart']['boot'].grid(row=0, column=m)

m += 1

# - Timer
variables['autostart']['timer'] = tk.IntVar()
inputs['autostart']['timer'] = tk.Checkbutton(
    frames['autostart'],
    text='Timer',
    variable=variables['autostart']['timer'],
    onvalue=1,
    offvalue=0
)
inputs['autostart']['timer'].grid(row=0, column=m)

m += 1

# - USB Interface
variables['autostart']['usb-interface'] = tk.IntVar()
inputs['autostart']['usb-interface'] = tk.Checkbutton(
    frames['autostart'],
    text='SNI / QUSB2SNES',
    variable=variables['autostart']['usb-interface'],
    onvalue=1,
    offvalue=0
)
inputs['autostart']['usb-interface'].grid(row=0, column=m)

m = 0

# - Tracker
variables['autostart']['tracker'] = tk.IntVar()
inputs['autostart']['tracker'] = tk.Checkbutton(
    frames['autostart'],
    text='Tracker',
    variable=variables['autostart']['tracker'],
    onvalue=1,
    offvalue=0
)
inputs['autostart']['tracker'].grid(row=1, column=m)

m += 1

# - Entrance tracker
variables['autostart']['entrance-tracker'] = tk.IntVar()
inputs['autostart']['entrance-tracker'] = tk.Checkbutton(
    frames['autostart'],
    text='Entrance tracker',
    variable=variables['autostart']['entrance-tracker'],
    onvalue=1,
    offvalue=0
)
inputs['autostart']['entrance-tracker'].grid(row=1, column=m)

m += 1

# - Door tracker
variables['autostart']['door-tracker'] = tk.IntVar()
inputs['autostart']['door-tracker'] = tk.Checkbutton(
    frames['autostart'],
    text='Door tracker',
    variable=variables['autostart']['door-tracker'],
    onvalue=1,
    offvalue=0
)
inputs['autostart']['door-tracker'].grid(row=1, column=m)

m += 1

# - Keydrop key count
variables['autostart']['keydrop'] = tk.IntVar()
inputs['autostart']['keydrop'] = tk.Checkbutton(
    frames['autostart'],
    text='Keydrop key count info',
    variable=variables['autostart']['keydrop'],
    onvalue=1,
    offvalue=0
)
inputs['autostart']['keydrop'].grid(row=1, column=m)

m, n = 0, n + 1

# Post-gen options frame
# TODO : reformat this
p = 0

frames['postgen'] = tk.LabelFrame(window, text='Post-gen options', bd=2)
frames['postgen'].grid(row=n, sticky=tk.W + tk.E)

frames['heart'] = tk.Frame(frames['postgen'], bd=2)
frames['heart'].grid(row=0, sticky=tk.W)

# Heart speed
labels['heartspeed'] = {}

labels['heartspeed']['main'] = tk.Label(frames['heart'], text='Heart speed', width=LBL_WIDTH, anchor=tk.W)
labels['heartspeed']['main'].grid(row=m, column=p)
p += 1

variables['heartspeed'] = {'off': tk.IntVar(), 'double': tk.IntVar(), 'normal': tk.IntVar(), 'half': tk.IntVar(),
                           'quarter': tk.IntVar()}

# Speed off
labels['heartspeed']['off'] = tk.Label(frames['heart'], text='Off', width=SPIN_WIDTH + 1)
labels['heartspeed']['off'].grid(row=m, column=p)
p += 1

inputs['heartspeed'] = {}

inputs['heartspeed']['off'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                         textvariable=variables['heartspeed']['off'])
inputs['heartspeed']['off'].grid(row=m, column=p)
p += 1

# Speed double
labels['heartspeed']['double'] = tk.Label(frames['heart'], text='Double', width=SPIN_WIDTH + 1)
labels['heartspeed']['double'].grid(row=m, column=p)
p += 1

inputs['heartspeed']['double'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                            textvariable=variables['heartspeed']['double'])
inputs['heartspeed']['double'].grid(row=m, column=p)
p += 1

# Speed normal
labels['heartspeed']['normal'] = tk.Label(frames['heart'], text='Normal', width=SPIN_WIDTH + 1)
labels['heartspeed']['normal'].grid(row=m, column=p)
p += 1

inputs['heartspeed']['normal'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                            textvariable=variables['heartspeed']['normal'])
inputs['heartspeed']['normal'].grid(row=m, column=p)
p += 1

# Speed half
labels['heartspeed']['half'] = tk.Label(frames['heart'], text='Half', width=SPIN_WIDTH + 1)
labels['heartspeed']['half'].grid(row=m, column=p)
p += 1

inputs['heartspeed']['half'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                          textvariable=variables['heartspeed']['half'])
inputs['heartspeed']['half'].grid(row=m, column=p)
p += 1

# Speed quarter
labels['heartspeed']['quarter'] = tk.Label(frames['heart'], text='Quarter', width=SPIN_WIDTH + 1)
labels['heartspeed']['quarter'].grid(row=m, column=p)
p += 1

inputs['heartspeed']['quarter'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                             textvariable=variables['heartspeed']['quarter'])
inputs['heartspeed']['quarter'].grid(row=m, column=p)

m += 1
p = 0

# Heart color
labels['heartcolor'] = {}
labels['heartcolor']['main'] = tk.Label(frames['heart'], text='Heart color', width=LBL_WIDTH, anchor=tk.W)
labels['heartcolor']['main'].grid(row=m, column=p)
p += 1

inputs['heartcolor'] = {}

variables['heartcolor'] = {'red': tk.IntVar(), 'blue': tk.IntVar(), 'green': tk.IntVar(), 'yellow': tk.IntVar()}

# Color red
labels['heartcolor']['red'] = tk.Label(frames['heart'], text='Red', width=SPIN_WIDTH + 1)
labels['heartcolor']['red'].grid(row=m, column=p)
p += 1

inputs['heartcolor']['red'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                         textvariable=variables['heartcolor']['red'])
inputs['heartcolor']['red'].grid(row=m, column=p)
p += 1

# Color blue
labels['heartcolor']['blue'] = tk.Label(frames['heart'], text='Blue', width=SPIN_WIDTH + 1)
labels['heartcolor']['blue'].grid(row=m, column=p)
p += 1

inputs['heartcolor']['blue'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                          textvariable=variables['heartcolor']['blue'])
inputs['heartcolor']['blue'].grid(row=m, column=p)
p += 1

# Color green
labels['heartcolor']['green'] = tk.Label(frames['heart'], text='Green', width=SPIN_WIDTH + 1)
labels['heartcolor']['green'].grid(row=m, column=p)
p += 1

inputs['heartcolor']['green'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                           textvariable=variables['heartcolor']['green'])
inputs['heartcolor']['green'].grid(row=m, column=p)
p += 1

# Color yellow
labels['heartcolor']['yellow'] = tk.Label(frames['heart'], text='Yellow', width=SPIN_WIDTH + 1)
labels['heartcolor']['yellow'].grid(row=m, column=p)
p += 1

inputs['heartcolor']['yellow'] = tk.Spinbox(frames['heart'], from_=0, to=100, width=SPIN_WIDTH,
                                            textvariable=variables['heartcolor']['yellow'])
inputs['heartcolor']['yellow'].grid(row=m, column=p)

m = 0

frames['gameoptions'] = tk.Frame(frames['postgen'], bd=2)
frames['gameoptions'].grid(row=1, sticky=tk.W + tk.E)

# BGM
variables['backgroundmusic'] = tk.IntVar()
inputs['backgroundmusic'] = tk.Checkbutton(frames['gameoptions'], text='Background music',
                                           variable=variables['backgroundmusic'], onvalue=1, offvalue=0)
inputs['backgroundmusic'].grid(row=0, column=m)
m += 1

# Quickswap
variables['quickswap'] = tk.IntVar()
inputs['quickswap'] = tk.Checkbutton(frames['gameoptions'], text='Quickswap', variable=variables['quickswap'],
                                     onvalue=1, offvalue=0)
inputs['quickswap'].grid(row=0, column=m)

m = 0

frames['sprites'] = tk.Frame(frames['postgen'], bd=2)
frames['sprites'].grid(row=1, sticky=tk.W)

# Edit sprites
buttons['editsprites'] = tk.Button(frames['sprites'], text='Sprites list', width=BTN_WIDTH)
buttons['editsprites'].grid(row=0, column=m)
m += 1

# Update sprites
buttons['updatesprites'] = tk.Button(frames['sprites'], text='Update sprites', width=BTN_WIDTH)
buttons['updatesprites'].grid(row=0, column=m)
m += 1

# Glitched logic
# TODO : override button, list available sprites
variables['linksprite'] = tk.IntVar()
inputs['linksprite'] = tk.Checkbutton(frames['sprites'], text='Force Link sprite (e.g. glitched logic)',
                                      variable=variables['linksprite'], onvalue=1, offvalue=0)
inputs['linksprite'].grid(row=0, column=m)

m, n = 0, n + 1

# Run frame
frames['run'] = tk.Frame(
    window,
    bd=2
)
frames['run'].grid(row=n, sticky=tk.W + tk.E)

labels['msu'] = tk.Label(
    frames['run'],
    text='MSU Pack',
    width=LBL_WIDTH,
    anchor=tk.W
)
labels['msu'].grid(row=0, column=0)

variables['msu'] = tk.StringVar()
variables['msu'].set('Default')
inputs['msu'] = tk.OptionMenu(
    frames['run'],
    variables['msu'],
    *['Default', 'Random']
)
inputs['msu'].config(width=ENTRY_WIDTH - 7)
inputs['msu'].grid(row=0, column=1)

buttons['msu'] = tk.Button(
    frames['run'],
    text='Refresh',
    width=BTN_WIDTH
)
buttons['msu'].grid(row=0, column=2)

n += 1

buttons['run'] = tk.Button(
    window,
    text='RUN'
)
buttons['run'].grid(row=n)

n += 1

labels['log'] = tk.Label(
    window,
    text='',
    anchor=tk.W,
    width=80
)
labels['log'].grid(row=n, sticky=tk.W)

# Main loop
utils.config(variables, 0)  # Load config

for x in defaults:
    utils.set_default_text(inputs[x], defaults[x])

if variables['mode'].get() == 0:
    utils.switch_frame(frames['transfer'].winfo_children(), frames['copy'].winfo_children())
else:
    utils.switch_frame(frames['copy'].winfo_children(), frames['transfer'].winfo_children())

labels['rom'].config(state='disabled')
inputs['rom'].config(state='disabled')
buttons['rom'].config(state='disabled')
for child in frames['heart'].winfo_children():
    child.configure(state='disabled')
for child in frames['gameoptions'].winfo_children():
    child.configure(state='disabled')
for child in frames['sprites'].winfo_children():
    child.configure(state='disabled')

# Set commands
buttons['seed'].configure(command=lambda: utils.set_path(
    variables['seed'],
    inputs['seed'],
    0))
buttons['rom'].configure(command=lambda: utils.set_path(
    variables['rom'],
    inputs['rom'],
    0))
buttons['emulator'].configure(command=lambda: utils.set_path(
    variables['emulator'],
    inputs['emulator'],
    0))
buttons['folder-path'].configure(command=lambda: utils.set_path(
    variables['folder-path'],
    inputs['folder-path'],
    1))
buttons['retroarch-core'].configure(command=lambda: utils.set_path(
    variables['retroarch-core'],
    inputs['retroarch-core'],
    0))
buttons['timer'].configure(command=lambda: utils.set_path(
    variables['timer'],
    inputs['timer'],
    0))
buttons['tracker'].configure(command=lambda: utils.set_path(
    variables['tracker'],
    inputs['tracker'],
    0))
buttons['entrance-tracker'].configure(command=lambda: utils.set_path(
    variables['entrance-tracker'],
    inputs['entrance-tracker'],
    0))
buttons['door-tracker'].configure(command=lambda: utils.set_path(
    variables['door-tracker'],
    inputs['door-tracker'],
    0))
buttons['usb-interface'].configure(command=lambda: utils.set_path(
    variables['usb-interface'],
    inputs['usb-interface'],
    0))
inputs['mode'][0].configure(command=lambda: utils.switch_frame(
    frames['transfer'].winfo_children(),
    frames['copy'].winfo_children()))
inputs['mode'][1].configure(command=lambda: utils.switch_frame(
    frames['copy'].winfo_children(),
    frames['transfer'].winfo_children()))
buttons['detect'].config(command=lambda: fxpak.detect(
    variables,
    labels['log']))
buttons['msu'].config(command=lambda: utils.refresh(
    variables,
    inputs['msu'],
    labels['log']))
buttons['run'].config(command=lambda: utils.run(
    variables,
    defaults,
    labels['log']))

# sprites.build_dict()
# sprites.load_sprites()
# var_patch.set(0)

window.mainloop()

utils.config(variables, 1)
# sprites.save_sprites()
