import os
from pathlib import Path
import logging

#Log format for the execution
logging.basicConfig(level= logging.INFO, format="[%(asctime)s]:%(message)s:")

project_name = "cnnClassifier"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, filename = os.path.split(file_path)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok= True)
        logging.info(f"Creating directory: {file_dir} and the file {filename}")
    
    if (not os.path.exists(file_dir)) or (os.path.getsize(file_dir)== 0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file: {file_dir}")
    else:
        logging.info(f"{filename} already exists")
