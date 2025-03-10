

import os
from abc import ABC, abstractmethod


# Interface for loading data
class DataCleaningProcess(ABC):
    @abstractmethod
    def validate_data(self):
        pass 
    
    @abstractmethod
    def transform_data(self):
        pass    
    
    @abstractmethod
    def print_information(self):
        pass