
import os, sys, urllib2

from tools.ping import Ping

from munin import MuninMultiGraphPlugin

class MuninPingPlugin(MuninMultiGraphPlugin):
    category = "network"

    def __init__(self):
        super(MuninPingPlugin, self).__init__()

    def getPing(self, host):
        return Ping(host, timeout=1000, interval=100, packet_size=55, out=False)
