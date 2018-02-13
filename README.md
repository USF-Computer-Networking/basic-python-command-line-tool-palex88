# basic-python-command-line-tool-palex88

This is a basic command line program used to test out argsparse python library.

Using python 3.6. Usage: `python main.py [args]`

Possible options:
* '-h' or '--help'
* '-v' or '--verbose', default=False, action='store_true', help='increase verbosity')
* '-n' or '--number', type=int, default=1, help='print up to this number')
* '-na' or '--name', help='Your name')
* '-ps' or '--progress', help='see a progress bar for the number')
* '-w' or '--who', help='look up a domain')
* '-f' or '--file', help='create a new file txt file, do not specify file type')
* '-l' or '--list', default=False, action='store_true', help='list all txt files')
* '-df' or '--delete', help='delete a txt file, specify a file type')
