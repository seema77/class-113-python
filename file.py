import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source="C:/Users/Seema/Downloads"
dest="C:/Users/Seema/Downloads/result"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        
        


event_handler=FileMovementHandler()

observer=Observer()
observer.schedule(event_handler,source,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running.....")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()