from txt_helper import txt_function	
from make_file import *

# Take user input and set it to the filename variable
filename = input("Enter the name of the file \nDefault is 'passwords' if no name is entered:")
if(filename == ""): #Check if a default name is needed
    filename="passwords"

extension = input("Enter the extension of the file (without the dot) \nDefault is 'txt' if no extension is entered:")
if(extension == ""): #Check if a default extension is needed
    extension="txt"

# Check what kind of file it is an if a write function is possible
match extension:
    case 'txt':
        txt_function(filename, extension)
    case _:
        make_file_default(filename, extension)