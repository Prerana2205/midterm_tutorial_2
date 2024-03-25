#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws.provider import AwsProvider
from imports.aws.ecs_cluster import EcsCluster
from imports.aws.instance import Instance
from imports.aws.s3_bucket import S3Bucket
from imports.aws.s3_bucket_policy import S3BucketPolicy
from imports.aws.s3_bucket_object import S3BucketObject
from imports.aws.s3_bucket_public_access_block import S3BucketPublicAccessBlock
from imports.aws.s3_bucket_ownership_controls import S3BucketOwnershipControls, S3BucketOwnershipControlsRule
import json
import os


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        AwsProvider(self, "AWS", region="us-east-1")
        
        local_folder_path = os.getcwd()+"/scripts/configure.sh"

        bucket = S3Bucket(self, "bucket", bucket="exam-2-scripts")

        user_data_asset = S3BucketObject(self, "ScriptFile",
            bucket=bucket.bucket,
            key='scripts/configure.sh',
            source=local_folder_path
        )
        
        instance = Instance(self, "compute",
                            ami="ami-01456a894f71116f2",
                            instance_type="t2.micro",
                            tags={"Name": "CDKTF-Demo"},
                            user_data=user_data_asset.source
                            )

        TerraformOutput(self, "public_ip",
                        value=instance.public_ip,
                        )
        
        


app = App()
MyStack(app, "tutorial_1")

app.synth()

