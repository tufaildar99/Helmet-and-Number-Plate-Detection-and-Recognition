from bucket import Bucket

bucket = Bucket()
try:
    bucket.upload_blob('test.txt', 'test.txt')
    bucket.download_blob('test.txt', 'test.txt')
    bucket.list_blobs()
except Exception as e:
    print(e)

