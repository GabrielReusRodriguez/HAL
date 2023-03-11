# -*- coding: utf-8 -*-

class ResponseManager:
    


    def __init__(self):
        #self.response = respuesta
        pass


    def imprimeRespuesta(self,response):
        message = response.choices[0]['message']
        print("\n+++ {}:\n{}\n\n".format( message['role'], message['content']))
