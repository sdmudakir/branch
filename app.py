import boto3

client = boto3.client('ec2')
response = client.run_instances(
            ImageId='ami-0453ec754f44f9a4a',
                InstanceType='t2.medium',
                    KeyName = 'devops',

                        MaxCount=1,
                            MinCount=1,
                            )
