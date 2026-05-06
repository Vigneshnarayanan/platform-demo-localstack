import os
from flask import Flask, jsonify
import boto3

app = Flask(__name__)

AWS_ENDPOINT = os.environ.get('AWS_ENDPOINT_URL', 'http://localhost:4566')
BUCKET = os.environ.get('BUCKET_NAME', 'platform-demo-bucket')

s3 = boto3.client('s3', endpoint_url=AWS_ENDPOINT, aws_access_key_id='test', aws_secret_access_key='test')

@app.route('/')
def index():
    return jsonify({'message': 'Platform Demo app running', 'bucket': BUCKET})

@app.route('/put')
def put():
    s3.put_object(Bucket=BUCKET, Key='hello.txt', Body=b'hello from local')
    return jsonify({'status': 'ok'})

@app.route('/get')
def get():
    obj = s3.get_object(Bucket=BUCKET, Key='hello.txt')
    body = obj['Body'].read().decode('utf-8')
    return jsonify({'body': body})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
