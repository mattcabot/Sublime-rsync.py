#!/usr/bin/env python
from os import popen
from os.path import exists, join
from sublime import active_window, error_message
from sublime_plugin import EventListener


def rsync(source, dest):
    source = source.replace(" ","\\ ")
    dest = dest.replace(" ","\\ ")
    cmd = "/usr/bin/rsync -rtu --delete %s %s" % (source,dest)
    popen(cmd)


class ShebangPythonListener(EventListener):
    def rsync_sh(self, source):
        f = join(source,"rsync.sh")
        if exists(f):
            popen(f)

    def rsync_txt(self, source):
        f = join(source,"rsync.txt")
        if exists(f):
            dest = open(f).read()
            rsync(source, dest)

    def rsync_dir(self, source):
        self.rsync_txt(source)
        self.rsync_sh(source)

    def on_post_save(self, view):
        try:
            for source in active_window().folders():
                self.rsync_dir(source)
        except Exception, e:
            error_message(str(e))
