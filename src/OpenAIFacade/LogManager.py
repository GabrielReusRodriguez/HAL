# -*- coding: utf-8 -*-

import calendar
import time
import os

from datetime import datetime

from Exceptions import HALException

class LogManager:
    
    def __init__(self, folder : str = None):

        
        self._folder = None
        if folder == None:
            self._folder = "./"
        else:
            self._folder = folder
        #fileName = folder+"/"+fileName
        #self._file = fileName
        self._fileName = "HAL_"+self._getFormatedTimeStamp()+".log"
        self._fileDescriptor= None


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

    def init(self):

        if  os.path.isDir(self._folder) == False  :
            exception = HALException(desc="La carpeta no existe")
            raise exception
        self._fileDescriptor = open( self._folder+"/"+self._fileName,"w")

    def finish(self):
        if self._fileDescriptor is None:
            exception = HALException(desc="Se hace log en un fichero que NO está abierto.")
            raise exception
        self._fileDescriptor.close()

    def log(self, txt: str):
        if self._fileDescriptor is None:
            exception = HALException(desc="Se hace log en un fichero que NO está abierto.")
            raise exception
        msg=""
        hdr = self._getFormatedTimeStamp()
        msg = hdr+": "+txt
        self._fileDescriptor.write(msg)