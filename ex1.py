import os

# guardo la info en un archivo de texto
command = 'ffprobe -i BigBuckBunny_512kb.mp4 2> file.txt'
os.system(command)


lines2mark = 'Stream'

# list_lineas[]-> se guarda o se imprime

with open('file.txt', 'r') as file:
    for line in file:
        for word in line.split():
            if word == lines2mark:
                print(line)

