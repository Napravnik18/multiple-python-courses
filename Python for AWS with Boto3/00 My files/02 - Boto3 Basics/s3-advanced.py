import boto3

client = boto3.client('s3')
s3 = boto3.resource('s3')
'''
encryption = client.get_bucket_encryption(Bucket='stan-compasso-boto3-criars3-teste')
url = client.generate_presigned_url(ClientMethod='get_object',
                                    Params={'Bucket':'stan-compasso-boto3-criars3-teste',
                                            'Key':'another-upload'},
                                    ExpiresIn=120)

bucket = s3.Bucket('stan-compasso-boto3-criars3-teste')
bucket.objects.all().delete()
#print(url)
#print(encryption)
'''
client.delete_bucket(Bucket='compassotestetesteteste')