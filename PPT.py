import random

def validacion_ingreso():
    validacion = True

    while validacion:

        opcion_humano = input('ingresa tu opcion.. ')
        if opcion_humano.isdigit():
            opcion_humano = int(opcion_humano)
            if  0 <= opcion_humano <= 2:
                validacion = False
            else:
                print('el numero ingresado debe estar entre 0 y 2')
        else:
            print('caracter invalido, porfavor ingresar de nuevo\n')

    return opcion_humano

print('bienvenido a Piedra, Papel o Tijera 2021')

seguir_jugando = True
        
while seguir_jugando:
    
    print('para usar piedra introduce 0')
    print('para usar papel  introduce 1')
    print('para usar tijera introduce 2\n')

    opcion_humano = validacion_ingreso()

    if opcion_humano == 0:
        respuesta_humano = 'piedra'
    elif opcion_humano == 1:
        respuesta_humano = 'papel'
    elif opcion_humano == 2:
        respuesta_humano = 'tijera'

    opcion_pc = random.randint(0,2)
    if opcion_pc == 0:
        respuesta_pc = 'piedra'
    elif opcion_pc == 1:
        respuesta_pc = 'papel'
    elif opcion_pc == 2:
        respuesta_pc = 'tijera'

    print(f'seleccionaste: {respuesta_humano}')
    print(f'seleccion de la pc: {respuesta_pc}')

    if respuesta_humano == 'piedra' and respuesta_pc == 'tijera':
        print('ganaste!')
    elif respuesta_humano == 'papel' and respuesta_pc == 'piedra':
        print('ganaste!')
    elif respuesta_humano == 'tijera' and respuesta_pc == 'papel':
        print('ganaste!')
    elif respuesta_pc == 'piedra' and respuesta_humano == 'tijera':
        print('perdiste!')
    elif respuesta_pc == 'papel' and respuesta_humano == 'piedra':
        print('perdiste!')
    elif respuesta_pc == 'tijera' and respuesta_humano == 'papel':
        print('perdiste!')
    else:
        print('empate ._.')

    print('')
    jugar_denuevo_pregunta = input('desea jugar de nuevo? y/n.. ')
    print('')


    validacion_volverjugar = True

    while validacion_volverjugar:

        if jugar_denuevo_pregunta == 'y':
            validacion_volverjugar = False
            seguir_jugando = True

        elif jugar_denuevo_pregunta == 'n':
            validacion_volverjugar = False
            seguir_jugando = False

        else: 
            print('ingresar y/n para definir la accion')
            jugar_denuevo_pregunta = input('desea jugar de nuevo? y/n..')
            print('')
