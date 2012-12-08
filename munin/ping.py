
import os, sys, urllib2

from tools.ping import Ping

from munin import MuninPlugin

class MuninPingPlugin(MuninPlugin):
    category = "network"

    def __init__(self):
        super(MuninPingPlugin, self).__init__()

    def getPing(self, host):
        return Ping(host, timeout=1000, packet_size=55, out=False)
