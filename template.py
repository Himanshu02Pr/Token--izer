import os
from pathlib import Path

project_name = 'tokenizers'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/classical/__init__.py",
    f"src/{project_name}/subword/__init__.py",
    f"src/{project_name}/visualisation/__init__.py",
    f"src/{project_name}/evaluation/__init__.py",
    f"src/{project_name}/registry.py",
    "datasets/"
    "models/"
    "app.py",
    "requirements.txt",
    "setup.py",
    "pyproject.toml"
  


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass