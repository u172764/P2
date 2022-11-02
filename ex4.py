import os

# Explain in which broadcasting standard the video can fit

command = 'ffprobe -i output_package.mp4 2> file.txt'
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

"""
The standards are:
    DVB: Video  = MPEG2 (mpeg2video), h.264 (h264)      Audio = AAC (aac), AC-3 (ac3) and MP3 (mp3)
    ISDB: Video = MPEG2, h.264                          Audio = AAC (aac)
    ISDB-Tb Brazilian and Latam : Video = h.246         Audio = AAC (aac_latm)
    ATSC: Video = MPEG2, h.264                          Audio = AC-3 (ac3)
    DTMB: Video = AVS (avs), AVS+ (avs2) , MPEG2, h.264 Audio = DRA (dra) , AAC (aac), AC-3 (ac3) , MP2 (mp2) , MP3 (mp3)
"""

#ONLY AUDIO
for format in formats:
    if format in


