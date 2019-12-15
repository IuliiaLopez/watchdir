import os
import sys
import time

# Extended version of https://pythonhosted.org/watchdog/quickstart.html#a-simple-example
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Directory we track, and target directory for the files
track_directory = "/Users/julia/Downloads"
target_directory = "/Users/julia/Downloads/moved_files"


class DirectoryHandler(FileSystemEventHandler):
    """
    Event Handler for directory
    """

    def on_modified(self, event):
        """
        On modified content within directory, change path within directory tree (the location of your file)
        """
        for filename in os.listdir(track_directory):
            current_complete_filename = track_directory + "/" + filename
            new_complete_filename = target_directory + "/" + filename
            # odd thing to fix: OSError: [Errno 22] Invalid argument: '/Users/julia/Downloads/moved_files' -> '/Users/julia/Downloads/moved_files/moved_files'
            os.rename(current_complete_filename, new_complete_filename)


def main():
    event_handler = DirectoryHandler()

    observer = Observer()
    observer.schedule(event_handler, track_directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
            print("watching for another 5 sec")
    except (KeyboardInterrupt, SystemExit):
        print("Stopped watching your directory")
        observer.stop()
    observer.join()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
