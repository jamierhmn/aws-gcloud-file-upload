from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

def Gcloud_upload_file(filename):

    # Setting credentials using the downloaded JSON file

    client = storage.Client.from_service_account_json(json_credentials_path='gcloud.json')

    # Creating bucket object

    bucket = client.get_bucket('pdf-bucket')

    # Name of the object to be stored in the bucket

    object_name_in_gcs_bucket = bucket.blob(Gcloud_upload_file)


    # Name of the object in local file system

    object_name_in_gcs_bucket.upload_from_filename(Gcloud_upload_file)
    return("File transfer successful")