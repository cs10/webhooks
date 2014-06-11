# This file is a type of generic deploy script for github repos.
# This file can run on Python3.

# Sys Utils
import sys, os, datetime, json
# Helper Methods for dealings with repos.
# THIS CONTAINS THE ACTUAL SCRIPTS
from RepoConfig import *
# This gives:
# RepoConfig
#   getRepo(string: name)


###############################################################################
# Setup...

# Store the POST data from GitHub
params = ''
# Logs location
# This is relative to help with script portability. :)
folder = "./"
# Log files
repo_file = folder + "github_log_"
generic   = folder + "python_log.txt"
FILE      = ''
EVENT     = None
DATA      = {}
NAME      = None

###############################################################################
# Util Functions

def writeFile(file, message):
    print("FILE...   " + file)
    sep = '*' * 80
    with open(file, "a+") as myfile:
        myfile.write('\n\n\n' + sep + '\n')
        myfile.write(str(datetime.datetime.now()) + '\n')
        myfile.write(message)
        myfile.close()

def getRepoName():
    if 'repository' in DATA:
        if 'name' in DATA['repository']:
            return DATA['repository']['name']
    return None

###############################################################################
# The Work Goes Here...

try:
    # Data gets passed in WITH SPACES...
    # Skip first item of array, and last item
    # HOWEVER -- perhaps we can be smarter about last item errors.
    # If a POST option can't be parsed...
    last = -2
    if sys.argv[-2] == '}':
        last = -1
    params = ' '.join(sys.argv[1:-1])
    DATA   = json.loads(params)
except:
    DATA = {}
    FILE = generic

print(DATA)
if len(sys.argv) > 2:
    # Event should then be the very last item..
    EVENT = sys.argv[-1]

NAME = getRepoName()

# Can't do a pull, so log the message and quit
if DATA == {} or NAME == None:
    msg = "CAN'T PARSE REPO NAME...\n"
    msg += "PARAMS:\t" + str(params) + '\n'
    msg += "EVENT:\t" + EVENT + '\n'
    msg += "NAME:\t" + str(NAME) + '\n'
    writeFile(FILE, msg)
    sys.exit(1)

FILE = repo_file + NAME + '.txt'
# Start
msg = "EVENT:\t" + EVENT + '\n'
repo = RepoConfig.getRepo(NAME)
try:
    repo.deploy()
    msg += "Repo Deployed Successfully!\n"
except Exception as error:
    import traceback
    msg += "ERROR OCCURRED:\n" + str(error) + '\n'
    msg += "TRACEBACK: \n" + traceback.print_exc()
finally:
    writeFile(FILE, msg)

# used purely for debugging PHP quickly
print('Python Script Finished')