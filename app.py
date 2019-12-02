import sys
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from flask import Flask



class MyEventHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        app.fib_number = get_fib_number()
        print('Handling event: fib_number is now %s' % app.fib_number)


def get_fib_number():
    with open('to_watch/number.txt') as f:
        return int(f.read().strip())


def fib(number):
    sequence = [0, 1]
    while sequence[-1] < number:
        sequence.append(sequence[-2] + sequence[-1])
    return sequence


def launch_watch_thread():
    thread = threading.Thread(target=start_watch)
    thread.run()


def start_watch():
    path = '/home/sergey/0dev/galaxy/watcher_debug/to_watch'
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()


app = Flask(__name__)
app.fib_number = get_fib_number()
start_watch()


@app.route("/", methods=['GET'])
def get_content():
    return '%s<p>%s' % (app.fib_number, fib(app.fib_number)), 200
