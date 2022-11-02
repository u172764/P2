# resize (resolution change) of any input given
import os


def resize(w, h, file1, file2):
    command = 'ffmpeg -i {} -vf scale={}:{} {}'.format(file1, w, h, file2)
    os.system(command)


print('Input to resize (extension required):')
f1 = input()
print('Width = ')
width = input()
print('Height = ')
height = input()
print('Where you want to save the file (extension required)')
f2 = input()

resize(width, height, f1, f2)
