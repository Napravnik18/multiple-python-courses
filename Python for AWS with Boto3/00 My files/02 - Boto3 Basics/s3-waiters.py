import boto3

s3 = boto3.client('s3')

bucket_name = 'stan-compasso-boto3-criars3-teste-waiter'

waiter = s3.get_waiter('bucket_exists')
wait_config = {'Delay':10,'MaxAttempts':40}

print(f'WAITING FOR THE BUCKET: {'bucket_name'}')
waiter.wait(Bucket=bucket_name, WaiterConfig=wait_config)
print('THE BUCKET HAS BEEN MADE')