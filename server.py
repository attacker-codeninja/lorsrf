#!/usr/bin/env python3

from flask import Flask,request
import sys,os,platform

colors = True  # Output should be colored
machine = sys.platform  # Detecting the os of current system
checkplatform = platform.platform() # Get current version of OS
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False  # Colors shouldn't be displayed in mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')   # Enables the ANSI
if not colors:
    end = red = white = green = yellow = run = bad = good = bold = info = que = ''
else:
    white = '\033[97m'
    green = '\033[92m'
    red = '\033[91m'
    yellow = '\033[93m'
    end = '\033[0m'
    back = '\033[7;91m'
    bold = '\033[1m'
    blue = '\033[94m'
    info = '\033[93m[!]\033[0m'
    que = '\033[94m[?]\033[0m'
    bad = '\033[91m[-]\033[0m'
    good = '\033[92m[+]\033[0m'
    run = '\033[97m[~]\033[0m'
    grey = '\033[7;90m'
    cyan='\u001B[36m'
    gray = '\033[90m'
print('''
{red}{bold}
\t _            ___      __ 
\t| |   ___ _ _/ __|_ _ / _|
\t| |__/ _ \ '_\__ \ '_|  _|
\t|____\___/_| |___/_| |_|  
\t
\t{yellow}{bold}# Coded By : Khaled Nassar @knassar702
{end}
	'''.format(red=red,bold=bold,yellow=yellow,end=end))
port = int(sys.argv[1])

app = Flask(__name__)

@app.route('/<param>',methods=['GET','POST'])
def index(param):
	if request.method == 'POST':
		print(f'POST [ {param} ]')
		print(request.headers)
	else:
		print(f'GET [ {param} ]')
		print(request.headers)
	return 'okie'
if __name__ == '__main__':
	app.run(port=port)
