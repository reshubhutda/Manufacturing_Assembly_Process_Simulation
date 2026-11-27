from boto3.exceptions import S3UploadFailedError 
import boto3
from botocore.exceptions import (NoCredentialsError, PartialCredentialsError, EndpointConnectionError, ClientError)
import os
import logging


logger = logging.getLogger(__name__)


def upload_file(file_path):
    bucket_name = "manufacturing-timeseries-data"
    file_name = os.path.basename(file_path)
    try:
        session = boto3.Session(profile_name="s3")
        s3 = session.client("s3")
        s3.upload_file(file_path, bucket_name, f"raw/{file_name}")
        logger.info(f"Successfully uploaded: {file_name}")
        return True

    except S3UploadFailedError as e:
        logger.error(f"Upload Failed: {e}")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")

    except PermissionError as e:
        logger.error(f"File access denied: {e}")

    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"AWS credentials issue: {e}")

    except EndpointConnectionError as e:
        logger.error(f"AWS connection failed: {e}")

    except ClientError as e:
        logger.error(f"AWS service error: {e}")

    return False