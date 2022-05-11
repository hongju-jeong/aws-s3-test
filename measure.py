from datetime import datetime, timedelta

import boto3

s3r = boto3.resource('s3')
s3 = boto3.client('s3')
file_name = "10mb.txt"

avg_latency = {}
for bucket in s3r.buckets.all():
    print(bucket.name)
    avg_latency[bucket.name] = 0


def upload_latency(s3, bucket_name, file_name):
    with open(file_name, "rb") as f:
        timer1 = datetime.now()
        s3.upload_fileobj(f, bucket_name,file_name)
        timer2 = datetime.now()
    return (timer2 - timer1).total_seconds()

def download_latency(s3, bucket_name, file_name):
    with open('downloads/'+file_name, "wb") as f:
        timer1 = datetime.now()
        s3.download_fileobj(bucket_name,file_name,f)
        timer2 = datetime.now()
    return (timer2 - timer1).total_seconds()

def delete_latency(s3, bucket_name, file_name):
    timer1 = datetime.now()
    s3.delete_object(Bucket=bucket_name, Key = file_name)
    timer2 = datetime.now()
    return (timer2 - timer1).total_seconds()


# print("upload")
# for i in range(10):
#     print("step ",i+1)
#     for bucket in s3r.buckets.all():
#         bucket_name = bucket.name
#         latency = upload_latency(s3, bucket.name, file_name)
#         avg_latency[bucket_name] += latency
#         print(bucket_name,": ", str(latency))
        
# for bucket in avg_latency:
#     print(bucket, "'s avg: ", str(avg_latency[bucket] / 10))

# print("download")
# for i in range(10):
#     print("step ",i+1)
#     for bucket in s3r.buckets.all():
#         bucket_name = bucket.name
#         latency = download_latency(s3, bucket.name, file_name)
#         avg_latency[bucket_name] += latency
#         print(bucket_name,": ", str(latency))
        
# for bucket in avg_latency:
#     print(bucket, "'s avg: ", str(avg_latency[bucket] / 10))

print("delete")
for i in range(10):
    print("step ",i+1)
    for bucket in s3r.buckets.all():
        bucket_name = bucket.name
        latency = delete_latency(s3, bucket.name, file_name)
        avg_latency[bucket_name] += latency
        print(bucket_name,": ", str(latency))
        
for bucket in avg_latency:
    print(bucket, "'s avg: ", str(avg_latency[bucket] / 10))