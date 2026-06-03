'''
python provides various functions and variables that are used
to manipulate different parts of python runtime environment 
'''

import sys 
import logging

# whenever error gets it creates own custom expection

def error_message_details(error,error_detail:sys):
    #this will give on which file exception is occur and which code
    # store into this variable 
    _,_,exc_tb=error_detail.exc_info()
    # this code will be in custom exception handling documentation already
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] Line number[{1}] Error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)

    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
       super().__init__(error_message)
       self.error_message=error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
     
    
'''if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("DIVIDE by ZERO")
        raise CustomException(e,sys)'''
