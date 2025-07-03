import boto3

s3 = boto3.resource('s3')

buckets = list(s3.buckets.all())

if not buckets:
    print('There are no buckets')
else:
    for bucket in buckets:
        print(bucket.name)
