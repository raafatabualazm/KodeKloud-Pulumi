"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3, ec2

# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2('my-bucket-raafat')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# Create Security Group for SSH on Webserver

sg = ec2.SecurityGroup("webserver-sg", description="SG to allow SSH")

allow_ssh = ec2.SecurityGroupRule("Allow SSH", type="ingress", from_port=22, to_port=22, protocol="tcp", cidr_blocks=["0.0.0.0/0"], security_group_id=sg.id)

# Create an EC2 instance

ec2_instance = ec2.Instance("web_server", ami="ami-0349dc82277d50797",instance_type="t3.nano",tags={"Name":"webserver"}, vpc_security_group_ids=[sg.id])

# Export Public IP

pulumi.export('Public IP', ec2_instance.public_ip)
