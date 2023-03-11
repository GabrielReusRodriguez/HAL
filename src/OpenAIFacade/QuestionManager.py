# -*- coding: utf-8 -*-


class QuestionManager:
    
    def __init__(self, unica: bool = True, esBatch: bool = False ):
        self.unique = unica
        self.isBatch = esBatch
        self.preguntas = []

    def obtenPregunta(self):
        pregunta = None
        if self.isBatch == False:
            preguntaConsole = input("*** ¿Que quieres preguntarle a ChatGpt ?:\n")
            self.preguntas.append(preguntaConsole)
        if len(self.preguntas) > 0:
            pregunta = self.preguntas.pop()
        return pregunta
    
    def preguntasPendientes(self):
        if self.unique == False and self.isBatch == False:
            return 1
        else:
            return len(self.preguntas)
        
