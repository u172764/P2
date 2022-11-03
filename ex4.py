import os


# Explain in which broadcasting standard the video can fit

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

    print(formats)
    return formats


"""
The standards are:
    DVB: Video  = MPEG2 (mpeg2video), h.264 (h264)      Audio = AAC (aac), AC-3 (ac3) and MP3 (mp3)
    ISDB: Video = MPEG2, h.264                          Audio = AAC (aac)
    ISDB-Tb Brazilian and Latam : Video = h.246         Audio = AAC (aac_latm)
    ATSC: Video = MPEG2, h.264                          Audio = AC-3 (ac3)
    DTMB: Video = AVS (avs), AVS+ (avs2) , MPEG2, h.264 Audio = DRA (dra) , AAC (aac), AC-3 (ac3) , ###MP2 (mp2) , MP3 (mp3)
"""


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
    elif ac3 == len(formats):
        print('DVB or ATSC or DTMB')
    elif aac_latm == len(formats):
        print('ISDB_Tb')
    elif mp3 == len(formats):
        print('DVB or DTMB')
    elif mp2 > 0 or dra > 0:
        print('DTMB')
    else:
        print('DTMB or DVB')


videoname = 'BigBuckBunny_512kb.mp4'
broadcast_standard_type(detect_audio_formats(videoname))
