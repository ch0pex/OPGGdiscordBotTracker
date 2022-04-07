import os
from google.cloud import storage


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'smart-mark-346320-1a104a43c039.json'
storage_client = storage.Client()


bucket_name = 'photo_loltracker'
bucket = storage_client.bucket(bucket_name)

def upload_to_bucket(blob_name,file_path,bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_file_name(file_path)
        return True

    except:
        print('Error uploading to bucket')
        return False
