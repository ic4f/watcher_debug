import os
import threading
from uwsgidecorators import postfork
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


CONTENT = ['nothing']


def app(env, start_response):
    print('\t=========== app(); pid=%d' % os.getpid())
#    launch_thread_watcher()

    start_response('200 OK', [('Content-Type','text/html')])
    return CONTENT[0].encode('utf-8')

@postfork
def launch_thread_watcher():
    print('\t=========== launch_thread_watcher(); pid=%d' % os.getpid())
    thread = threading.Thread(target=watch)
    thread.start()

def watch():
    path = '/home/sergey/0dev/galaxy/watcher_debug/to_watch'
    event_handler = MyFileSystemEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()


class MyFileSystemEventHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print('\t=========== handling event; pid=%d' % os.getpid())
        CONTENT[0] = self.get_content()

    def get_content(self):
        with open('to_watch/content.txt') as f:
            return f.read().strip()
    
