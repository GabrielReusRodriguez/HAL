# -*- coding: utf-8 -*-


import calendar
import time

from datetime import datetime


""" Clase abstracta para definir los LogManagers """

class LogManager():

    def init(self):
        """ Inicializa  el log"""
        pass
    
    def log(self, txt:str ):
        """ Escribe en el log"""
        pass

    def finish(self):
        """Finaliza el log y libera recursos"""
        pass

    def _getFormatedFileTimeStamp(self) -> str:

        #Current GMT time in a tuple format
        current_GMT = time.gmtime()
        
        # ts stores timestamp
        ts = calendar.timegm(current_GMT)

        date_time = datetime.fromtimestamp(ts)
        #str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
        str_date_time = date_time.strftime("%d%m%Y_%H%M%S")
        return str_date_time


    def _getFormatedTimeStamp(self) -> str:

        #Current GMT time in a tuple format
        current_GMT = time.gmtime()
        
        # ts stores timestamp
        ts = calendar.timegm(current_GMT)

        date_time = datetime.fromtimestamp(ts)
        str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
        #str_date_time = date_time.strftime("%d%m%Y_%H%M%S")
        return str_date_time
