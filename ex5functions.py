import os


def parse_file(filename):
    command = 'ffprobe -i {} 2> file.txt'.format(filename)
    os.system(command)
    lines2mark = ['Stream', 'Input', 'Duration:']
    with open('file.txt', 'r') as file:
        for line in file:
            for word in line.split():
                if word == lines2mark[0] or word == lines2mark[1] or word == lines2mark[2]:
                    print(line)


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


def resize(w, h, file1, file2):
    command = 'ffmpeg -i {} -vf scale={}:{} {}'.format(file1, w, h, file2)
    os.system(command)


def detect_audio_formats(videoname):
    command = 'ffprobe -i {} 2> file.txt'.format(videoname)
    os.system(command)
    lines2mark = ['Stream', 'Audio']
    formats = []
    with open('file.txt', 'r') as file:
        for line in file:
            line2 = line.split(" ")
            for word in line2:
                if word == lines2mark[0] and line2[4] == 'Audio:':
                    formats.append(line2[5])
    return formats


def broadcast_standard_type(formats):
    # ONLY AUDIO
    aac = 0
    ac3 = 0
    aac_latm = 0
    mp3 = 0
    mp2 = 0
    dra = 0
    for format in formats:
        if format == 'aac':
            aac = aac + 1
        if format == 'ac3':
            ac3 = ac3 + 1
        if format == 'aac_latm':
            aac_latm = aac_latm + 1
        if format == 'mp3':
            mp3 = mp3 + 1
        if format == 'mp2':
            mp2 = mp2 + 1
        if format == 'dra':
            dra = dra + 1

    if aac == len(formats):
        print('ISDB or DVB or DTMB')
    if ac3 == len(formats):
        print('DVB or ATSC or DTMB')
    if aac_latm == len(formats):
        print('ISDB_Tb')
    if mp3 == len(formats):
        print('DVB or DTMB')
    if mp2 > 0 or dra > 0:
        print('DTMB')
    else:
        print('DTMB or DVB')
