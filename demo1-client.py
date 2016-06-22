#!/usr/bin/env python

import urllib3
import json
from sys import argv
import os
import re  
from ftplib import FTP
from subprocess import call

os.chdir('/home/rockwyc992/code/uva')

def greatest_version(homework, student):
    versions = []  
    version = 1
    regex = re.compile('PH%s_%s_v([0-9]+)\.zip' % (homework, student))
    ls = os.listdir()

    def match(s):  
        m = regex.match(s)  
        if m:  
            return int(m.group(1))

    version = max([x for x in map(match, ls) if x] + [0]) + 1
    return version

args = len(argv)
homework = 1
version = '1'
student = '102502044'
if args == 4:
    homework = argv[1]
    version = argv[2]
    student = argv[3]
elif args == 3:
    homework = argv[1]
    version = argv[2]
elif args == 2:
    homework = argv[1]
    version = greatest_version(homework, student)
else:
    print('Usage: ' + argv[0] + ' homework [version] [student]')
    exit()

print('Getting problem homework list fom https://uvaph.seal.tw/ph/' + homework)
urllib3.disable_warnings()
http = urllib3.PoolManager()
request = http.request('GET', 'https://uvaph.seal.tw/ph/' + homework)
data = json.loads(request.data.decode('ascii'))

print('Zipping source code')
zip_path = 'PH%s_%s_v%s.zip' % (homework, student, version)
zip_cmd = ['zip', '-q', zip_path]

for key in data:
    path = str(data[key]) + '.cpp'
    if os.path.isfile(path):
        zip_cmd.append(path)

call(zip_cmd)

print('Upload your zip file to ftp://pgp@uva.seal.tw')

ftp = FTP('uva.seal.tw') 
ftp.login('pgp', 'pgp204pgp')
bufsize = 1024
file_handler = open(zip_path, 'rb')
ftp.storbinary('STOR %s' % os.path.basename(zip_path), file_handler, bufsize)
file_handler.close() 
ftp.quit() 
