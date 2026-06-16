import boto3
from botocore.client import Config

# Replace with your AWS access key, secret key, and region
access_key_id='AKIAJWZ2ZZGXLUNQBHDA'  
secret_access_key='+7aIlRYlsg5NzHyZjSUf+KdNhCxyh30YTOHz7jGqRBRPF4bf8eVpF2NZ7lzCZfZk'
aws_region_name='us-east-1'
bucket_name = 'sit.chats'


file_path = r'Unix\Data\cars.csv'
s3_file_name = r'logs\data.csv'

def main():
    print('start')

    # s3_client = boto3.client(service_name = 's3', region_name = aws_region_name, 
    #                          aws_access_key_id = access_key_id, 
    #                          aws_secret_access_key = secret_access_key)
    s3_client = boto3.client(
    service_name='s3',
    region_name=aws_region_name,
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key)

    s3_client.upload_file(r'C:\Users\rjakkula\Documents\DE2\Data\cars.csv', 'sit.chats', 'logs/data.csv')
    # response = s3_client.upload_file(file_path, bucket_name, s3_file_name)
    #s3_client.upload_file('Unix/Data/cars.csv', 'sit.chats', 'logs/data.csv')
    # print(f'upload file response: {response}')
    print('File uploaded successfully!')
if __name__ == '__main__':
    main()