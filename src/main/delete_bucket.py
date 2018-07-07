import boto3
session = boto3.Session()
s3 = session.resource('s3')
bucket = s3.Bucket('squilup-batch4-samath-1')
bucket.object_versions.all().delete()