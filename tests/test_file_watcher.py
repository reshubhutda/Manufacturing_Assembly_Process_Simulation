from unittest.mock import patch, MagicMock
from watchdog.events import FileCreatedEvent, DirCreatedEvent
from file_watcher import SensorFileHandler

def test_csv_file():
    with patch("file_watcher.upload_file") as mock_upload:
        handler = SensorFileHandler()
        event = FileCreatedEvent("sensor.csv")
        handler.on_created(event)
        mock_upload.assert_called_once_with("sensor.csv")


def test_unsupported_file():
    with patch("file_watcher.upload_file") as mock_upload:
        handler = SensorFileHandler()
        event = FileCreatedEvent("sensor.txt")
        handler.on_created(event)
        mock_upload.assert_not_called()


def test_directory():
    with patch("file_watcher.upload_file") as mock_upload:
        handler = SensorFileHandler()
        event = DirCreatedEvent("new_folder")
        handler.on_created(event)