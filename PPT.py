import random
import time
import rich

from rich import style, color, emoji
from rich import color_triplet
from rich.theme import Theme
from rich.progress import track
from rich.console import Console

custom_theme = Theme({'valido':'italic green','error':'italic red','humano':'#3887E1','pc':'#F0882D'})
console = Console(theme=custom_theme)

def validacion_ingreso():
    validacion = True

    while validacion:

        opcion_humano = console.input('ingresa tu opcion.. ')
        print('')

        opcion_humano = opcion_humano.lower()
        if opcion_humano.isalpha():
            if opcion_humano == 'piedra' or opcion_humano == 'papel' or opcion_humano == 'tijera':
                validacion = False
            else:
                console.print('al parecer escribiste mal la opcion..\n', style='error')
        else:
            console.print(f'caracter invalido, porfavor ingresar de nuevo\n', style='error')

    return opcion_humano

seguir_jugando = True
wins_pc = 0
wins_humano = 0

print('')
print('bienvenido a Piedra, Papel o Tijera 2021')

while seguir_jugando:

    console.print('Introduce [humano]piedra[/] para jugarlo')
    console.print('Introduce [humano]papel[/]  para jugarlo')
    console.print('Introduce [humano]tijera[/] para jugarlo\n')
    opcion_humano = validacion_ingreso()

    if opcion_humano == 'piedra':
        respuesta_humano = 'piedra'
    elif opcion_humano == 'papel':
        respuesta_humano = 'papel'
    elif opcion_humano == 'tijera':
        respuesta_humano = 'tijera'

    opcion_pc = random.randint(0,2)
    if opcion_pc == 0:
        respuesta_pc = 'piedra'
    elif opcion_pc == 1:
        respuesta_pc = 'papel'
    elif opcion_pc == 2:
        respuesta_pc = 'tijera'

    console.print(f'seleccionaste: [humano]{respuesta_humano}[/]')
    console.print(f'seleccion de la pc: [pc]{respuesta_pc}[/]')

    if respuesta_humano == 'piedra' and respuesta_pc == 'tijera':
        console.print(f'ganaste!', style='valido')
        wins_humano += 1

    elif respuesta_humano == 'papel' and respuesta_pc == 'piedra':
        console.print(f'ganaste!', style='valido')
        wins_humano += 1

    elif respuesta_humano == 'tijera' and respuesta_pc == 'papel':
        console.print(f'ganaste!', style='valido')
        wins_humano +=1

    elif respuesta_pc == 'piedra' and respuesta_humano == 'tijera':
        console.print(f'perdiste!', style='error')
        wins_pc += 1

    elif respuesta_pc == 'papel' and respuesta_humano == 'piedra':
        console.print(f'perdiste!', style='error')
        wins_pc += 1
        
    elif respuesta_pc == 'tijera' and respuesta_humano == 'papel':
        console.print(f'perdiste!', style='error')
        wins_pc += 1

    else:
        console.print(f'empate', style='dim')

    print('')
    console.print(f'tus victorias: [blue]{wins_humano}[/]')
    console.print(f'victorias de la pc: [pc]{wins_pc}[/]\n')
  
    jugar_denuevo_pregunta = console.input('desea jugar de nuevo? ([green]y[/]/[red]n[/]).. ')
    print('')

    validacion_volverjugar = True

    while validacion_volverjugar:

        if jugar_denuevo_pregunta == 'y':
            console.print('─────────────────────────────────────────────────────────────────────────────────────────\n')
            validacion_volverjugar = False
            seguir_jugando = True

        elif jugar_denuevo_pregunta == 'n':
            console.print('terminando programa...', style='blink')
            time.sleep(1)
            validacion_volverjugar = False
            seguir_jugando = False

        else: 
            console.print('ingresar y/n para definir la accion!', style='error')
            jugar_denuevo_pregunta = console.input('desea jugar de nuevo? ([green]y[/]/[red]n[/])..')
            print('')
