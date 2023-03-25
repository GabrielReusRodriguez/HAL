# -*- coding: utf-8 -*-


class QuestionManager:
    
    def __init__(self, listaPreguntas:list[str] = None ):
        self._interactive = True
        self._preguntas = []
        if listaPreguntas != None:
            self._preguntas = listaPreguntas
            self._interactive = False

        

    def obtenPregunta(self) -> str:
        pregunta = None
        if self._interactive == True:
            preguntaConsole = input("*** ¿Que quieres preguntarle a ChatGpt ?:\n")
            self._preguntas.append(preguntaConsole)
        if len(self._preguntas) > 0:
            pregunta = self._preguntas.pop(0)
        #En caso que sea algo NO interactivo, imprimo la pregunta
        if self._interactive == False:
            print( "*** "+pregunta+"\n")
        return pregunta
    
    def preguntasPendientes(self) -> int:
        if self._interactive == True:
            return 1
        else:
            return len(self._preguntas)
        
