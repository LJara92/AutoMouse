import time
import pyautogui
import keyboard
import sys

# Constantes
NUM_COORDINATES = 5
CLICK_DELAY = 0.15
DRAG_DURATION = 1
BUTTON_DELAY = 0.1
PAGE_CHANGE_DELAY = 0.25

# Variables globales
coordenadas = []

def obtener_coordenadas():
    global coordenadas
    print("Ingresar las coordenadas")
    print("Abre el archivo que necesitas automatizar")
    print("Mueve el mouse a la posición deseada y presiona F2")
    print("Recuerda que solo puedes asignar 5 coordenadas")
    coordenadas = []

    while len(coordenadas) < NUM_COORDINATES:
        if keyboard.is_pressed('F2'):
            x, y = pyautogui.position()
            coordenadas.append((x, y))
            time.sleep(CLICK_DELAY)

    print('Coordenadas grabadas')

def guardar_coordenadas():
    global coordenadas
    if coordenadas:
        with open("coordenadas.txt", "w") as file:
            for x, y in coordenadas:
                file.write(f"{x},{y}\n")
        print("Coordenadas guardadas en el archivo 'coordenadas.txt'.")
    else:
        print("No hay coordenadas para guardar.")

def cargar_coordenadas():
    global coordenadas
    try:
        with open("coordenadas.txt", "r") as file:
            coordenadas = [tuple(map(int, line.strip().split(','))) for line in file]
        print("Coordenadas cargadas correctamente.")
    except FileNotFoundError:
        print("El archivo 'coordenadas.txt' no existe.")
    except Exception as e:
        print(f"Error al cargar las coordenadas: {e}")

def obtener_repeticiones():
    ciclos = int(input("Ingrese la cantidad de repeticiones: "))
    return ciclos

def iniciar_firma_documento():
    if not coordenadas:
        print("No hay coordenadas asignadas. Debes asignar coordenadas antes de iniciar la firma.")
        return

    try:
        cant_repeticiones = obtener_repeticiones()
        print('En 5 segundos se va a empezar a mover solo el mouse')
        print('Abre el archivo que desees firmar')
        time.sleep(4)

        boton_firmar, seleccion_firma, posicion_firma, boton_guardar, boton_siguiente_pagina = coordenadas

        for i in range(cant_repeticiones):
            pyautogui.moveTo(boton_firmar, duration=CLICK_DELAY)
            pyautogui.click(button='left', clicks=1, interval=CLICK_DELAY)
            pyautogui.moveTo(seleccion_firma, duration=CLICK_DELAY)
            pyautogui.dragTo(posicion_firma, button='left', duration=DRAG_DURATION)
            pyautogui.moveTo(boton_guardar, duration=CLICK_DELAY)
            pyautogui.click(button='left', clicks=1, interval=BUTTON_DELAY)
            pyautogui.moveTo(boton_siguiente_pagina, duration=PAGE_CHANGE_DELAY)
            pyautogui.click(button='left', clicks=1, interval=CLICK_DELAY)

        print(f'Se firmaron {cant_repeticiones} hojas')
        time.sleep(2)
    except KeyboardInterrupt:
        print("Proceso de automatización interrumpido por el usuario.")


def instrucciones():
    print("\n")
    def mecanografiar(texto):
        
        lista = texto.split()

        for palabra in lista:
            sys.stdout.write(palabra + " ")
            sys.stdout.flush()
            time.sleep(0.11)
        
        print('\n')
    
    mecanografiar("---- Bienvenido a AutoMouse ----")
    mecanografiar("Este es un simple programa que te permite firmar varias hojas de un documento de una forma automatica y rapida")
    mecanografiar("---------------------------------------------------------------------------------------------------------------")
    mecanografiar("2. Asignar coordenadas:")
    mecanografiar("Si es la primera vez que se usa el programa, se deben asignar coordenadas (opcion 2)")
    mecanografiar("Una vez seleccionada la opcion 2, debe abrir el archivo que desea firmar")
    mecanografiar("Cuando este abierto, recuerde que debe ajustar el tamaño de la firma y guardar el documento")
    mecanografiar("Al finalizar este paso debe posicionar el mouse en las siguientes posiciones y tocar F2 sobre cada una, resperado el orden")
    mecanografiar("- Boton de firma")
    mecanografiar("- Seleccion de firma")
    mecanografiar("- Posicion donde va la firma")
    mecanografiar("- Boton de guardado")
    mecanografiar("- Boton de siguiente pagina")
    mecanografiar("---------------------------------------------------------------------------------------------------------------")
    mecanografiar("3. Guardar coordenadas:")    
    mecanografiar('Ahora como opcion, podes seleccionar "Guardar coordenadas" para utilizarlas la proxima vez')
    mecanografiar("Para guardas las coordenadas, debe seleccionar la opcion 3")
    mecanografiar('Esto va a crear un archivo .txt con las coordenadas asignadas en la opcion 2')
    mecanografiar("---------------------------------------------------------------------------------------------------------------")
    mecanografiar("4. Cargar coordenadas:")
    mecanografiar('Si ya contas con coordenadas guardadas, (archivo .txt generado con la opcion 3) podes seleccionar "Cargar coordenadas"')
    mecanografiar("Vamos a utilizar las coordenadas guardas para firmar el documento")
    mecanografiar("---------------------------------------------------------------------------------------------------------------")
    mecanografiar("5. Iniciar firma del documento:")
    mecanografiar('Una vez que tenemos la coordenadas, se habilita una nueva opcion "Iniciar firma del documento"')
    mecanografiar("Al seleccionarla nos solicitara la cantidad de repeticiones que debe hacer (cantidad de hojas del documento)")
    mecanografiar("Y en 5 segundos se inicia de forma automatica la firma del documento")
    mecanografiar("Y al finalizar todo el proceso, el programa vuelve al menu principal")
    mecanografiar("---------------------------------------------------------------------------------------------------------------")
    mecanografiar("0. Salir:")
    mecanografiar("Cierra el programa")
    
def mostrar_menu():
    while True:
        print("\n---- MENU ----")
        print("1. Instrucciones")
        print("2. Asignar coordenadas")
        print("3. Guardar coordenadas")
        print("4. Cargar coordenadas")
        if coordenadas:
            print("5. Iniciar firma del documento")
        print("0. Salir")
        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            instrucciones()
        elif opcion == "2":
            obtener_coordenadas()
        elif opcion == "3":
            guardar_coordenadas()
        elif opcion == "4":
            cargar_coordenadas()
        elif opcion == "5" and coordenadas:
            iniciar_firma_documento()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
