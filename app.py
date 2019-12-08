import os
import sys
import time
import threading
from uwsgidecorators import postfork
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

print('\tXXXXX top; pid=%d' % os.getpid())


def app(env, start_response):
    print('\tXXXXX app(); pid=%d' % os.getpid())
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World, " + str(FOO)]

class MyFileSystemEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print('\tHANDLE event; pid=%d' % os.getpid())
        my_number = get_number()
        FOO = my_number
        #print('Handling event: my_number is now %s\n' % my_number)

def get_number():
    with open('to_watch/number.txt') as f:
        return int(f.read().strip())

@postfork
def launch_postfork():
#    launch_thread_watcher()
    print('\tXXXXX launching postfork pid=%d' % os.getpid())
    path = '/home/sergey/0dev/galaxy/watcher_debug/to_watch'
    event_handler = MyFileSystemEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()





#def launch_thread_watcher():
#    print('\tXXXXX launch_thread_watcher(); pid=%d' % os.getpid())
#    thread = threading.Thread(target=watch)
#    thread.start()
#
#def watch():
#    #path = '/Users/sergey/0dev/watcher_debug/app2/to_watch'
#    path = '/home/sergey/0dev/galaxy/watcher_debug/to_watch'
#    event_handler = MyFileSystemEventHandler()
#    observer = Observer()
#    observer.schedule(event_handler, path, recursive=True)
#    observer.start()



#def launch_thread_clock():
#    print('\tXXXXX launch_thread_clock(); pid=%d' % os.getpid())
#    thread = threading.Thread(target=clock)
#    thread.start()
#
#def clock():
#    while True:
#        print('\tXXXXX clock: %s, pid=%d' % (time.ctime(), os.getpid()))
#        time.sleep(1)




#@postfork
#def reload():
#    start_watch()
#    print('reloading after forking')
#    print('new5', os.getpid())
#    #app.fib_number = get_fib_number()
#
#
#class MyEventHandler(FileSystemEventHandler):
#
#
#    def on_any_event(self, event):
#        print('4', os.getpid())
#        app.fib_number = get_fib_number()
#        print('Handling event: fib_number is now %s' % app.fib_number)
#
#
#def get_fib_number():
#    with open('to_watch/number.txt') as f:
#        return int(f.read().strip())
#
#
#def fib(number):
#    sequence = [0, 1]
#    while sequence[-1] < number:
#        sequence.append(sequence[-2] + sequence[-1])
#    return sequence
#
#
#def launch_watch_thread():
#    print('3', os.getpid())
#    thread = threading.Thread(target=start_watch)
#    thread.run()
#
#
#def start_watch():
#    print('new2', os.getpid())
#    path = '/Users/sergey/0dev/watcher_debug/to_watch'
#    event_handler = MyEventHandler()
#    observer = Observer()
#    observer.schedule(event_handler, path, recursive=True)
#    observer.start()
#
#
#app = Flask(__name__)
#app.fib_number = get_fib_number()
#start_watch()
#print('1', os.getpid())
#
#
#@app.route("/", methods=['GET'])
#def get_content():
#    return '%s<p>%s' % (app.fib_number, fib(app.fib_number)), 200
