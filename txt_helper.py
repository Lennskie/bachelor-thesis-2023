from make_file import *

def txt_function(filename, extension):
    user_input = input('Type what you want to write in the file \nTyping nothing will insert nothing:')
    make_file_txt(filename, extension, user_input)