import pygame 
from Constantes import *
from Funciones import *

pygame.init()

lista_botones = []
fondo = pygame.image.load("fondo_bg.png")
fondo = pygame.transform.scale(fondo,VENTANA)

for i in range(4):
    boton = {}
    boton["superficie"] = pygame.image.load("boton_inicio.png")  # Carga la imagen del botón
    boton["superficie"] = pygame.transform.scale(boton["superficie"], TAMAÑO_BOTON)  # Escala la imagen al tamaño del botón
    boton["rectangulo"] = boton["superficie"].get_rect()  # Obtén el rectángulo asociado a la superficie
    lista_botones.append(boton)
 
def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "menu"
    pygame.display.set_caption("MENU")

    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if lista_botones[BOTON_JUGAR]["rectangulo"].collidepoint(evento.pos):
                retorno = "juego"
                CLICK_SONIDO.play()
            elif lista_botones[BOTON_AJUSTES]["rectangulo"].collidepoint(evento.pos):
                retorno = "configuracion"
                CLICK_SONIDO.play()
            if lista_botones[BOTON_RANKINGS]["rectangulo"].collidepoint(evento.pos):
                retorno = "puntuaciones"
                CLICK_SONIDO.play()
            if lista_botones[BOTON_SALIR]["rectangulo"].collidepoint(evento.pos):
                retorno = "salir"
                CLICK_SONIDO.play()
   
                
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo, (0, 0))
    lista_botones[BOTON_JUGAR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_JUGAR]["superficie"],(50,115))
    lista_botones[BOTON_AJUSTES]["rectangulo"] = pantalla.blit(lista_botones[BOTON_AJUSTES]["superficie"],(50,195))
    lista_botones[BOTON_RANKINGS]["rectangulo"] = pantalla.blit(lista_botones[BOTON_RANKINGS]["superficie"],(50,275))
    lista_botones[BOTON_SALIR]["rectangulo"] = pantalla.blit(lista_botones[BOTON_SALIR]["superficie"],(50,355))
        
    mostrar_texto(lista_botones[BOTON_JUGAR]["superficie"],"JUGAR",(105,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_AJUSTES]["superficie"],"AJUSTES",(90,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_RANKINGS]["superficie"],"RANKINGS",(80,20),FUENTE_30,COLOR_BLANCO)
    mostrar_texto(lista_botones[BOTON_SALIR]["superficie"],"SALIR",(115,20),FUENTE_30,COLOR_BLANCO)
    
    return retorno
