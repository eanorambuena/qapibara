from importlib import reload
import os
from time import sleep

import app

class Watch:
    """
    Watch a file and call a handler when it changes.
    Extracted from: https://stackoverflow.com/questions/182197/how-do-i-watch-a-file-for-changes
    https://stackoverflow.com/questions/1548704/delete-multiple-lines-in-a-file-python
    """
    def __init__(self, filename, handler, sleep=0.1):
        self._cached_stamp = 0
        self.filename = filename
        self.sleep = sleep
        self.handler = handler

    def ook(self):
        sleep(self.sleep)
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            try:
                self.handler()
            except Exception as e:
                print(e)

def handler():
    app.main()
    reload(app)

watch = Watch('app.py', handler)

while True:
    watch.ook()
    