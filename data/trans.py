import os

cmdStr = 'ffmpeg-normalize o_mp3/%s -c:a libmp3lame -nt peak --target-level 0 -o mp3/%s'

for fname in os.listdir('o_mp3'):
    os.system(cmdStr % (fname, fname))

