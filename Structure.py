import os
import logging

# Define project structure

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s] : %(message)s:')

project_structure = {
    "project_Dojo": {
        "app": [
            "__init__.py",
            "db_manager.py",
            "bio_service.py",
            "config.py"
        ],
       ".env": None,
        "main.py": None,
        "requirement.txt": None
    }
}



def get_project_structure(base_path, structures):
    for folder, content in structures.items():
        folder_path = os.path.join(base_path, folder)
        print(f"Created folder: {folder_path}")
        if isinstance(content, dict):
            os.makedirs(folder_path, exist_ok=True)  # Create folder

            get_project_structure(folder_path, content)
        if isinstance(content, list):
            os.makedirs(folder_path, exist_ok=True)  # Create folder

            for file in content:
                file_path = os.path.join(folder_path, file)
                open(file_path, "w").close()
                print(f"Created file: {file_path}")
        elif content is None:
            # Create a file directly in the base path
            # file_path = os.path.join(base_path, folder)
            open(folder_path, "w").close()
            print(f"Created file: {file_path}")

# Base path for the project
base_path = os.getcwd()  # Current working directory
get_project_structure(base_path, project_structure)

print("Project structure creation complete.")