import boto3
import botocore

# Define the S3 Bucket Name
BUCKET_NAME = 'p3na-18gus.3101.027'
# Path within the S3 bucket to folder we desire
PATH = 'video-files/'
SAVE_PATH = 'downloaded-files/'
# File name we wish to download
file_name = 'Recfile P3 Edge 20181121 082855 Webcam Logitech Forward Outputiplimage.m4v'
KEY = PATH + file_name

# Establish the AWS client connection using access keys.
# Select the correct AWS resource
s3 = boto3.resource('s3',
                    aws_access_key_id='AKIAJJKVLCJ47OTT7FYQ',
                    aws_secret_access_key='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',
                    region_name='us-east-1'
                    )

# Download file from S3 bucket, and store at local location 'file_name'.
try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, SAVE_PATH + file_name)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise