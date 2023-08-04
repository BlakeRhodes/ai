import sys
import threading
import time


class LoadingIndicator(threading.Thread):
    def __init__(self, message="Loading"):
        super().__init__()
        self.message = message
        self.is_running = True

    def run(self):
        i = 0
        while self.is_running:
            char = '\\*|@/#-%'
            sys.stdout.write(f'\r{self.message} {char[i % len(char)]} ')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

    def stop(self):
        self.is_running = False
        self.join()
        sys.stdout.write('\r         \n\nOk pal, ')
        sys.stdout.flush()
