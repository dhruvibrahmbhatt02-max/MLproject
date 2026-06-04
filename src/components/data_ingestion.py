from src.components import data_transformation
import os 
import sys
# exception
from src.exception import CustomException
# logging
from src.logger import logging
import pandas as pd 

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# data ingestion need inputs to save train , test and raw data in diff class
# use the class to define the paths and where to save them
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    # so soon as you call this class this upper class 3 paths will be get will saved in this (self.ingestionconfig) class variable

    # to read from the databases where the data is stored
    def initate_data_ingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            # any fil can perfrom by just changing this file path 
            df=pd.read_csv("data/stud.csv")
            logging.info("read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initate_data_ingestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)