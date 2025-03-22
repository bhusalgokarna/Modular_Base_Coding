import os
import sys
from pathlib import Path
# Add src directory to sys.path
src_path = Path(__file__).resolve().parent.parent.parent 
sys.path.append(str(src_path))
import pandas as pd
from verkeerOngevallen.interfaces.process_file import DataCleaningProcess


class DataProcessor(DataCleaningProcess):
    def __init__(self, data):
        #self.data = data.copy()
        self.data = data
        self.keep_cols=[]
        self.numeric_cols = ['DT_HOUR', 'MS_ACCT', 'MS_ACCT_WITH_DEAD', 'MS_ACCT_WITH_DEAD_30_DAYS', 
                              'MS_ACCT_WITH_MORY_INJ', 'MS_ACCT_WITH_SERLY_INJ', 'MS_ACCT_WITH_SLY_INJ']
        self.date_col = 'DT_DAY'
        
    #Implement the validate_data method
    def validate_data(self):
        if self.data is None:
            print("Data is empty")
        else:
            # Remove the columns that are not useful to analysis of the data
            for col in self.data.columns:
                if col.endswith("_FR") or col.startswith("CD"):
                    self.data.drop(col, axis=1, inplace=True)
                else:
                    self.keep_cols.append(col)
            self.data = self.data[self.keep_cols]

            # Remove leading/trailing spaces     
            self.data[self.date_col] = self.data[self.date_col].str.strip()  
            
            # Change the correct dtypes of the columns to numeric
            self.data[self.numeric_cols] = self.data[self.numeric_cols].apply(pd.to_numeric, errors='coerce')

            # Feature Engineering for the date columns
            self.data['Year'] = self.data[self.date_col].str[:4].astype('Int64', errors='ignore')
            self.data['Month'] = self.data[self.date_col].str[5:7].astype('Int64', errors='ignore')
            self.data['Day_of_Month'] = self.data[self.date_col].str[8:10].astype('Int64', errors='ignore') 
            self.data['total_Deaths'] = self.data['MS_ACCT_WITH_DEAD'] + self.data['MS_ACCT_WITH_DEAD_30_DAYS']

            # Drop the date column
            self.data.drop(self.date_col, axis=1, inplace=True)

            

            # Fill the missing values of province with Brussels
            self.data['TX_PROV_DESCR_NL'] = self.data['TX_PROV_DESCR_NL'].replace(['', ' '], 'Brussels')
            self.data.fillna({'TX_PROV_DESCR_NL': 'Brussels'}, inplace=True)
            
               
            # Rename the columns
            columns_rename = {
                'DT_DAY': 'Day', 'DT_HOUR': 'Hour', 'TX_DAY_OF_WEEK_DESCR_NL': 'DayOfWeek',
                'TX_BUILD_UP_AREA_DESCR_NL': 'BuiltUpArea', 'TX_COLL_TYPE_DESCR_NL': 'CollisionType',
                'TX_LIGHT_COND_DESCR_NL': 'LightCondition', 'TX_ROAD_TYPE_DESCR_NL': 'RoadType',
                'TX_MUNTY_DESCR_NL': 'Municipality', 'TX_ADM_DSTR_DESCR_NL': 'District',
                'TX_PROV_DESCR_NL': 'Province', 'TX_RGN_DESCR_NL': 'Region', 'MS_ACCT': 'Accident',
                'MS_ACCT_WITH_DEAD': 'AccidentsWithFatalities', 'MS_ACCT_WITH_DEAD_30_DAYS': 'AccidentsWithFatalities30Days',
                'MS_ACCT_WITH_MORY_INJ': 'AccidentsWithMinorInjuries', 'MS_ACCT_WITH_SERLY_INJ': 'AccidentsWithSeriousInjuries',
                'MS_ACCT_WITH_SLY_INJ': 'AccidentsWithSlightInjuries'
            }
            # This loop will rename the columns
            for key, value in columns_rename.items():
                self.data.rename(columns={key: value}, inplace=True)
                
            print("Data cleaned successfully") 
            return self.data
        
    #Implement the transform_data method   
    def transform_data(self, data, output_path):
        self.output_Path = output_path
        if os.path.exists(self.output_Path):
            os.remove(self.output_Path)
        data.to_csv(self.output_Path, index=False)
        print(f"Data saved successfully at {self.output_Path}")

    #Implement the print_information method
    def print_information(self, data_to_print):
        print("-" * 50)
        print(f"Shape of the data: {data_to_print.shape}\n")
        print("Data Info:\n")
        data_to_print.info()
        print("\nStatistics of Data:\n")
        print(data_to_print.describe().T)
        print("\nColumns of Dataframe:\n")
        print(data_to_print.columns)
        print("\nDatatypes of Dataframe:\n")
        print(data_to_print.dtypes)
        print("\nAre there any null values:\n")
        print(data_to_print.isnull().sum())
        print(f"Top 5 rows of the dataframe:\n")
        print(data_to_print.head())
        print("-" * 50)