from aws_uploader import upload_file
from file_watcher import watch_folder
import logging

folder_path = r"C:\Users\reshu\Downloads\MES"

logging = logging.basicConfig(
    level=logging.INFO, 
    format="%{asctime}s - %{levelname}s - %{name}s - %{message}s",
    handlers= [logging.FileHandler("pipeline.log"), logging.SteamHandler()]
)

def main():
    watch_folder(folder_path)

if __name__ == "__main__":
    main()
