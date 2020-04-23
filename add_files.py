import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import time
import send2trash
import sqlite3

r'C:\Users\akush\Desktop\Programming\Personal Projects\Safe_sql'

def on_any_event(event):
    conn1 = sqlite3.connect(r'C:\Users\akush\Desktop\Programming\Personal Projects\Safe_sql\safe.sqlite')
    cur = conn1.cursor()
    for filename in os.listdir(path):
        filename.strip()
        abs = os.path.join(path, filename)
        name,ext = os.path.splitext(filename)
        name = name.strip()
        ext = ext.strip()
        with open(abs, 'rb') as fhand:
            binary_data = fhand.read()
        file = binary_data
        cur.execute('INSERT OR REPLACE INTO Files (name, ext, file) VALUES (?, ?, ?)',(name, ext, file,))
        send2trash.send2trash(abs)
    conn1.commit()


conn = sqlite3.connect(r'C:\Users\akush\Desktop\Programming\Personal Projects\Safe_sql\safe.sqlite')

cur1 = conn.cursor()
cur1.executescript('''Create table if not exists Files (name TEXT, ext TEXT, file BLOB NOT NULL UNIQUE)''')
cur1.close()

patterns = "*"
ignore_patterns = ""
case_sensitive = False
ignore_directories = False
my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

my_event_handler.on_any_event = on_any_event

path = r"C:\Users\akush\Desktop\Safe"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive = go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
