# -*- coding: utf-8 -*-

import os

from LogManager import LogManager
from Exceptions import HALException

class FileLogManager(LogManager):
    
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