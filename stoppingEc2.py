import boto3

# Initialize EC2 resource
ec2 = boto3.resource('ec2', region_name='us-east-1')  # Change region if needed

# Loop through all instances
for instance in ec2.instances.all():
    instance_id = instance.id
    state = instance.state['Name']

    print(f"Instance ID: {instance_id}, State: {state}")

    # Stop only if instance is running
    if state == 'running':
        print(f"Stopping instance {instance_id}...")
        instance.stop()
