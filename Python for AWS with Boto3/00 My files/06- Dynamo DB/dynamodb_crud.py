import boto3
client = boto3.client('dynamodb',region_name='us-east-1')

'''
table_name= 'Movies'

attributes = [
    {
        'AttributeName':'Title',
        'AttributeType':'S'
    },
    {
        'AttributeName':'Rating',
        'AttributeType':'N'
    }
]
key_schema = [
    {
        'AttributeName':'Title',
        'KeyType':'HASH'
    },
    {
        'AttributeName':'Rating',
        'KeyType':'RANGE'
    }
]

provisioned_throughput = {
    'ReadCapacityUnits':5,
    'WriteCapacityUnits':5
}
response = client.create_table(TableName=table_name,
                               AttributeDefinitions=attributes,
                               KeySchema=key_schema,
                               ProvisionedThroughput=provisioned_throughput)
'''

'''
entry = {'Title':{'S': 'The Matrix'},
         'Director':{'S':'Wachowski bros'},
         'Year':{'N':'1999'},
         'Rating':{'N':'5'}
         }
client.put_item(TableName='Movies', Item=entry)
'''
'''
#hard to understand, look for documentation
update = 'SET Director = :r'
client.update_item(TableName='Movies',
                   Key=item_key,
                   UpdateExpression=update,
                   ExpressionAttributeValues={':r':{'S':'Wachowski sis'}})
'''
item_key = {'Title':{'S': 'The Matrix'},
            'Rating':{'N':'5'}
         }

client.delete_item(TableName='Movies', Key=item_key)
response = client.get_item(TableName='Movies', Key=item_key)