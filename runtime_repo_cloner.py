import os
import subprocess

repositories = [
    "ancillary-masterdata-service",
    "ancillary-customizations-service",
    "product-style-service",
    "product-item-service",
    "product-item-process-service",
    "product-style-integration-service"]

dir_name = os.getcwd()
print(dir_name)

relative_path = os.path.join(dir_name, "repos")

branch_name = "main"
new_branch = "new-branch"

def clone_repositories(repositories, relative_path):
    for repo in repositories:
        if not os.path.exists(relative_path):
            os.makedirs(relative_path)
        os.chdir(relative_path)

        command = f"https://github.com/brandix-ict/{repo}.git"
        
        process = subprocess.Popen(f"git clone {command}", shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(f"Repository {repo} cloned successfully")

        process = subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(f"Repository {repo} pulled successfully")

        process = subprocess.Popen(f"git checkout {branch_name}", shell=True, stdout=subprocess.PIPE)
        process.wait()
        process = subprocess.Popen(f"git checkout -b {new_branch}", shell=True, stdout=subprocess.PIPE)
        process.wait()
        print(f"Branch {new_branch} created successfully")

    print("All repositories cloned successfully")

clone_repositories(repositories, relative_path)
