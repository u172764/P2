import os


# I will inform about the Input, the Duration and Streams (these are important characteristics for next exercises)
def parse_file(filename):
    command = 'ffprobe -i {} 2> file.txt'.format(filename)
    os.system(command)
    lines2mark = ['Stream', 'Input', 'Duration:']
    with open('file.txt', 'r') as file:
        for line in file:
            for word in line.split():
                if word == lines2mark[0] or word == lines2mark[1] or word == lines2mark[2]:
                    print(line)


file_name = 'BigBuckBunny_512kb.mp4'
parse_file(file_name)
