import subprocess


comando = 'vlc --play-and-exit --no-video-deco -f assetsCNDH\\prueba.mp4'
subprocess.run(comando, shell=True)
