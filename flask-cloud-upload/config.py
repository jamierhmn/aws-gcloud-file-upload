# flask_s3_uploads/config.py

import os

S3_BUCKET                 = os.environ.get("S3_BUCKET_NAME")
S3_KEY                    = os.environ.get("S3_KEY_NAME")
S3_SECRET                 = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION               = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
SECRET_KEY                = os.urandom(32)
DEBUG                     = True
PORT                      = 5000
ALLOWED_EXTENSIONS_IMG_MEDIA = {'jpg', 'png', 'svg','webp','mp3', 'mp4', 'mpeg4', 'wmv', '3gp','webm'}

ALLOWED_EXTENSIONS_DOC = {'doc','docx','csv','pdf'}