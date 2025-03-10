import os
from abc import ABC, abstractmethod


# Interface for loading data
class LoadDataProcess(ABC):

    @abstractmethod
    def read_data(self):
        pass