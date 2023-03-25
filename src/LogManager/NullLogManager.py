# -*- coding: utf-8 -*-


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
