import sys, os, datetime

name = "github_event_" + str(datetime.datetime.now())
log = "../web_hook_log.txt"

with open(name, "w+") as myfile:
    #os.chmod(name, 0744)
    myfile.write('\n ')
    if len(sys.argv) > 1:
        myfile.write(sys.argv[1])
    myfile.close()

with open(log, "a") as myfile:
    myfile.write(str(datetime.datetime.now()) + '\n\n')
    if len(sys.argv) > 1:
        myfile.write(sys.argv[1])
        myfile.write('\n\n\n')
    myfile.close()
