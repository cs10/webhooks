#!/usr/sww/bin/python3

print('Content-type: text/html')
print('')

print('<H1>Hello!</H1>')
import os, subprocess
print('imported...')
print('<br>')
print('PWD:')
print(os.getcwd())
print('<br>')
print(os.chdir('fa14'))
print('CD:')
print(os.getcwd())
print('<br>')
print(subprocess.getoutput('GIT_SSL_NO_VERIFY=true /usr/sww/bin/git pull'))
print('pulled')
print('<br>')
print(subprocess.getoutput('chmod -R 755 .'))
print('permissions updated.')