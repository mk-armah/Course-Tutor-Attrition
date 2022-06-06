"""
Engineer: Michael Kofi Armah
5/06/22
Lincence : Apache Lincence

Script Abstract:
This script provides helper function for setting up an aws s3 bucket
"""


import logging
import boto3
import json
import argparse
from botocore.exceptions import ClientError, EndpointConnectionError

# configure logs
logging.basicConfig(
    level=logging.INFO, filemode="a+",
    filename="aws-config.log",
    format='%(asctime)s >> %(levelname)s >> %(message)s'
)

# s3 client intitial call/setup
s3_client = boto3.client('s3')


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).
    Args:
         param bucket_name: Bucket to create
         param region: String region to create bucket in, e.g., 'us-west-2'
    Return:
         True if bucket created, else False
    """

    # Create bucket
    try:
        s3_client.create_bucket(Bucket=bucket_name)

    except ClientError as e:
        logging.error(e)
        print("Action Failed : Please refer to logs at aws-config.log")
        return False
    else:
        return True


# Create a bucket policy

# Convert the policy from JSON dict to string
#bucket_policy = json.dumps(bucket_policy)

# Set the new policy
def bucket_policy(policy_file_path: str, bucket_name: str):
    """set a bucket policy for s3 bucket
    Args:
        policy_file_path: file path of the bucket policy json file
    Return:
        None , An inplace operation is performed to set bucket policy"""

    if policy_file_path == "null":
        pass
    else:
        with open(policy_file_path, "r") as jsonfile:
            bucket_policy = json.load(jsonfile)
        s3_client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    Args:
        param file_name: File to upload
        param bucket: Bucket to upload to
        param object_name: S3 object name. If not specified then file_name is used

    Return:
        True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    else:
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="set-up AWS Bucket Configurations")

    #create arparse group to distinguish tasks
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-c",
        "--create_bucket",
        action="store_true",
        help="Create a new S3 bucket >> returns true if specified")

    group.add_argument(
        "-u",
        "--upload_file",
        action="store_true",
        help="Uploaded a File into an s3 bucket >> returns true if specified")

    group.add_argument(
        "-up",
        "--update_policy",
        action="store_true",
        help="Update S3 bucket policy into >> returns true if specified")

    #common arguments
    
    parser.add_argument(
        "--bucket",
        "-b",
        type=str,
        required = False,
        default="ucc-code-bucket",
        help="bucket-name",
        metavar='')

    parser.add_argument(
        "--policy_file",
        "-p",
        type=str,
        required=False,
        default="null",
        help="<option to set bucket policy> file path to the bucket policy",
        metavar='')

    parser.add_argument(
        "--object",
        "-o",
        type=str,
        required=False,
        default = "myfakeobject", ###
        help="object file path",
        metavar='')

    parser.add_argument(
        "--filename",
        "-f",
        type=str,
        default="course_tutor_attrition_data",
        help="name of the file object to be uploaded")

    args = parser.parse_args()

    if args.create_bucket:
        try:
            create_bucket(bucket_name=args.bucket, region=None)
        except BaseException:
            raise

    elif args.upload_file:
        if args.object!="myfakeobject": ###
            upload_file(args.filename, args.bucket, args.object)
        else:
            print("please provide object file")

    elif args.update_policy:
        bucket_policy(args.policy_file)

    else:
        print("No Action Specified")
        _ = input("Do you need some help ? y/N  : ")
        if _ == "y":
            print("\n Available aws actions include:\n 1. Creating a New Bucket \n 2. Updating Bucket Policies \n 3. Uploading objects")
            print("\nuse aws-config.py --help \t to get help on each functionality :)")
        else:
            pass
