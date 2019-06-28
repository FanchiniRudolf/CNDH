import subprocess


comando = 'vlc --play-and-exit --no-video-deco --no-embedded-video -f --one-instance --no-playlist-enqueue  assetsCNDH\\directorio.mp4'
subprocess.run(comando, shell=True)
