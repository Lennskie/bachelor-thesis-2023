# Introduction
This repo is made for my Bachelor Thesis of 2023.
It includes a tool to make a new file with a custom name and extension and will forever check if the file has been accessed.

Ideally, you want to name it something the hacker might want to access like 'passwords.txt'.

# How to use and usecases

`python poc.py`
It will ask for a filename and extension.
Do **not** add a dot to the extension, this happens automatically

The default will be "passwords.txt", if nothing is supplied.

# Current support of file types
These files can have custom text in them, so they don't appear as 0kb files.
- `.txt`

# TODO
Add to the README:
- Show how a python file can forever be ran on Linux

Add to the code:
- A way for the user to see their files & if they are accessed in a remote / better way