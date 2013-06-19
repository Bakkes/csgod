from cx_Freeze import setup, Executable

build_exe_options = {
    'includes': ['win32api'],
    'include_files': [("csgod/hooks", "hooks")]
}

setup(
    name='csgod',
    version='0.1',
    description='Daemon that provides automations for Counter-Strike: Global Offensive, including auto demo recording.',
    options={'build_exe': build_exe_options},
    executables=[Executable("csgod.py")]
)
