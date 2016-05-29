# -*- coding: utf8 -*-
__author__="Chris Park(namegpark@gmail.com)"

import datetime, traceback

class logmon(object):
    def __init__(self, logname="logmon", savepath="/"):
        if savepath[-1] != "/":
            savepath = savepath + "/"

        self.logname = logname
        self.savepath = savepath
        self.now_time = self.getNowTime().split(' ')[0]
        self.handle = open(self.savepath + self.now_time + '_' + self.logname + ".log", 'a')

    def write(self, title="", body=""):
        nowtime = self.getNowTime()
        self.handle.write("[" + nowtime + "] " + title + "\nBody: " + body + "\n")

    def exit(self):
        self.handle.close()

    def getNowTime(self):
        return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")