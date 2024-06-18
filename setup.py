from cx_Freeze import setup, Executable
import sys
# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], 'silent_level': 3}

base = "Win32GUI"

executables = [
    Executable('main.py', base=base, icon= "icon.ico")
    
]

setup(name='Gerador de imagem para aniversariantes',
      version = '1.0',
      description = 'Gera imagens de Aniversario para os medicos',
      options = {'build_exe': build_options},
      executables = executables)