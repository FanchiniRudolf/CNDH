import subprocess


comand = 'vlc --play-and-exit --no-video-deco --no-embedded-video --one-instance --no-playlist-enqueue -f assetsCNDH\\directorio.mp4'
subprocess.run(comand, shell=True)
