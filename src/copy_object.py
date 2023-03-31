import configparser
from datetime import datetime, timezone
from minio import Minio
from minio.commonconfig import CopySource, REPLACE
from minio.error import MinioException

config = configparser.ConfigParser()
config.read('credentials.ini')

# Set the credentials with credentials.ini #

URL_API = config['minio']['url_api']
ACCES_KEY = config['minio']['acces_key']
SECRET_KEY = config['minio']['secret_key']
SECURE = config['minio']['secret']

client = Minio(
    URL_API,
    access_key=ACCES_KEY,
    secret_key=SECRET_KEY,
    secure=SECURE
)

# copy an object with condition.
try:
    result = client.copy_object(
        "my-bucket",
        "my-object",
        CopySource(
            "my-sourcebucket",
            "my-sourceobject",
            modified_since=datetime(2023, 1, 30, tzinfo=timezone.utc),
        ),
    )
    print(result.object_name, result.version_id)

except MinioException as err:
    print(err)

# Set the metadata
metadata = {"test_meta_key": "test_meta_value"}

# copy object with metadata
try:
    copy_result = client.copy_object("my-bucket",
                                     "my-object",
                                     "/my-sourcebucket/my-sourceobject",
                                     metadata=metadata,
                                     metadata_directive=REPLACE
                                     )
    print(result.object_name, result.version_id)
except MinioException as e:
    print(e)
