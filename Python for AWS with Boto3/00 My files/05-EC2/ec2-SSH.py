import boto3
import paramiko

client = boto3.client('ec2')
'''
key_pair = client.create_key_pair(KeyName='boto3-keypair')
private_key = key_pair['KeyMaterial']
with open('my-key-pair.pem', 'w') as f:
    f.write(private_key)
'''
#security_groups = client.describe_security_groups()
#print(security_groups['SecurityGroups'])
'''
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    ImageId= 'ami-0453ec754f44f9a4a',
    KeyName='boto3-keypair',
    SecurityGroupIds=['sg-0a48ead47bcb02b7e'],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Project', 'Value':''},
                {'Key': 'CostCenter', 'Value':''},
                {'Key': 'Name', 'Value':''}
            ]
        },
        {
            'ResourceType': 'volume',
            'Tags': [
                {'Key': 'Project', 'Value':''},
                {'Key': 'CostCenter', 'Value':''},
                {'Key': 'Name', 'Value':''}
            ]
        }
    ]
)
print(f"Instância criada com ID: {instance[0].id}")
'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
private_key = paramiko.RSAKey(filename='my-key-pair.pem')
description = client.describe_instances(InstanceIds=['i-0946bc6ee78aff009'])
ip = description['Reservations'][0]['Instances'][0]['PublicIpAddress']
ssh.connect(hostname=ip, username='ec2-user', pkey=private_key)
