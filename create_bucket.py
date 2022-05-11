import boto3
import json

with open('config.json', 'r') as f:
    json_data = json.load(f)

s3 = boto3.resource('s3')

locations = json_data.get('location')

for location in locations:
    
    if(location == 'us-east-1'):
        print(location)
        continue
    else : s3.create_bucket(Bucket='hongju-'+location, CreateBucketConfiguration={'LocationConstraint': location})



