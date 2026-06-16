# test2.py

import boto3

def upload_to_s3(local_file, bucket, s3_key, aws_access_key_id, aws_secret_access_key, region_name):
    s3_client = boto3.client(
        's3',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    s3_client.upload_file(local_file, bucket, s3_key)
    print(f"Uploaded {local_file} to s3://{bucket}/{s3_key}")

if __name__ == "__main__":
    print("Hello from test2.py!")
    # Example usage
    local_file = r"Unix/Data/cars.csv"
    bucket = "sit.chats"
    s3_key = "logs/data.csv"
    aws_access_key_id = "AKIAJWZ2ZZGXLUNQBHDA"
    aws_secret_access_key = '+7aIlRYlsg5NzHyZjSUf+KdNhCxyh30YTOHz7jGqRBRPF4bf8eVpF2NZ7lzCZfZk'
    region_name = "us-east-1"
    upload_to_s3(local_file, bucket, s3_key, aws_access_key_id, aws_secret_access_key, region_name)

