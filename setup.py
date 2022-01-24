import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# 'packages': ['os'] is used as example only
build_exe_options = {
    'include_files': [('resources/icon.ico', 'resources/icon.ico')],
    'optimize': 2}

# base='Win32GUI' should be used only for Windows GUI app
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='ALTTPR Helper',
    version='3.0',
    description='An helper to solve my laziness problems',
    options={'build_exe': build_exe_options},
    executables=[Executable('gui.py', base=base, icon='resources/icon.ico', target_name='Helper')]
)
