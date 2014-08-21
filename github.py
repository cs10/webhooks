try:
    # This file is a type of generic deploy script for github repos.
    # This file can run on Python3.

    # Sys Utils
    import sys, os, datetime, json, urllib.parse
    # Helper Methods for dealings with repos.
    # THIS CONTAINS THE ACTUAL SCRIPTS
    from RepoConfig import *
    # This gives:
    # RepoConfig
    #   getRepo(string: name)


    ###############################################################################
    # Setup...

    # Option to run from a separate location
    EXEC_LOC  = '/home/ff/cs10/public_html'

    # Logs location
    folder    = '/home/ff/cs10/github'
    # Log files
    repo_file = folder + "github_log_"
    generic   = folder + "python_log.txt"
    LOG_FILE  = ''
    # Store the POST data from GitHub
    # Raw data will be url encoded
    rawData   = ''
    rawHeader = ''
    NAME      = None #FIXME this is a crappy name
    EVENT     = None
    HEADER    = {}
    DATA      = {}

    # Make sure we're in the right location
    os.chdir(EXEC_LOC)

    # FIXME THIS IS TEMPORARY AND SHOULD BE DELETED SOON!!!
    # This needs to be run from the account the script ran on the first time
    os.system('rm -r /home/ff/cs10/public_html/fa14')

    ###############################################################################
    # Util Functions

    def writeFile(file, message):
        print("LOG_FILE...   " + file)
        sep = '*' * 80
        with open(file, "a+") as myfile:
            myfile.write('\n' + sep + '\n')
            myfile.write(str(datetime.datetime.now()) + '\n')
            myfile.write(str(message) + '\n')
            myfile.close()

    def getRepoName(ghResp):
        if 'repository' in ghResp:
            if 'name' in ghResp['repository']:
                return ghResp['repository']['name']
        return None

    def getGHEvent(ghHeader):
        key = 'X-GitHub-Event'
        if key in ghHeader:
            return ghHeader[key]
        return None

    ###############################################################################
    # The Work Goes Here...

    # RUN FORMAT
    # github.py RequestData RequestHeaders
    try:
        rawData    = sys.argv[1]
        rawHeaders = sys.argv[2]
    except (IndexError):
        if rawData == '':
            print('ERROR: No input data found; exiting')
            exit(1)
        else:
            print('ERROR: No headers found! Attempting to continue.')

    # Convert data to Python dicts
    dataStr   = urllib.parse.unquote(rawData)
    headerStr = urllib.parse.unquote(rawHeader)
    DATA      = json.loads(dataStr)
    HEADER    = json.loads(headerStr)
    NAME      = getRepoName(DATA)
    EVENT     = getGHEvent(HEADER)

    # Can't do a pull, so log the message and quit
    if DATA == {} or NAME == None:
        msg = "CAN'T PARSE REPO NAME...\n"
        msg += "PARAMS:\t" + str(params) + '\n'
        msg += "EVENT:\t" + str(EVENT) + '\n'
        msg += "NAME:\t" + str(NAME) + '\n'
        writeFile(LOG_FILE, msg)
        sys.exit(1)

    LOG_FILE = repo_file + str(NAME) + '.txt'
    # Start
    msg = "EVENT:\t" + str(EVENT) + '\n'
    repo = RepoConfig.getRepo(NAME)
    try:
        repo.deploy()
        msg += "Repo Deployed Successfully!\n"
    except Exception as error:
        # import traceback
        msg += "ERROR OCCURRED:\n" + str(error) + '\n'
        # msg += "TRACEBACK:\n" + traceback.print_exc()
        print(msg)
    finally:
        writeFile(LOG_FILE, msg)

    # used purely for debugging PHP quickly
    print('Python Script Finished')

except Exception as e:
    print(e)