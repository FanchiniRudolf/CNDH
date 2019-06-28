import subprocess

comando = 'vlc vlc://quit '
subprocess.run(comando, shell=True)