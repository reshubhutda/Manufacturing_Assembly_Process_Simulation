from unittest.mock import MagicMock, patch
from boto3.exceptions import S3UploadFailedError
from aws_uploader import upload_file

def test_upload_success():
    with patch("aws_uploader.boto3.Session") as mock_session:
        mock_s3 = mock_session.return_value.client.return_value
        result = upload_file("sensor.csv")
        assert result is True
        mock_s3.upload_file.assert_called_once_with(
            "sensor.csv",
            "manufacturing-timeseries-data",
            "raw/sensor.csv"
        )   


def test_upload_failure():
    with patch("aws_uploader.boto3.Session") as mock_session:
        mock_s3 = mock_session.return_value.client.return_value
        mock_s3.upload_file.side_effect = S3UploadFailedError(
            "Upload failed"
        )
        result = upload_file("sensor.csv")
        assert result is False