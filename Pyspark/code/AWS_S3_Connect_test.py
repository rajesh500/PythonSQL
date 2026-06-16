import boto3
from botocore.client import Config

# Replace with your AWS access key, secret key, and region
access_key_id='AKIAJWZ2ZZGXLUNQBHDA'  
secret_access_key='+7aIlRYlsg5NzHyZjSUf+KdNhCxyh30YTOHz7jGqRBRPF4bf8eVpF2NZ7lzCZfZk'
aws_region_name='us-east-1'
bucket_name = 'sit.chats'

## s3://sit.chats/Reports/Canned/

file_name = "example.txt"
object_name = 'Reports/Canned/example.txt'
with open(file_name, "w") as f:
    f.write("This is the first line of data.")

def main():
    print('start')
    s3_client = boto3.client(
    service_name='s3',
    region_name=aws_region_name,
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key)
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print('File uploaded successfully!')
    except Exception as e:
        print(f"upload failed: {e}")


if __name__ == '__main__':
    main()