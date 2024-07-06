import boto3
import uuid

# Create an S3 client
s3 = boto3.client('s3')

# Generate a unique bucket name
bucket_name = 'aws-jam-bamfjfjf' + str(uuid.uuid4())

# Create the bucket
response = s3.create_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} created successfully.')
