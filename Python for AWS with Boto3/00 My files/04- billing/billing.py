import boto3
from datetime import datetime, timedelta

client = boto3.client('ce')

start_date = (datetime.now()+timedelta(days=1)).strftime('%Y-%m-%d')
end_date = (datetime.now()+timedelta(days=31)).strftime('%Y-%m-%d')

result = client.get_cost_forecast(TimePeriod={
    'Start':start_date,
    'End':end_date
}, Metric='UNBLENDED_COST', Granularity='MONTHLY')

print(result)
'''
start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
end_date = datetime.now().strftime('%Y-%m-%d')
print(start_date)


response = client.get_cost_and_usage(TimePeriod={
            'Start':start_date,
            'End':end_date},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type':'DIMENSION',
                'Key':'SERVICE'
            }
        ])

for item in response['ResultsByTime']:
    print(item['TimePeriod'])
    print('\n')
    for group in item['Groups']:
        service_name = group['Keys'][0]
        cost = group['Metrics']['UnblendedCost']['Amount']
        print(f'{service_name}: ${cost}')
    print('\n\n\n')
'''


'''
response = client.get_cost_and_usage(TimePeriod={
    'Start':start_date,
    'End':end_date
}, Granularity='MONTHLY',Metrics=['UnblendedCost','UsageQuantity'])

for item in response['ResultsByTime']:
    print(item['TimePeriod'])
    print(item['Total']['UnblendedCost'])
    print('\n\n')


response = client.get_dimension_values(TimePeriod={
    'Start':start_date,
    'End':end_date},
     Dimension='SERVICE')

for service in response['DimensionValues']:
    print(service['Value'])

'''