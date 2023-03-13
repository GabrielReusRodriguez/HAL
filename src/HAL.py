#!/bin/env python3

# -*- coding: utf-8 -*-

"""
Este código es una interfaz para utilizar ChatGPT por consola linux ( preferentemente ).
Se presupone que tendrás definida la variable de entorno  OPEN_AI_KEY definida con la api key que te dan en la web, si no NO funcionará, 
    tendrás que modificar el script para especificarle el fichero de la key o hardcodear la key.
"""

#Imports
import  sys
from OpenAIFacade.OpenAIFacade import OpenAIFacade
from Params.ParamsManager import ParamsManager

#Obtengo los parámetros del programa.
paramManager = ParamsManager( parameterList = sys.argv[1:])
paramManager.parseArgs()

hal = OpenAIFacade( questionManager = paramManager.questionManager, responseManager = paramManager.responseManager  )
hal.run()
