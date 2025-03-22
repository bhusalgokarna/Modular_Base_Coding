import os
import sys
from pathlib import Path
# Add src directory to sys.path
src_path = Path(__file__).resolve().parent.parent.parent  
sys.path.append(str(src_path))
import pandas as pd
from verkeerOngevallen.interfaces.read_file import LoadDataProcess


class FileHandler(LoadDataProcess):
    def __init__(self, path):
        self.path = path
        self.data = self.read_data()
    
    def read_data(self):
        data_list = []
        try:
            if os.path.isdir(self.path):
                for file in os.listdir(self.path):
                    file_path = os.path.join(self.path, file)
                    if file.endswith(".txt"):
                        data_list.append(pd.read_csv(file_path, sep='|', dtype=str))
                    elif file.endswith(".csv"):
                        data_list.append(pd.read_csv(file_path, dtype=str))
                    elif file.endswith(".xlsx"):
                        data_list.append(pd.read_excel(file_path, dtype=str))
                    elif file.endswith(".json"):
                        data_list.append(pd.read_json(file_path))
            data = pd.concat(data_list, ignore_index=True)
            return data
        except Exception as e:
            print(f"Error reading data: {e}")
            return None