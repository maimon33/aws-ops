import json

import boto3
from botocore.exceptions import ClientError

def _format_json(dictionary):
    return json.dumps(dictionary, indent=4, sort_keys=True)

ec2 = boto3.client('ec2')

list_of_instances = []

try:
    sg_response = ec2.describe_security_groups()
    ins_response = ec2.describe_instances()
    for i in ins_response["Reservations"]:
        if i["Instances"][0]["State"]["Name"] == 'running':
            instance_dict = {}
            instance_dict["instance"] = i["Instances"][0]["InstanceId"]
            list_of_securitygroups = []
            for sg in i["Instances"][0]["SecurityGroups"]:
                list_of_securitygroups.append(sg["GroupId"])
            instance_dict["Security Groups"] = list_of_securitygroups
            list_of_instances.append(instance_dict)
    print list_of_instances
except ClientError as e:
    print(e)
