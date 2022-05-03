from cx_Freeze import setup, Executable

base = None    

executables = [Executable("PASSWORD MANAGER.py", base=base)]

packages = ["idna","PyQt5","cryptography","pickle","images"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "pswdmang",
    options = options,
    version = "0.1",
    description = 'Password Manager that uses MySQL database to store data.',
    executables = executables
)