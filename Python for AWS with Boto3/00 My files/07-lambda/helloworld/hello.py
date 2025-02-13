import json
import boto3
import zipfile
import io
from lambda_stan import function_code


iam_client = boto3.client('iam', region_name='us-east-1')
lambda_client = boto3.client('lambda',region_name='us-east-1')

def lambda_handler(event, context):
    return 'Hello World'

function_name = 'HelloWorld'
runtime = 'python3.8'
handler = 'lambda_function.lam'

lambda_execution_policy = {
    'Version':'2012-10-17',
    'Statement':[
        {'Effect':'Allow',
         'Action':[
             'logs:CreateLogGroup',
             'logs:CreateLogsStream',
             'logs:PutLogEvents'
         ],
         'Resource':'arn:aws:logs:*:*:*'
         },
    ]}
role_name = 'LambdaExecutionRole'
'''
role_response = iam_client.create_role(RoleName=role_name,
                                       AssumeRolePolicyDocument=json.dumps(
                                       {'Version':'2012-10-17',
                                        'Statement':[
                                            {'Effect':"Allow",
                                             "Principal":{'Service':"lambda.amazonaws.com"},
                                             'Action':'sts:AssumeRole'}
                                        ]}    
                                       ))
'''

#conseguir arn
response = iam_client.get_role(RoleName=role_name) 
role_arn = response['Role']['Arn']
print(f"The arn role {role_name} is: {role_arn}")

policy_name = 'LambdaExecutionPolicy'
iam_client.put_role_policy(RoleName=role_name,PolicyName=policy_name, 
                           PolicyDocument=json.dumps(lambda_execution_policy))
'''
with io.BytesIO() as deployment_package:
    with zipfile.ZipFile(deployment_package,'w') as zipf:
        zipf.writestr('lambda_function.py',function_code)
        
    create_function_response = lambda_client.create_function(
        FunctionName = function_name,
        Runtime = runtime,
        Role = role_arn,
        Handler = handler,
        Code={'ZipFile':deployment_package.getvalue()}
    )
'''    

lambda_client.delete_function(FunctionName=function_name)