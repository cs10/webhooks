# A repo configuration for the build script.

class RepoConfig(object):
    # Github URL
    # Github ZIP
    registry = {}

    def __init__(self, name, account, func):
        self.name    = name
        self.account = account
        # So far we really only care about pushes...
        self.events  = {'push' : func}
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

    def getZipUrl(self):
        return 'something'

    @classmethod
    def getRepo(cls, name):
        if name in cls.registry:
            return cls.registry[name]

###############################################################################
# UTIL FUNCTIONS

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