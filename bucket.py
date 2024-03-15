# create a python module to upload and get files from google cloud storage

import os
from google.cloud import storage

class Bucket:
    def __init__(self):
        self.storage_client = storage.Client()
        self.bucket_name = 'violations_proof'
        self.bucket = self.storage_client.get_bucket(self.bucket_name)

    def upload_blob(self, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        print('Uploading file to bucket')
        blob = self.bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(
            "File {} uploaded to {}.".format(
                source_file_name, destination_blob_name
            )
        )

    def get_bucket(self):
        """Gets the bucket."""
        return self.bucket

    def get_public_url(self, blob_name):
        """Gets the public url of the file."""
        blob = self.bucket.blob(blob_name)
        return blob.public_url
    