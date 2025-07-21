import sys
import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    msg = str(error)    
    error_message=f"Error occured in Python Script [{file_name}] at Line Number [{line_no}] with Error Message [{msg}]"
    
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        
        self.error_message = error_message_details(error_message,error_detail=error_details)
        
    def __str__(self):
        return self.error_message
    
        
