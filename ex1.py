import os


def parse_file():
    command = 'ffprobe -i output_package.mp4 2> file.txt'
    os.system(command)
    lines2mark = ['Stream', 'Input', 'Duration:']
    with open('file.txt', 'r') as file:
        for line in file:
            #print(line)
            for word in line.split():
                if word == lines2mark[0] or word == lines2mark[1] or word == lines2mark[2]:
                    print(line)


parse_file()
