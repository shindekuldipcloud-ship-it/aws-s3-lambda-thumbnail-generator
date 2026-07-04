import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # 1. Get the bucket name and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    image_name = event['Records'][0]['s3']['object']['key']
    
    # 2. Define the destination bucket
    destination_bucket = 'thumbnali-photos' 
    
    print(f"Source bucket: {source_bucket}, Image: {image_name}")
    
    try:
        # 3. Copy the object to the destination bucket
        s3_client.copy_object(
            Bucket=destination_bucket,
            Key=f"thumbnail-{image_name}",
            CopySource={'Bucket': source_bucket, 'Key': image_name}
        )
        print(f"Successfully copied to {destination_bucket}")
        
    except Exception as e:
        print(f"Error: {e}")
        raise e
