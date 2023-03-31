from minio import Minio
import configparser

config = configparser.ConfigParser()
config.read('credentials.ini')

# Set the credentials with credentials.ini ####
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
buckets = client.list_buckets()

for bucket in buckets:

    print(bucket.name, bucket.creation_date)


# List all object paths in bucket that begin with my-prefixname.
if client.bucket_exists("my-bucketname"):
    objects = client.list_objects('my-bucketname',
                                  prefix='my-prefixname',
                                  recursive=True)
    for obj in objects:
        print(obj.bucket_name,
              obj.object_name.encode('utf-8'),
              obj.last_modified,
              obj.etag, obj.size,
              obj.content_type)
else:
    print("my-bucket does not exist")
