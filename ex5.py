import os
import ex5functions


class MyClassEx:
    def ex1(self):
        print('File to parse: ')
        input_file = input()
        ex5functions.parse_file(input_file)

    def ex2(self):
        print('Name of the new container: ')
        name_new_container = input()
        ex5functions.create_new_container(name_new_container)

    def ex3(self):
        print('Input to resize (extension required):')
        f1 = input()
        print('Width = ')
        width = input()
        print('Height = ')
        height = input()
        print('Where you want to save the file (extension required)')
        f2 = input()
        ex5functions.resize(width, height, f1,f2)

    def ex4(self):
        print('File to detect the standard: ')
        input_file = input()
        ex5functions.broadcast_standard_type(ex5functions.detect_audio_formats(input_file))
