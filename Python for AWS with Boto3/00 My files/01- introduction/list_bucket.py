import boto3

# Inicializar o cliente do S3
s3 = boto3.client('s3')

try:
    response = s3.list_buckets()
    print("Buckets disponíveis:")
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")
except Exception as e:
    print("Erro:", e)
    