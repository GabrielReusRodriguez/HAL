#!/bin/env python3

# -*- coding: utf-8 -*-

"""
Este código es una interfaz para utilizar ChatGPT por consola linux ( preferentemente ).
Se presupone que tendrás definida la variable de entorno  OPEN_AI_KEY definida con la api key que te dan en la web, si no NO funcionará, 
    tendrás que modificar el script para especificarle el fichero de la key o hardcodear la key.
"""

#Imports
import openai
import getopt, sys
from OpenAIFacade.Engines import Engines

#Constantes
PROGRAMA    =   "myChatGPT"
VERSION     =   "0.1"
AUTHOR      =   "Gabriel Reus Rodriguez"
CONTACT     =   "https://github.com/GabrielReusRodriguez/myChatGPT"

#Funciones
def printHelp():
    ayuda =""" {} 
    Esta es la segunda linea al respecto."""

    print(
"""{} v{} by {}
    Ejecución: {} {{hul}} {{log_file}} {{b}} {{batch_file}}
        h,--help:\t Imprime esta ayuda.
        u,--unica:\t Realiza una única consulta.
        l,--log:\t Logea  en el fichero que le especifivamos con --log_file <TODO>
        b,--batch:\t Ejecuta  las preguntas de un fichero y  guarda las respuestas en un fichero <TODO>
        k,--key:\t  Especifica la key de chatgpt <TODO>
""".format(PROGRAMA,VERSION, AUTHOR,PROGRAMA)
)

#Función para entrar la pregunta nque queremos enviar a chatGPT
def entraPregunta():
    pregunta = None
    pregunta = input("*** ¿Que quieres preguntarle a ChatGpt ?:\n")
    return pregunta

#Función que imprime la respuesta.
def muestraRespuesta(response):
    message = response.choices[0]['message']
    print("\n+++ {}:\n{}\n\n".format( message['role'], message['content']))

#Declaraciones de variables inicial.
unica_ejecucion = False
log             = False
log_file        = None
batch           = False
batch_file      = None
#model_engine    = "gpt-3.5-turbo"
model_engine    = Engines.GPT_3_5_TURBO
run_bucle       = True


#Obtengo los parámetros del programa.
#Listado de parámetros
argumentList = sys.argv[1:]

#Opciones posibles
options = "hulbkiof"

#Opciones desplegadas
long_options =[ "help", "log", "unica","batch","key","input","output","file_key"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--help"):
            printHelp()
            exit(0)
             
        elif currentArgument in ("-u", "--unica"):
            unica_ejecucion = True
             
        elif currentArgument in ("-o", "--Output"):
            print (("Enabling special output mode (% s)") % (currentValue))


except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    exit(1)

"""Hago check de las precondiciones
    1. Que tenga la api
    2. Si tengo definida el log, quiero que la ruta de log se defina.
"""

#Lanzamos las preguntas...

while(run_bucle):
    pregunta = entraPregunta()
    if pregunta == "***":
        run_bucle = False
        continue


    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            { "role": "system", "content": pregunta}
        ]
    )

    muestraRespuesta(response)
    
    if( unica_ejecucion == True):
        run_bucle = False

