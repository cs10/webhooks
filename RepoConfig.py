# A repo configuration for the build script.

class RepoConfig(object):
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
        self.zipURL  = ''
        # TODO: Advanced events:
        # (branch, event): function
        self.setZipURL()
        RepoConfig.registry[name] = self

    def deploy(self):
        self.deployEvent('push')

    def deployEvent(self, event):
        '''
        Execute the event function
        Push is currently special cased until this class is a bit more
        robust
        '''
        if event in self.events:
            self.events[event]()

    def setZipURL(self):
        self.zipURL = RepoConfig.ghURL + self.account + "/" + self.name + "/"
        self.zipURL += self.branch + ".zip"

    def getZipURL(self):
        return self.zipURL

    def setFunction(self, branch, event, func):
        pass
        
    @classmethod
    def getRepo(cls, name):
        if name in cls.registry:
            return cls.registry[name]

###############################################################################
# UTIL FUNCTIONS AND SETTINGS
TMP = "/tmp/"

###############################################################################
# DEPLOY FUNCTIONS

def labsBJC():
    pass

def labsCS10():
    pass

def snap():
    pass

def fa14():
    pass

def resources():
    pass

###############################################################################
# SETUP FUNCTIONS

Repos = RepoConfig

RepoConfig('fa14', 'cs10', fa14)
RepoConfig('bjc-r', 'beautyjoy', labsCS10)