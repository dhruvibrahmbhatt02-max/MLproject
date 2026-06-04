import os
import sys
import numpy as np 
import pandas as pd 
import dill

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        # get the directory path of the file path
        dir_path = os.path.dirname(file_path)

        #make a directory path
        os.makedirs(dir_path,exist_ok=True)

        # this is used for opening and writing the file
        with open(file_path, "wb") as file_obj:

            # dumping the object in binary format
            # this pickle is used to make a serialisation
            # dill is used to serialise the file in binary format
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)



        