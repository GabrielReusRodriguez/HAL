# -*- coding: utf-8 -*-

import getopt
import os

from Constants.Constants import Constants
from OpenAIFacade.QuestionManager import QuestionManager
from OpenAIFacade.ResponseManager import ResponseManager


class ParamsManager:

    def __init__(self, parameterList : list[str]):
        
        self._listaParametros = parameterList

        #Opciones posibles
        self._options = "hlki:ofq:"
        #Opciones desplegadas
        self._long_options =[ "help", "log", "key","input=","output","file_key","question="]

        #Flags
        self._flag_log = False
        self._flag_inputBatch = False
        self._flag_help =  False
        
        #Parametros literales
        self._listaPreguntas = None
        self._log_carpeta = None
        self._inputBatch_file = None
        
        self.logManager = None
        self.questionManager = None
        self.responseManager = None


    def parseArgs(self):

        try:
            # Parsing argument
            arguments, values = getopt.getopt(self._listaParametros, self._options, self._long_options)
     
            # checking each argument
            for currentArgument, currentValue in arguments:
 
                if currentArgument in ("-h", "--help"):
                    self.help()
                    exit(0)

                elif currentArgument in ("-i", "--input"):
                    self._listaPreguntas = []
                    self._inputBatch_file = currentValue
                    self.cargaFicheroPreguntas()
             
                elif currentArgument in ("-o", "--Output"):
                    print (("Enabling special output mode (% s)") % (currentValue))

                elif currentArgument in ("-q","--question"):
                    self._listaPreguntas = []
                    self._listaPreguntas.append(currentValue)

        except getopt.error as err:
            # output error, and return with an error code
            print (str(err))
            exit(1)

        """Hago check de las precondiciones
            1. Que tenga la api
            2. Si tengo definida el log, quiero que la ruta de log se defina.
        """
        self.questionManager = QuestionManager(
            listaPreguntas  = self._listaPreguntas 
            )
        self.responseManager = ResponseManager()


    def help(self):
        print(
"""{} v{} by {}
    Ejecución: {} {{lkqh}} {{log_file}} {{i}} {{input_file}}
        l,--log:\t Logea  en el fichero que le especifivamos con --log-file <TODO>
        i,--input:\t Ejecuta las preguntas de un fichero y  guarda las respuestas en un fichero <TODO>
        k,--key:\t  Especifica la key de chatgpt <TODO>
        q,--question:\t Pasa por parámetro la pregunta.
        h,--help:\t Imprime esta ayuda.
 
""".format(Constants.PROGRAMA,Constants.VERSION, Constants.AUTHOR,Constants.PROGRAMA)
)

    def cargaFicheroPreguntas(self):
        if (os.path.isfile( self._inputBatch_file )):
            f = open(  self._inputBatch_file , "r")
            for line in f:
                self._listaPreguntas.append(line)
            f.close()
        else:
            print ("El fichero con las preguntas NO existe.")
            exit(1)
