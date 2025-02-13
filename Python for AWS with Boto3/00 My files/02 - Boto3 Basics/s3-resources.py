import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket(name='stan-compasso-boto3-criars3-teste')

with open('myfile.txt', 'w') as file:
    file.write('Test file for upload')
    
    
bucket.upload_file(Filename='myfile.txt', Key='another-upload')
print(list(bucket.objects.all()))

bucket.download_file(Filename='new_download.txt', Key='another-upload')

with open('new_download.txt', 'r') as f:
    print(f.read())
    
print(list(bucket.objects.filter(Prefix='another')))