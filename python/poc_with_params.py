from make_files import make_file_default
from txt_helper import txt_function

# Make this file so params are supported when launching this python file from the terminal

import sys, getopt

def main(argv):
    filename = ''
    extension = ''
    path = ''
    opts, args = getopt.getopt(argv,"hf:e:p:")
    for opt, arg in opts:
        if opt == '-h':
            print ('poc_with_params.py -f <filename> -e <extension> -p <path>')
            sys.exit()
        elif opt in ("-f"):
            filename = arg
        elif opt in ("-e"):
            extension = arg         
        elif opt in ("-p"):
            path = arg

    if(extension == "txt"):
        txt_function(filename, extension, path)
    else:
        make_file_default(filename, extension, path)

if __name__ == "__main__":
   main(sys.argv[1:])