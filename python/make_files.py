import os
from access_checker import access_checker

def make_file_default(filename, extension, path):

    #Make the file including the extension
    filename = path + filename + "." + extension

    # Check if the file exists, if it does, re-write it. If it doesn't, make it a new one
    if(os.path.exists(filename)):
        os.remove(filename)
        print("The file " + filename + " exists, deleting it and making a new one")
    else:
        print("The file " + filename + " does not exist, making a new one")

    # make a file with the os package
    with open(filename, "w") as file:
        file.close()

    access_checker(filename)

def make_file_txt(filename, extension, path, user_input):

    #Make the file including the extension
    filename = path + filename + "." + extension

    # Check if the file exists, if it does, re-write it. If it doesn't, make it a new one
    if(os.path.exists(filename)):
        os.remove(filename)
        print("The file " + filename + " exists, deleting it and making a new one")
    else:
        print("The file " + filename + " does not exist, making a new one")


    # write the user input to the file
    with open(filename, "w") as file:
        file.write(user_input)


    access_checker(filename)
