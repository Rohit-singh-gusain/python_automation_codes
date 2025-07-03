import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    
    for instance in ec2.instances.all():
        state = instance.state['Name']
        print(f"Instance ID: {instance.id}, State: {state}")
        
        if state == 'stopped':
            instance.start()
            print(f"Starting instance {instance.id}...")
    
    return {'status': 'done'}
