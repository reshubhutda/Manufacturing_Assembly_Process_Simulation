from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from aws_uploader import upload_file
import time
import logging

logger = logging.getLogger(__name__)

class SensorFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            if event.src_path.endswith(".csv"):
                logger.info(f"New File Detected: {event.src_path}")
                upload_file(event.src_path)
            else:
                logger.warning(f"Unsupported file: {event.src_path}")

def watch_folder(folder_path):
    event_handler = SensorFileHandler()
    observer = Observer()
    try:
        observer.schedule(event_handler, folder_path, recursive=False)
        observer.start()
        logger.info(f"Monitoring folder: {folder_path}")

    except FileNotFoundError as e:
        logger.warning(f"File Not Found: {e}")
        return
    except PermissionError as e:
        logger.warning(f"Permission Denied: {e}")
        return
    
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("Stopping file watcher")
        observer.stop()

    observer.join()
    logger.info("File watcher stopped")