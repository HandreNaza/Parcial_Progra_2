import pygame
from Constantes import *
from Funciones import *

pygame.init()

fondo = pygame.image.load("configuracion.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

boton_suma = {}
boton_suma["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()
boton_suma["superficie"].fill(COLOR_ROJO)

boton_resta = {}
boton_resta["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()
boton_resta["superficie"].fill(COLOR_ROJO)

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

boton_mute = {}  # Botón de mute
boton_mute["superficie"] = pygame.image.load("vol_mute.png") 
boton_mute["superficie"] = pygame.transform.scale(boton_mute["superficie"],TAMAÑO_BOTON_VOLUMEN)
boton_mute["rectangulo"] = boton_mute["superficie"].get_rect()





def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuracion"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                else:
                    ERROR_SONIDO.play()
                print("SUMA VOLUMEN")
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                else:
                    ERROR_SONIDO.play()
                print("RESTA VOLUMEN")
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                print("VUELVE AL MENU")
            elif boton_mute["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] > 0:
                    # Guardar el volumen actual antes de mutear
                    datos_juego["volumen_musica_guardado"] = datos_juego["volumen_musica"]
                    datos_juego["volumen_musica"] = 0  # Mutear
                    print("MUTE ACTIVADO")
                else:
                    # Restaurar el volumen guardado
                    datos_juego["volumen_musica"] = datos_juego["volumen_musica_guardado"]
                    print("MUTE DESACTIVADO")
                
    porcentaje_coma = datos_juego["volumen_musica"] / 100
    pygame.mixer.music.set_volume(porcentaje_coma)

    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo, (0, 0))
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,200))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(320,200))    
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    boton_mute["rectangulo"] = pantalla.blit(boton_mute["superficie"], (20, 130))
    
    mostrar_texto(boton_suma["superficie"],"VOL+",(0,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"VOL-",(0,10),FUENTE_22,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(boton_mute["superficie"], "MUTE", (10, 10), FUENTE_20, COLOR_BLANCO)  # Mostrar texto para mute
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(130,200),FUENTE_50,COLOR_NEGRO)
    
    return retorno
