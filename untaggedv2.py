#!/usr/bin/python3
###########################################
#  Script to dislay untagged resources    #
#  Author: DDD Team                       #
#  Version 1.2                            #
#                                         #
###########################################

import boto3, sys
##Initializing variables to be used

#Empty lists to hold specified untagged resources
untagged_amis = []
untagged_subnets = []
untagged_rt = []
untagged_igw = []
untagged_ni = []
Instances_not_tagged = []
Volumes_not_tagged = []
Snapshots_not_tagged = []
untagged_vpc = []
untagged_security = []
untagged_elb = []
untagged_asg = []
untagged_eip = []

 #variables holding aws data.
client = boto3.client('ec2')
regions = [region['RegionName'] for region in client.describe_regions()['Regions']] 
      #list regions for user to select
for region in range(len(regions)):
	print('{}. {}'.format(region, regions[region]))
select = input("Select a region '0 - 14' $ ")
try:
	region = regions[int(select)]
except IndexError:
	sys.exit("Out of range. Select between {} and {}".format(min(range(len(regions))), max(range(len(regions)))))
except ValueError:
	sys.exit("Input must be of type int")


#Check for untagged images and append to corresponding list above
client = boto3.client('ec2', region)
images = client.describe_images(Owners = ['self'])
for image in images['Images']:
	try:
		tag = (image["Tags"])
	except KeyError:
		untagged_amis.append(image["ImageId"])

#Check for untagged subnets and append to corresponding list above
client = boto3.client('ec2')
subnets = client.describe_subnets()
for subnet in subnets['Subnets']:
	try:
		tag = (subnet["Tags"])
	except KeyError:
		untagged_subnets.append(subnet["SubnetId"])

#Check for untagged route_tables and append to corresponding list above
ec2 = boto3.resource('ec2', region)
route_table = ec2.RouteTable('id')
client = boto3.client('ec2', region)
route_tables = client.describe_route_tables()
for tables in route_tables['RouteTables']:
	if tables["Tags"]:
		tag = (tables["Tags"])
	else:
		untagged_rt.append(tables['RouteTableId'])

#Check for untagged internet_gateways and append to corresponding list above
internet_gateway = ec2.InternetGateway('id')
client = boto3.client('ec2', region)
internet_gateways = client.describe_internet_gateways()
for state in internet_gateways['InternetGateways']:
	if state["Tags"]:
		tag = (state["Tags"])
	else:
		untagged_igw.append(state['InternetGatewayId'])

#Check for untagged network_interfaces and append to corresponding list above
network_interface = ec2.NetworkInterface('id')
client = boto3.client('ec2', region)
network_interfaces = client.describe_network_interfaces()
for network in network_interfaces['NetworkInterfaces']:
	try:
		tag = (network["Tags"])
	except KeyError:
		untagged_ni.append(network['NetworkInterfaceId'])

#Check for untagged instances and append to corresponding list above
ec2client = boto3.client('ec2',region)              
instance_response = ec2client.describe_instances()
for reservation in instance_response["Reservations"]:
    for instance in reservation["Instances"]:
        try:
        	 tag = (instance["Tags"])
        except KeyError:
        	Instances_not_tagged.append(instance["InstanceId"])


#Check for untagged volumes and append to corresponding list above
volume_iterator = ec2.volumes.all()
for volume in volume_iterator:
    for a in volume.attachments:
    	if volume.tags == None:
    		Volumes_not_tagged.append(volume.id)

#Check for untagged snapshots and append to corresponding list above
client = boto3.client('ec2', region)
response_snapshots = client.describe_snapshots(OwnerIds=['self'])
for snapshots in response_snapshots["Snapshots"]:
	try:
		tags = snapshots["Tags"]
	except KeyError:
		Snapshots_not_tagged.append(snapshots["SnapshotId"])


#Check for untagged vpcs and append to corresponding list above
client = boto3.client('ec2', region)
vpc = ec2.Vpc('id')
response = client.describe_vpcs()
for v in response["Vpcs"]:
	try:
		tags = v["Tags"]
	except KeyError:
		untagged_vpc.append(v["VpcId"])

#Check for untagged SecurityGroups and append to corresponding list above
security_group = ec2.SecurityGroup('id')
client = boto3.client('ec2', region)
security_groups = client.describe_security_groups()
for security in (security_groups['SecurityGroups']):
		try:
			tags = (security["Tags"])
		except:
			untagged_security.append(security['GroupId'])


#Check for untagged load_balancers and append to corresponding list above
#ec2 = boto3.resource('ec2', region)
client = boto3.client('elb', region)
load_balancers = client.describe_load_balancers()
for load in(load_balancers['LoadBalancerDescriptions']):
	try:
		tag = (load["Tags"])
	except:
		untagged_elb.append(load['LoadBalancerName'])

#Check for untagged auto_scaling_groups and append to corresponding list above
client = boto3.client('autoscaling', region)
auto_scaling_groups = client.describe_auto_scaling_groups()
for groups in (auto_scaling_groups['AutoScalingGroups']):
	tags = groups['Tags']
	if not tags:
		untagged_asg.append(groups['AutoScalingGroupName'])


#Check for untagged Elastic ip addresses and append to corresponding list above
ec2 = boto3.client('ec2', region)
addresses = ec2.describe_addresses()
for p in (addresses['Addresses']):
	try:
		tag = (p["Tags"])
	except:
		untagged_eip.append(p['PublicIp'])

#Function to display the untagged resources held on the lists above
def display(description, resource):
	if resource:
		print("{}:".format(description))
		for item in range(len(resource)):
			print("{}. {}".format(item,resource[item]))
		print('')


#display function call
display("untagged_amis", untagged_amis)
display("untagged_subnets", untagged_subnets)
display("untagged_rt", untagged_rt)
display("untagged_igw", untagged_igw)
display("untagged_ni", untagged_ni)
display("Instances with no tags in", Instances_not_tagged)
display("Volumes with no tags in", Volumes_not_tagged)
display("Snapshots with no tags in", Snapshots_not_tagged)
display("untagged_vpc", untagged_vpc)
display("untagged_security", untagged_security)
display("untagged_elb", untagged_elb)
display("untagged_asg", untagged_asg)
display("untagged_eip", untagged_eip)