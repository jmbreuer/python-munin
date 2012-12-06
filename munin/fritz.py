
import os, sys, urllib2
from BeautifulSoup import BeautifulSoup

from munin import MuninPlugin

class MuninFritzPlugin(MuninPlugin):
    category = "FritzBox"
    default_host = "fritz.box"

    def __init__(self):
        super(MuninFritzPlugin, self).__init__()
        self.hostname = (sys.argv[0].rsplit('_', 1)[-1] or os.environ.get('FRITZBOX_HOSTNAME') or self.default_host)

    def getpage(self, name):
        return urllib2.urlopen('http://'+self.hostname+'/cgi-bin/webcm?getpage=..%2Fhtml%2Fde%2Finternet%2F'+name+'&lang=de&lang=de&pagename=inetstat&menu=internet')

    def getcontents(self, name):
        return BeautifulSoup(self.getpage(name))

    def autoconf(self):
        return bool(self.getpage('adsl.html'))

    def gettable(self, name):
        return self.getcontents(name).findAll('tr')
