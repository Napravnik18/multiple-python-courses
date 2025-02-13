import boto3

client = boto3.client('s3')
client.create_bucket(Bucket='stan-compasso-boto3-criars3-teste')

with open('myfile.txt', 'w') as file:
    file.write('Test file for upload')
    
client.upload_file(Filename='myfile.txt',
                   Bucket='stan-compasso-boto3-criars3-teste',
                   Key='test-upload-file')

client.download_file(Bucket='stan-compasso-boto3-criars3-teste',
                     Key='test-upload-file',
                     Filename= 'my_local.txt')

with open('my_local.txt', 'r') as f:
    print(f.read())
    
client.delete_object(Bucket='stan-compasso-boto3-criars3-teste',
                     Key='test-upload-file')