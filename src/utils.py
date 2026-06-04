from sklearn.metrics import r2_score
import os
import sys
import numpy as np 
import pandas as pd 
import dill

from sklearn.metrics import r2_score
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

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}

        for i in range(len(list(models))):
            model=list(models.values())[i]

            model.fit(X_train,y_train) # train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score =r2_score(y_train,y_train_pred)

            test_model_score= r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score
            
        return report

    except Exception as e:
        raise CustomException(e,sys)


    