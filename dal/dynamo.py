# This file is part of the DAL (Data Access Layer) for the Print Jobs Starter Project.
# It provides functions to interact with the DynamoDB database for managing print jobs, partners, and citations.


# Project imports ------------------------------------------------------
from models.models import PrintJob, Partner, Citation, PrintJobCitationLink
import boto3


# Set up the database connection --------------------------------------
# Create a DynamoDB resource
table = None
dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
# Create the table if it doesn't exist
table_name = 'print_jobs'
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}  # Partition key
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'N'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
except dynamodb.meta.client.exceptions.ResourceInUseException:  # If the table already exists, we catch the exception
    table = dynamodb.Table(table_name)          
# --------------------------------------------------------------------- 


def create_print_job(print_job: PrintJob) -> PrintJob:
    # Convert PrintJob to a dictionary for DynamoDB
    print_job_dict = print_job.model_dump()
    # Put the item into the DynamoDB table
    table.put_item(Item=print_job_dict)   
    return print_job


def get_all_print_jobs() -> list[PrintJob]:
    # Scan the DynamoDB table to get all print jobs
    response = table.scan()
    print_jobs = []
    for item in response.get('Items', []):
        # Convert each item back to a PrintJob model
        print_job = PrintJob.model_validate(item)
        print_jobs.append(print_job)
    # Handle pagination if there are more items
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        for item in response.get('Items', []):
            print_job = PrintJob.model_validate(item)
            print_jobs.append(print_job)
    # Return the list of print jobs
    if not print_jobs:  # If no print jobs found, return an empty list
        return []
    return print_jobs


def get_print_job(print_job_id: int) -> PrintJob | None:
    # Get a specific print job by its ID
    response = table.get_item(Key={'id': print_job_id})
    if 'Item' not in response:
        raise ValueError(f"Print job with id {print_job_id} not found")
    # Convert the item back to a PrintJob model
    print_job = PrintJob.model_validate(response['Item'])
    return print_job



# --------------------------------------------------------------------- 
# TODO: Add the following routes for print job management starter project 

# Get all print jobs by partner id (need partner id)

# Update print job (need print job id)

# Add citation to print job (need citation id and print job id)

# Get print job citations by print job id (need print job id)

# Remove citation from print job (need citation id and print job id)
# --------------------------------------------------------------------- 

