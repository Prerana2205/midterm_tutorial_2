# import pytest
# from cdktf import Testing

# # The tests below are example tests, you can find more information at
# # https://cdk.tf/testing


# class TestMain:

#     def test_my_app(self):
#         assert True

#     #stack = TerraformStack(Testing.app(), "stack")
#     #app_abstraction = MyApplicationsAbstraction(stack, "app-abstraction")
#     #synthesized = Testing.synth(stack)

#     # def test_should_contain_container(self):
#     #    assert Testing.to_have_resource(self.synthesized, Container.TF_RESOURCE_TYPE)

#     # def test_should_use_an_ubuntu_image(self):
#     #    assert Testing.to_have_resource_with_properties(self.synthesized, Image.TF_RESOURCE_TYPE, {
#     #        "name": "ubuntu:latest",
#     #    })

#     # def test_check_validity(self):
#     #    assert Testing.to_be_valid_terraform(Testing.full_synth(stack))

import os

# Get the current directory
current_directory = os.getcwd()


# List all files in the current directory
file_names = os.listdir(current_directory+"/static-website/images")



# Print the file names
# for file_name in file_names:
#     print(file_name)
    
    
# for file_name in file_names:
#     file_path = os.path.join(current_directory+"/static-website", file_name)
#     #print(file_path)
#     if os.path.isdir(file_path): 
#         print(f"{file_name} is directory")
#     else:
#         print(file_name)
        



# Specify the path to the PNG file
def upload_files_to_s3(folder_path, parent_key=""):
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    print(f"{item} is directory")
                    upload_files_to_s3(item_path, f"{parent_key}/{item}")
                else:
                    print(item)
                

        # # # Specify the local folder path containing the static website

        # # # Upload files from local folder to S3 bucket recursively
upload_files_to_s3(current_directory+"/static-website")