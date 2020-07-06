import boto3
import click
# Retrieve the list of existing buckets
session = boto3.Session(profile_name="default")
s3 = session.resource('s3')
bucket = s3.Bucket('name')


@click.group()
def cli():
    "Deploys website to AWS"
    pass


@cli.command('list-buckets')
def list_buckes():
    "Output the bucket names"
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    print('listing bucket objects ...')
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)


if __name__ == "__main__":
    cli()
