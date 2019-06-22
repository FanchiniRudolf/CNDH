import subprocess


comando = 'vlc --play-and-exit --no-video-deco -f assetsCNDH\\directorio.mp4'
subprocess.run(comando, shell=True)
