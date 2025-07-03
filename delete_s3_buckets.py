import boto3

s3=boto3.client('s3',region_name='us-east-1')

s3.delete_bucket(
    Bucket='hey-zoro-here'
)