# -*- coding: utf-8 -*-

import openai
from OpenAIFacade.Engines import Engines
from OpenAIFacade.QuestionManager import QuestionManager
from OpenAIFacade.ResponseManager import ResponseManager
from Exceptions import HALException
from OpenAIFacade.LogManager import LogManager


class OpenAIFacade:

    #Constructor
    def __init__(self, questionManager: QuestionManager, responseManager: ResponseManager, logManager : LogManager = None ):
        #Variables locales.
        #self.unica_ejecucion = False
        #self.log             = False
        #self.log_file        = None
        #self.batch           = False
        #self.batch_file      = None
        #model_engine    = "gpt-3.5-turbo"
        self._model_engine       = Engines.GPT_3_5_TURBO
        self._run_bucle          = True
        self._questionManager    = questionManager
        self._responseManager    = responseManager
        self._logManager         = logManager


    #Funciones
    def run(self):

        try:
            while(self._run_bucle):
                pregunta = self._questionManager.obtenPregunta()
                if pregunta == "***":
                    self._run_bucle = False
                    continue


                response = openai.ChatCompletion.create(
                    model = self._model_engine,
                    messages = [
                        { "role": "system", "content": pregunta}
                    ]
                )

                self._responseManager.imprimeRespuesta(response)
                
                if ( self._questionManager.preguntasPendientes() <= 0 ):    
                    self._run_bucle = False
        except HALException as ex:
            print 