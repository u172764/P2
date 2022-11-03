import os


def create_new_container(new_name):
    # Cut BBB into 1 minute
    command1 = 'ffmpeg -i BigBuckBunny_512kb.mp4 -ss 00:00:00 -to 00:01:00 -c:v copy -c:a copy video_cortado.mp4'
    os.system(command1)

    # Export BBB(1min) audio as MP3
    command2 = 'ffmpeg -i video_cortado.mp4 audio1.mp3'
    os.system(command2)

    # Convert to stereo
    stereo = 'ffmpeg -i audio1.mp3 -ac 2 audio1_stereo.mp3'
    os.system(stereo)

    # Export BBB(1 min) audio in AAC w/ lower bitrate
    command3 = 'ffmpeg -i video_cortado.mp4 -vn -b:a 10k audio2.aac'
    os.system(command3)

    command4 = 'ffmpeg -i video_cortado.mp4 -i audio1_stereo.mp3 -i audio2.aac -map 0 -map 1 -map 2 -c copy ' \
               '-shortest {} '.format(new_name)
    os.system(command4)


name_new_container = 'new_container.mp4'
create_new_container(name_new_container)
