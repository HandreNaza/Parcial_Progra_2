import pygame 
import random
from Funciones import *
from Preguntas import *

pygame.init()
cuadro_pregunta = {}
#cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
cuadro_pregunta["superficie"] = pygame.image.load("fondo.jpg")
cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()
#cuadro_pregunta["superficie"].fill(COLOR_ROJO)

#----------Boton--comodin
boton_comodin = {}
boton_comodin["superficie"] = pygame.image.load("boton_inicio.png")  # Carga la imagen del botón
boton_comodin["superficie"] = pygame.transform.scale(boton_comodin["superficie"], TAMAÑO_BOTON)  # Escala la imagen al tamaño del botón
boton_comodin["rectangulo"] = boton_comodin["superficie"].get_rect()


lista_respuestas = []

for i in range(4):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cuadro_respuesta["superficie"].fill(COLOR_AZUL)
    lista_respuestas.append(cuadro_respuesta)
    
indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables
random.shuffle(lista_preguntas)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    
    retorno = "juego"
    if bandera_respuesta:
        pygame.time.delay(250)
        #cuadro_pregunta["superficie"].fill(COLOR_ROJO)
        #Limpio la superficie
        cuadro_pregunta["superficie"] = pygame.image.load("fondo.jpg")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)
        for i in range(len(lista_respuestas)):
            lista_respuestas[i]["superficie"].fill(COLOR_AZUL)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #Funcion comodin
            if boton_comodin["rectangulo"].collidepoint(evento.pos):
                print("Comodín activado")
                bomba_dtroy_res(lista_respuestas, pregunta_actual)
                resultado = verificar_respuesta(lista_respuestas, evento, pregunta_actual, datos_juego, indice)
                
            #Funcion para mostrar------------
            else: resultado = verificar_respuesta(lista_respuestas, evento, pregunta_actual, datos_juego, indice)
            if resultado == "terminado":
             retorno = "terminado"


            indice += 1   
            if indice == len(lista_preguntas):
                indice = 0
                random.shuffle(lista_preguntas)
                
            bandera_respuesta = True

    
    pantalla.fill(COLOR_VIOLETA)
    #pantalla.blit(fondo,(0,0))
    
    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["pregunta"]}",(20,20),FUENTE_27,COLOR_NEGRO)
    mostrar_texto(lista_respuestas[0]["superficie"],f"{pregunta_actual["respuesta_1"]}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],f"{pregunta_actual["respuesta_2"]}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],f"{pregunta_actual["respuesta_3"]}",(20,20),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(boton_comodin["superficie"],"COMODIN",(105,20),FUENTE_30,COLOR_BLANCO) # Comodin
    
    cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(80,80))
    lista_respuestas[0]["rectangulo"] = pantalla.blit(lista_respuestas[0]["superficie"],(125,245))#r1
    lista_respuestas[1]["rectangulo"] = pantalla.blit(lista_respuestas[1]["superficie"],(125,315))#r2
    lista_respuestas[2]["rectangulo"] = pantalla.blit(lista_respuestas[2]["superficie"],(125,385))#r3
    boton_comodin["rectangulo"] = pantalla.blit(boton_comodin["superficie"],(125,455)) # Comodin
        
   

    pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[0]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[1]["rectangulo"],2)
    pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[2]["rectangulo"],2)
    
    
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(10,40),FUENTE_25,COLOR_NEGRO)
    
    return retorno