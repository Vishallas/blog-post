import boto3
from os import environ
import botocore
import uuid

try:
    S3_BUCKET = "public-post-files-presidio"
    # REGION_NAME=environ.get("AWS_REGION_DEFAULT")
    DYNAMODB_TABLE = "Post"
except Exception as e:
    print(e)

dynamodb = boto3.resource('dynamodb', "us-east-1")

# Select the DynamoDB table
table = dynamodb.Table(DYNAMODB_TABLE)

def get_all_posts():
    response = table.scan()
    data = response.get('Items', None)
    # Fetch more data if there are more pages of data
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    return data

def put_post(request):
    # print(request.form, request.files)
    try:
        title = request.form['title']
        content = request.form['content']
        fileb = request.files['image']
    except:
        print("Insufficient form-data")
        return {'StatusCode':400}
    
    try:
        # Upload file to S3
        s3 = boto3.client('s3')
        file_key = str(uuid.uuid4())
        s3.upload_fileobj(fileb, S3_BUCKET, file_key)
        # Get object URL
        object_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{file_key}"        

    except botocore.exceptions.ClientError as e:
        error_message = f"Failed to upload file to S3: {str(e)}"
        print(error_message+" s3 errro")
        return {'StatusCode':500}
    try:
        table.put_item(
            Item={
                "title":title,
                "content": content,
                "imageurl":object_url,
                "postid":str(uuid.uuid4())
            }
        )
        return {'StatusCode':200}
    except Exception as e:
        print(e)
        return {'StatusCode':500}