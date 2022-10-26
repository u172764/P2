import os
import ex5functions
command = 'ffmpeg -i BigBuckBunny_512kb.mp4 -ss 00:00:00 -to 00:01:00 -c:v copy -c:a copy video_cortado.mp4'
os.system(command)

command2 = 'ffmpeg -i video_cortado.mp4 -vn -acodec copy audio_salida.mp3'
os.system(command2)

ex5functions.ex4('audio_salida.mp3')

command4 = 'ffmpeg -i video_cortado.mp4 -c:a aac -b:a 10k output.m4a'
os.system(command4)

'ffmpeg -i video.mkv -i audio.mp3 -map 0 -map 1:a -c:v copy -shortest output.mkv'

https://stackoverflow.com/questions/11779490/how-to-add-a-new-audio-not-mixing-into-a-video-using-ffmpeg