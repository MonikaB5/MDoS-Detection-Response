import boto3

def lambda_handler(event, context):
    print("M-DoS ALERT TRIGGERED!")
    print("Initiating automated response...")
    return {
        "statusCode": 200,
        "body": "Defence Initiated"
    }
