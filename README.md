# Introduction
This repo is made for my Bachelor Thesis of 2023.
This tool lets you create a new file that will have a listener on it to check if it has been accessed by someone.

Ideally, you want to name it something the hacker might want to access like 'passwords.txt' (this is the default name, explained below).

This project has been made it Python 3.10 and will only work in versions matching or higher, because the `match` function has only been introduced in 3.10.

# How to use and usecases

`python poc.py`
It will ask for a filename and extension.
Do **not** add a dot to the extension, this happens automatically

Example params:
filename: test
extension: txt
path: C:/users/user/Desktop/

> This will create C:/users/user/Desktop/test.txt
>
> These files **cannot** be moved without breaking the code, so please select the correct folder on your first set-up.
> You'll have to add the last slash at the end of your path for this to work like the example

The default will be "passwords.txt", if nothing is supplied.

# Current support of file types
These files can have custom text in them, so they don't appear as 0kb files.
- `.txt`

# Flow
poc   ->   make_files  ->  access_checker -> make_json

↳ txt_helper ⮥   

# TODO
Add to the README:
- Show how a python file can forever be ran on Linux
- Better showcase of the flow

Add to the code:
- A way for the user to see their files & if they are accessed in a remote / better way
- Make listeners so you can add more files and see which one changed.