#!/usr/bin/python3

import boto3

ec2 = boto3.resource('ec2')
snapshot = ec2.Snapshot()
print(snapshot)

