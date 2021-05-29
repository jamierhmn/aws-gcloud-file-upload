import logging
import boto3,os
from botocore.exceptions import ClientError

    
def upload_file_to_s3(filepath,filename,bucket,secret_key,access_key,acl="public-read"):
    print("upload_file_to_s3=\n",filename)
   
    s3 = boto3.client(
        "s3",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key)    
    try:
                
        with open(filepath, 'rb') as data:
          s3.upload_fileobj(data,bucket,filename)

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Exception: ", e)
        return e
    

    # after upload file to s3 bucket, return filename of the uploaded file. We should write code
    #to receive filepath in AWS S3 and display in UI
    return filename