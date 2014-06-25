# A repo configuration for the build script.
try:
    import urllib.request as URL
    # import zipfile as zipfile
except ImportError: # Python 2
    import urllib as URL
    # import ZipFile as zipfile

import sys, os

"""
NOTE: The original goal was to use zip files to update repos, but
for projects with submodules this is a bit problematic. While it saves
or server space it can also lead to longer update times. Instead I'm
going to use the git repos. Currently this means public fetching should
be setup, or you can deal with SSH keys for the account this script is
running from.
"""

# TODO: Switch to subprocess.call()
class RepoConfig(object):
    GIT = "git"
    CLONE = "clone --recursive"
    NO_SSL = 'GIT_SSL_NO_VERIFY=true'
    PULL = 'pull'
    # Github URL
    ghURL = "https://github.com/"
    # Github ZIP
    # https://github.com/beautyjoy/llab/archive/master.zip
    # https://github.com/beautyjoy/bjc-r/archive/gh-pages.zip
    # https://github.com/cycomachead/snap/archive/feedback.zip
    registry = {}

    def __init__(self, name, account, branch, func):
        self.name    = name
        self.account = account
        self.branch  = branch
        # So far we really only care about pushes...
        self.events  = { 'push' : func }
        # TODO track URL separately and make use of it...
        self.url     = RepoConfig.ghURL + account + "/" + name + "/"
        self.dest    = name
        self.zipURL  = ''
        # FIXME THIS IS TERRIBLE......
        self.noSSL   = True
        # TODO: Advanced events:
        # (branch, event): function
        self.setZipURL()
        RepoConfig.registry[name] = self

    def deploy(self):
        self.deployEvent('push')

    def deployEvent(self, event):
        '''
        Execute the event function
        Push is currently special cased until this class
        is a bit more robust
        '''
        if event in self.events:
            self.events[event](self)

    def setZipURL(self):
        self.zipURL = RepoConfig.ghURL + self.account + "/" + self.name + "/"
        self.zipURL += self.branch + ".zip"

    def getZipURL(self):
        return self.zipURL

    def setFunction(self, branch, event, func):
        pass

    def repoExists(self):
        return os.path.exists(self.dest)

    def cloneCommand(self):
        command = ''
        if self.noSSL:
            command += RepoConfig.NO_SSL + ' '
        command += RepoConfig.GIT + ' ' + RepoConfig.CLONE + ' ' + self.url
        command += ' ' + self.dest
        return command

    def pullCommand(self):
        command = ''
        if self.noSSL:
            command += RepoConfig.NO_SSL + ' '
        return command + RepoConfig.GIT + ' ' + RepoConfig.PULL

    def update(self):
        if not self.repoExists():
            os.system(self.cloneCommand())
        else:
            os.system(self.pullCommand())

    @classmethod
    def getRepo(cls, name):
        if name in cls.registry:
            return cls.registry[name]

###############################################################################
# UTIL FUNCTIONS AND SETTINGS

TMP = "/tmp/"

def downloadfile(rc):
    # urllib
    # open request
    # .read()
    # .write() to new file named .zip()
    pass

def extractZip(rc):
    # Zipfile.ZipFile.extractall()
    pass

def cleanup(rc):
    pass

###############################################################################
# DEPLOY FUNCTIONS
# rc is a repo in the RepoConfig

def labsBJC(rc):
    pass

def labsCS10(rc):
    pass

def snap(rc):
    pass

def fa14(rc):
    rc.update()
    # FIXME -- I don't like this...
    os.system('chmod -R 777 /home/ff/cs10/public_html/fa14')
    os.system()

def resources(rc):
    pass

###############################################################################
# SETUP FUNCTIONS

Repos = RepoConfig

RepoConfig('fa14', 'cs10', fa14)
RepoConfig('bjc-r', 'beautyjoy', labsCS10)