from make_files import *
import random

def txt_function(filename, extension, path):
    user_input = input('Type what you want to write in the file \nIf nothing is added it will generate some random numbers:')
    if(user_input == ""):
        user_input = str(random.randint(1,1000) + random.randint(1,1000) + random.randint(1,1000))
    make_file_txt(filename, extension, path, user_input)