import os
def ex4(video_name):
    check_command = 'ffprobe -i {} -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1 -v 0 > channel_layouts.txt'.format(
        video_name)
    os.system(check_command)
    archivo = open("channel_layouts.txt")
    channel_layouts = archivo.readline()
    if channel_layouts == 'mono\n':
        mono2stereo = 'ffmpeg -i {} -ac 2 stereo.mp3'.format(video_name)
        os.system(mono2stereo)
        check_command = 'ffprobe -i mono.mp3 -show_entries stream=channel_layout -select_streams a:0 -of compact=p=0:nk=1 -v 0 > channel_layouts_check.txt'
        os.system(check_command)
