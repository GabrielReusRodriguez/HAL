# -*- coding: utf-8 -*-

import openai
from OpenAIFacade.Engines import Engines
from OpenAIFacade.QuestionManager import QuestionManager
from OpenAIFacade.ResponseManager import ResponseManager
from OpenAIFacade.LogManager import LogManager


class OpenAIFacade:

    #Constructor
    def __init__(self,_questionManager: QuestionManager, _responseManager: ResponseManager, _logManager : LogManager = None ):
        #Variables locales.
        #self.unica_ejecucion = False
        #self.log             = False
        #self.log_file        = None
        #self.batch           = False
        #self.batch_file      = None
        #model_engine    = "gpt-3.5-turbo"
        self.model_engine       = Engines.GPT_3_5_TURBO
        self.run_bucle          = True
        self.questionManager    = _questionManager
        self.responseManager    = _responseManager
        self.logManager         = _logManager


    #Funciones
    def run(self):

        while(self.run_bucle):
            pregunta = self.questionManager.obtenPregunta()
            if pregunta == "***":
                self.run_bucle = False
                continue


            response = openai.ChatCompletion.create(
                model = self.model_engine,
                messages = [
                    { "role": "system", "content": pregunta}
                ]
            )

            self.responseManager.imprimeRespuesta(response)
            
            if ( self.questionManager.preguntasPendientes() <= 0 ):    
                self.run_bucle = False
