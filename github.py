import sys, os, datetime

name = "github_event_" + str(datetime.datetime.now())

with open(name, "wt") as myfile:
    os.chmod(name, 0744)
    if len(sys.argv) > 1:
        myfile.write(sys.argv[1])
    myfile.close()