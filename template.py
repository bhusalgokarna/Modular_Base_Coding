import os
from pathlib import Path

# Define project name
project_name = 'verkeerOngevallen'

# List of files to create
list_of_files = [
    f'src/{project_name}/interfaces/read_file.py',
    f'src/{project_name}/interfaces/process_file.py',
    f'src/{project_name}/models/file_handler.py',
    f'src/{project_name}/models/data_processor.py',
    f'src/{project_name}/models/pipeline.py',
    f'src/{project_name}/__init__.py',
    f'src/__init__.py',
    "requirements.txt",
]

# Iterate through each file in the list
for file in list_of_files:
    path = Path(file)  # Create a Path object
    filedir = path.parent  # Get the directory
    filename = path.name  # Get the file name
    
    # Create the directory if it doesn't exist
    if not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        print(f'Directory {filedir} created.')

    # Create the file if it doesn't exist
    if not path.exists():
        with open(path, 'w') as f:
            f.write('')
            print(f'File {filename} created in {filedir}')
    else:
        print(f'File {filename} already exists in {filedir}')

print('All files created successfully!')

    
        
        
            
        
       
            
   
    
         