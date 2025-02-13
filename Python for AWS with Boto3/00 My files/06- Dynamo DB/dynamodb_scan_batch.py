import boto3
client = boto3.client('dynamodb',region_name='us-east-1')

movies = [
        {"Title": "The Matrix",
         "Director": "Lana Wachowski",
         "Year": "1999",
         "Rating": "4.7"},
    
        {"Title": "The Matrix 2",
             "Director": "Lana Wachowski",
             "Year": "2003",
             "Rating": "4.6"},

        {"Title": "The Matrix 3",
             "Director": "Lana Wachowski",
             "Year": "2003",
             "Rating": "4.5"},

        {"Title": "Inception",
             "Director": "Christopher Nolan",
             "Year": "2010",
             "Rating": "4.6"},
    
        {"Title": "Saving Private Ryan",
             "Director": "Steven Spielberg",
             "Year": "1999",
             "Rating": "4.7"},

]
'''
batch_request = []

for movie in movies:
    batch_request.append({
        'PutRequest':{
            'Item':{
                'Title': {'S':movie['Title']},
                'Rating':{'N':str(movie['Rating'])},
                'Director':{'S':movie['Director']},
                'Year':{'N':str(movie['Year'])}
            }
        }
    })
response = client.batch_write_item(RequestItems={'Movies':batch_request})

batch_request_2 = {"Keys": []}
for movie in movies:
    batch_request_2["Keys"].append({
            'Title': {'S': movie['Title']},
            'Rating': {'N': str(movie['Rating'])},
        }
    )
response2 = client.batch_get_item(RequestItems={'Movies':batch_request_2})
'''


items = []
response3 = client.scan(TableName='Movies')
items.extend(response3['Items'])

while 'LastEvaluatedKey' in response3.keys():
    response3 = client.scan(TableName='Movies',ExclusiveStartKey=response3['LastEvaluatedKey'])
    items.extend(response3['Items'])

'''
#filter using client    
response4 = client.scan(TableName='Movies',
                        FilterExpression='Rating >= :num',
                        ExpressionAttributeValues={':num':{'N':'4.7'}}) 
print(response4)
'''
#filter using resource
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Movies')
response4 = table.scan(FilterExpression=Attr('Year').gte(2004))
print(response4)