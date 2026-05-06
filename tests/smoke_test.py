import os
import boto3

endpoint = os.environ.get('AWS_ENDPOINT_URL', 'http://localhost:4566')
bucket = os.environ.get('BUCKET_NAME', 'platform-demo-bucket')

s3 = boto3.client('s3', endpoint_url=endpoint, aws_access_key_id='test', aws_secret_access_key='test')

print('Creating bucket:', bucket)
try:
    s3.create_bucket(Bucket=bucket)
except Exception as e:
    print('Bucket create may have failed or already exists:', e)

print('Putting object...')
s3.put_object(Bucket=bucket, Key='smoke.txt', Body=b'smoke test')
obj = s3.get_object(Bucket=bucket, Key='smoke.txt')
body = obj['Body'].read().decode('utf-8')
print('Got object body:', body)
assert body == 'smoke test'
print('Smoke test passed')
