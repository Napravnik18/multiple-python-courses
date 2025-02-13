import boto3

s3 = boto3.client('s3')

bucket_name = 'stan-compasso-boto3-criars3-teste'

paginator = s3.get_paginator('list_objects_v2')
results = paginator.paginate(Bucket=bucket_name)

for item in results.search('Contents'):
    print(item['Key'])
    
