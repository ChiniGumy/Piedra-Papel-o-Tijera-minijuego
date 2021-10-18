import random
import time
from rich import *

from rich.theme import Theme
from rich.console import Console

custom_theme = Theme({'valido':'italic #1EBD1E','error':'italic #FC3636','humano':'#3887E1','pc':'#F0882D'})
console = Console(theme=custom_theme)

def validacion_ingreso():
    
    validacion = True

    while validacion:

        opcion_humano = console.input('ingresa tu opcion.. ') 
        opcion_humano = opcion_humano.lower()
        opcion_humano = opcion_humano.strip(' ')
        print('')

        if opcion_humano.isalpha():
            if opcion_humano == 'piedra' or opcion_humano == 'papel' or opcion_humano == 'tijera':
                validacion = False
            else:
                console.print('al parecer escribiste mal la opcion..\n', style='error')
        else:
            console.print(f'caracter invalido, porfavor ingresar de nuevo\n', style='error')

    return opcion_humano

def ingreso_pc():

    opcion_pc = random.randint(0,2)

    if opcion_pc == 0:
        respuesta_pc = 'piedra'
    elif opcion_pc == 1:
        respuesta_pc = 'papel'
    elif opcion_pc == 2:
        respuesta_pc = 'tijera'

    return respuesta_pc

def quien_gana(r_humano, r_pc, wins_humano, wins_pc):

    condicion_h1 = r_humano == 'piedra' and r_pc == 'tijera'
    condicion_h2 = r_humano == 'papel' and r_pc == 'piedra'
    condicion_h3 = r_humano == 'tijera' and r_pc == 'papel'

    if condicion_h1 or condicion_h2 or condicion_h3:
        console.print(f'ganaste!', style='valido')
        wins_humano += 1

    elif r_humano == r_pc:
        console.print(f'empate', style='dim')

    else:
        console.print(f'perdiste!', style='error')
        wins_pc += 1

    return (wins_humano, wins_pc)

def pregunta_seguir_jugando():

    jugar_denuevo_pregunta = console.input('desea jugar de nuevo? ([green]y[/]/[red]n[/]).. ')
    jugar_denuevo_pregunta = jugar_denuevo_pregunta.strip(' ')
    print('') 

    seguir_jugar_pregunta = True

    while seguir_jugar_pregunta:

        if jugar_denuevo_pregunta == 'y':
            console.print('─────────────────────────────────────────────────────────────────────────────────────────────────────────────\n')
            seguir_jugar_pregunta = False
            seguir = True

        elif jugar_denuevo_pregunta == 'n':
            seguir_jugar_pregunta = False
            seguir = False

        else: 
            console.print('ingresar y/n para definir la accion!\n', style='error')
            jugar_denuevo_pregunta = console.input('desea jugar de nuevo? ([green]y[/]/[red]n[/])..')
            jugar_denuevo_pregunta = jugar_denuevo_pregunta.strip(' ')
            print('')

    return seguir

wins_humano = 0
wins_pc = 0

print('')
print('bienvenido a Piedra, Papel o Tijera 2021')

seguir_jugando = True
while seguir_jugando:

    console.print('Introduce [humano]piedra[/] para jugarlo')
    console.print('Introduce [humano]papel[/]  para jugarlo')
    console.print('Introduce [humano]tijera[/] para jugarlo\n')

    respuesta_humano = validacion_ingreso()
    respuesta_pc = ingreso_pc()

    console.print(f'seleccionaste: [humano]{respuesta_humano}[/]')
    console.print(f'seleccion de la pc: [pc]{respuesta_pc}[/]')
    wins_humano, wins_pc = quien_gana(respuesta_humano, respuesta_pc, wins_humano, wins_pc)
    print('')

    console.print(f'tus victorias: [blue]{wins_humano}[/]')
    console.print(f'victorias de la pc: [pc]{wins_pc}[/]\n')

    seguir_jugando = pregunta_seguir_jugando()

console.print('gracias por jugar !')