import sys
import os
import shutil

APPS_DIR = "apps"

if len(sys.argv) < 2:
    print("Usage: python deploy.py <project-folder>")
    sys.exit(1)

project_path = sys.argv[1]

if not os.path.exists(project_path):
    print("Error: project folder does not exist")
    sys.exit(1)

project_name = os.path.basename(os.path.abspath(project_path))

destination = os.path.join(APPS_DIR, project_name)

if os.path.exists(destination):
    print(f"Error '{project_name}' is already deployed")
    sys.exit(1)

shutil.copytree(project_path, destination)

print(f"Deployment successful!")
print(f"Visit: http://localhost:8000/{project_name}")

