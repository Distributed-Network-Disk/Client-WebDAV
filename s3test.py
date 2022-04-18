import botocore

import boto3

aws_access_key_id = 'totorominio'
aws_secret_access_key = 'totorominio123'

session = boto3.Session(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# 连接到minio
s3 = session.resource('s3', endpoint_url='http://206.yyw.moe:9000/')

# 查看所有bucket
for bucket in s3.buckets.all():
    print('bucket name:%s' % bucket.name)

# 新建一个bucket(bucket name 中不能有_下划线)
# s3.create_bucket(Bucket='mybucket')

# 查看一个bucket下的所有object
bucket_name = 'mybucket'
bucket = s3.Bucket(bucket_name)
for obj in bucket.objects.all():
    print('obj name:%s' % obj.key)

# 删除bucket(只能删除空的bucket)
#try:
#    bucket.delete()
#except botocore.exceptions.ClientError as e:
#    print('bucket is not empty')

obj_name = 'test.md'
local_file = 's3test.py'
# 上传文件
s3.Object(bucket_name, obj_name).upload_file(local_file)
# 或
# bucket.put_object(Key=obj_name, Body=open(local_file, 'rb'))

local_file = 'README.md'
# 下载文件
s3.Object(bucket_name, obj_name).download_file(local_file)

# download to bytes
s3.Object(bucket_name, obj_name).get()['Body'].read() #.decode('utf-8')

# 删除bucket下所有object
#bucket.objects.filter().delete()

# 删除bucket下某个object
#bucket.objects.filter(Prefix=obj_name).delete()

