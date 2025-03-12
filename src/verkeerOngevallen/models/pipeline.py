import os
from .file_handler import FileHandler
from .data_processor import DataProcessor

class AccidentDataPipeline:
    def __init__(self, path):
        self.path = path
    def process_data(self):
        reader = FileHandler(self.path)
        original_df = reader.read_data()
        processor = DataProcessor(original_df)
        if not os.path.exists("Merge_Data"):
            os.makedirs("Merge_Data")
        processor.transform_data(original_df,'Merge_Data/Orignal_data.csv')
        clean_df = processor.validate_data()
        processor.transform_data(clean_df,'Merge_Data/Clean_data.csv')
        return processor.data