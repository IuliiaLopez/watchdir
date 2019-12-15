from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler

import os, json, time

source_directory = "~/Downloads"
target_directory = "~/Downloads/moved_files"


class DirectoryHandler(FileSystemEventHandler):
    '''
    Event Handler for directory
    '''
    
    def on_modified(self, event):
        '''
        On modified content within directory, change path within directory tree (the location of your file)
        '''
        for filename in os.listdir(directory):
            current_location =  
            new_location += "/" + filename
            os.rename (src, new_target)


event_handler = DirectoryHandler()
observer = Observer()
observer.shedule(event_handler, source_directory, recursive=True)

try:
    while True:
        # scan every ten seconds the directory for changes
        sleep(10)
 
