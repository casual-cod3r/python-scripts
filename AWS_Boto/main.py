# This is public code for educational use only. 
# Please check what instances are you terminating
# Before terminating, the script checks match to "key" of the instances and then if running, terminates the instance.
# Once temrinated the data may be lost!

from boto import ec2
import boto3
import boto_config_orig as boto_config
from pprint import pprint

aws_access_id = boto_config.aws_access_id
aws_access_key = boto_config.aws_access_key
ec21 = boto3.resource('ec2', boto_config.aws_region)

termination_list_instances = []

ec2conn = ec2.connection.EC2Connection(region=ec2.get_region(boto_config.aws_region))
reservations = ec2conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]

for i in instances:
    if str(i.key_name) == "<SPECIFIC KEY ONLY>" and str(i._state) != "terminated(48)": #CHECK FOR STATUS RUNNING
        termination_list_instances.append(str(i.id))

if not termination_list_instances:
    print("No instance to be terminated!")
    quit()

else:
    try:
        for i in termination_list_instances:
            print("Terminating this instance: " + i)
            ec21.instances.filter(InstanceIds=[i]).terminate() #real terminator

    except Exception as e:
        print(e)
