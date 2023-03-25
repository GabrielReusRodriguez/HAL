# -*- coding: utf-8 -*-

class HALException(Exception):
    
    def __init__(self, desc: str, codigo:int = None   ):
        self._codigo = codigo
        self._descripcion = desc
        super.__init(self._descripcion)
    
    def getCodigo(self):
        return self._codigo
    
    def getDescripcion(self):
        return self._descripcion