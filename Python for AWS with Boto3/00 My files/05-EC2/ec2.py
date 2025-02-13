import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')
'''
instance = ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    ImageId= 'ami-0453ec754f44f9a4a',
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
client = boto3.client('ec2')
description = client.describe_instances(InstanceIds=['i-0b01add37905330d6'])
print(description['Reservations'][0]['Instances'][0]['State'])
#client.stop_instances(InstanceIds=['i-0b01add37905330d6'])#stop instance
#client.start_instances(InstanceIds=['i-0b01add37905330d6'])#start insance
client.terminate_instances(InstanceIds=['i-0b01add37905330d6'])#terminate instance