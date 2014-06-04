print("Running Pull Script")

import sys, os, datetime

name = "/home/ff/cs10/logs/wgithub_event_" + str(datetime.datetime.now()) + ".txt"
log = "/home/ff/cs10/logs/web_hook_log.txt"
with open(name, "w+") as myfile:
    #os.chmod(name, 0744)
    myfile.write('writing... \n ')
    if len(sys.argv) > 1:
        myfile.write(sys.argv[1])
    myfile.close()

with open(log, "a") as myfile:
    myfile.write(str(datetime.datetime.now()) + '\n\n')
    myfile.write("Hmmmm.... \n")
    if len(sys.argv) > 1:
    	myfile.write(sys.argv[1])
        myfile.write('\n\n\n')
    myfile.close()
