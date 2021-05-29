import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("S3_KEY")
print(SECRET_KEY )