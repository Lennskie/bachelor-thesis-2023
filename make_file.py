import os
from access_checker import access_checker

def make_file_default(filename, extension):

    #Make the file including the extension
    filename = filename + "." + extension

    # Check if the file exists, if it does, re-write it. If it doesn't, make it a new one
    if(os.path.exists(filename)):
        os.remove(filename)
        print("The file " + filename + " exists, deleting it and making a new one")
    else:
        print("The file " + filename + " does not exist")

    access_checker(filename)

def make_file_txt(filename, extension, user_input):

    #Make the file including the extension
    filename = filename + "." + extension

    # Check if the file exists, if it does, re-write it. If it doesn't, make it a new one
    if(os.path.exists(filename)):
        os.remove(filename)
        print("The file " + filename + " exists, deleting it and making a new one")
    else:
        print("The file " + filename + " does not exist")

    #This is a copy of the previous code because the code calls the access_checker fucntion and thus cannot be re-used.


    # write the user input to the file
    with open(filename, "w") as file:
        file.write(user_input)


    access_checker(filename)
