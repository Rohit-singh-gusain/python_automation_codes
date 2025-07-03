

import boto3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def stop_instances():
    # Create EC2 client
    ec2 = boto3.client('ec2', region_name='us-east-1')
    
    try:
        # Get running instances
        response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        
        instances_to_stop = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instances_to_stop.append(instance_id)
                logger.info(f"Found running instance: {instance_id}")
        
        if instances_to_stop:
            logger.info(f"Attempting to stop instances: {instances_to_stop}")
            
            # Actually stop instances (disable dry run)
            response = ec2.stop_instances(
                InstanceIds=instances_to_stop,
                DryRun=False  # Explicitly set to False to execute for real
            )
            
            logger.info(f"Stop response: {response}")
            logger.info("Successfully sent stop command")
        else:
            logger.info("No running instances found")
            
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    stop_instances()