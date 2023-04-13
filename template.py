""" creating template file to create project skeleton """

import os
import logging
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode="a"
)

while True:
    project_name= input("Enter the project_name: ")
    if project_name != "":
        break

# lazy formatting in logging funcs (pylint preferred way to do)
logging.info(" creating project by name: %s", project_name)
# logging.inf("creating project by name: {project_name}")

# list of files:
list_of_files= [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "requirements_dev.txt",
    "requirements.txt",
    "init_setup.sh",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "Makefile"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename= os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(" creating a directory at: %s for file name: %s", filedir, filename)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w", encoding="utf-8") as f:
            pass
        logging.info("creating a new filename: %s at filepath : %s", filename, filepath)
    else:
        logging.info(" file already present at: %s", filepath)
