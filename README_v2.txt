INSTRUCTIONS:
    1. The script runs on python2.7+.
    2. Install the boto3 library.
    3. Install and set the AWS CLI tools within the box to run the python boto3 script

PREREQUISITES:
​ Linux (Ubuntu):-

For Python3
    1. Install python3-pip
$ sudo apt-get install python3-pip
    2. Install boto3
$ pip3 install boto3
For Python2
    1. Install python-pip
$ sudo apt-get install python-pip
    2. Install boto3
$ pip install boto3

​Windows:-

For Python2 Install boto3
$ pip install boto3 For Python3
Install boto3
$ pip3 install boto3

Setting up AWS CLI:-
​AWS CLI Accesskey/SecretKey setup:​-$ aws configure
AWS Access Key ID [****************QJRA]: AWS Secret Access Key [****************YNCw]:
Default region name [ ]: (Your default region here) Default output format [None]:

TESTING:

    1. All the Files within the Single folder: Example:
$ ls

README.txt   untagged.py

FILE	DETAILS

------	---------

README.txt.	- Instructions & Brief Explanation text file

Untagged.py	- Script that performs the listing of untagged AWS resources on the

AWS account used by the boto3
2. For a functional operation:

Command:

./untagged.py

Output:

0. ap-south-1
1. eu-west-3
2. eu-west-2
3. eu-west-1
4. ap-northeast-2
5. ap-northeast-1
6. sa-east-1
7. ca-central-1
8. ap-southeast-1
9. ap-southeast-2
10. eu-central-1
11. us-east-1
12. us-east-2
13. us-west-1
14. us-west-2
Select a region '0 - 14' $ 13         
untagged_amis:
0. ami-07e139a4c74252da8

untagged_subnets:
0. subnet-36f5ec50
1. subnet-8235fcd8
2. subnet-9b162ed3

untagged_rt:
0. rtb-2f8be548
1. rtb-0b1232940d67a5dd8
2. rtb-0a1a19ef816bcd84b

untagged_igw:
0. igw-e5cd4381

untagged_ni:
0. eni-05417ef8a184fc9b6
1. eni-02ee3c394aff9208e
2. eni-4084296e
3. eni-033b53b2648b1db9c
4. eni-0e0ccfc12d01bac15
5. eni-0fe2ffdf7a09dfbd1


Instances with no tags in:
0. i-06b68afdcbd3e0266
1. i-083a8950c51a95b59
2. i-0a7b6382d792dbdfd
3. i-0d970ecaf18508545

Volumes with no tags in:
0. vol-08604a7954b4e96f9
1. vol-052d380bb664dbec5
2. vol-0bb7b1b0978106fb8
3. vol-09908c5b54203404f
4. vol-07dd32b7a779c0f0e
5. vol-0c3f3bde1bed75ca3


Snapshots with no tags in:
0. snap-0cbd933cd94f53278

untagged_vpc:
0. vpc-18b17d7f

untagged_security:
0. sg-0021680738e72021f
1. sg-00cae68a9b3c4dc63
2. sg-0174247530ffe2073
3. sg-0187e3a074c6a70b0
4. sg-01b970c40d5a5aa4b
5. sg-01bc238fb36e6c04e


untagged_elb:
0. Maureen
1. EnquizitLB

untagged_asg:
0. chebet

untagged_eip:
0. 13.56.34.196
1. 54.219.113.67
2. 54.241.236.27