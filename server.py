#!/usr/bin/env python3

from flask import Flask,request
import sys

if len(sys.argv) < 3:
	print(f'Usage : {sys.argv[0]} HOST PORT')
else:
	host = sys.argv[1]
	port = int(sys.argv[2])

app = Flask(__name__)

@app.route('/<param>',methods=['GET','POST'])
def index(param):
	if request.method == 'POST':
		print(f'[ {param} ]')
		print(request.headers)
	else:
		print(f'[ {param} ]')
		print(request.headers)
	return 'okie'
if __name__ == '__main__':
	app.run(host=host,port=port)