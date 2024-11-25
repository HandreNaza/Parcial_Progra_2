from Constantes import *
import random
import pygame

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.




#comodin--------------------
def bomba_dtroy_res(lista_respuestas, pregunta_actual):
     for i in range(len(lista_respuestas)):
        if (i + 1) != pregunta_actual["respuesta_correcta"]:  # Si no es la respuesta correcta
            lista_respuestas[i]["superficie"].fill(COLOR_ROJO)  # Cambiar a color gris
            #mostrar_texto(lista_respuestas[i]["superficie"],f"{pregunta_actual[respuesta_1]}",(20,20),FUENTE_22,COLOR_NONE)
            lista_respuestas[i]["rectangulo"] = None 
 
 
 
#Segundo intento 

def verificar_respuesta(lista_respuestas, evento, pregunta_actual, datos_juego, indice):

    for i in range(len(lista_respuestas)):
                
                if lista_respuestas[i]["rectangulo"] and lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    
                    if respuesta_seleccionada == pregunta_actual["respuesta_correcta"]:
                        ACIERTO_SONIDO.play()
                        print("RESPUESTA CORRECTA")
                        lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
                        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
                    else:
                        ERROR_SONIDO.play(maxtime=2000)
                        lista_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        if datos_juego["puntuacion"] > 0:
                            datos_juego["puntuacion"] -= PUNTUACION_ERROR
                        datos_juego["cantidad_vidas"] -= 1
                        print("RESPUESTA INCORRECTA")
                        return  "terminado"
    return None