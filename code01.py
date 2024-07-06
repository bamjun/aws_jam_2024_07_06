# I'll simulate the AWS CLI commands to fetch and display the tags for the 'roast-function' Lambda function.
import boto3

# Initialize a session using Amazon Lambda
client = boto3.client('lambda')

# Get the tags for the specified Lambda function
response = client.list_tags(
    Resource='arn:aws:lambda:ap-northeast-2:254510235751:function:roast-function'
)

response['Tags']
