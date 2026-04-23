import boto3
import uuid
from flask import Flask, request
import os

AWSKEY=os.environ.get('AWS_ACCESS_KEY_ID')
AWSSECRET=os.environ.get('AWS_SECRET_ACCESS_KEY')
PUBLIC_BUCKET='dv19500n-instantgram'
STORAGE_URL='https://s3.amazonaws.com/'+PUBLIC_BUCKET+'/'

def get_public_bucket():
    s3=boto3.resource(service_name='s3',
                        region_name='us-east-1',
                        aws_access_key_id=AWSKEY,
                        aws_secret_access_key=AWSSECRET)
    bucket= s3.Bucket(PUBLIC_BUCKET)
    return bucket

def get_table(name):
    dbclient= boto3.resource(service_name='dynamodb',
                            region_name='us-east-1',
                            aws_access_key_id=AWSKEY,
                            aws_secret_access_key=AWSSECRET)
    return dbclient.Table(name)


def upload_picture():
    bucket = get_public_bucket()
    file= request.files["file"]
    caption= request.form.get("caption",'')
    filename=file.filename
    ct='image/jpeg'
    if filename.endswith('.png'):
        ct='image/png'
    unique_filename=str(uuid.uuid4())+'_'+filename
    bucket.upload_fileobj(file,unique_filename, ExtraArgs={'ContentType':ct})
    url=STORAGE_URL+unique_filename
    PictureID= str(uuid.uuid4())
    picture={
        'PictureID':PictureID,
        'ImageName':url,
        'Caption':caption,
        'FIleName':unique_filename
    }
    table=get_table('PictureInfo')
    table.put_item(Item=picture)
    return {'resullts':'OK'}

def list_pictures():
    table=get_table('PictureInfo')
    results=[]
    for item in table.scan()['Items']:
        results.append(item)
    return results