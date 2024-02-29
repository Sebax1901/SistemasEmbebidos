# Juan Sebastián Fernández Enciso 89244
# Sebastián Camilo Ariza Rodríguez 88460

import RPi.GPIO as GPIO #Importación de los pines GPIO
from time import sleep # Importación del módulo sleep para hacer delays

GPIO.setmode(GPIO.BOARD) #BCM - Importación de los pines para llamarlos por la dirección física

LEDA = 29 #Indicamos que el pin que queremos para A
LEDB = 31 #Indicamos que el pin que queremos para B
LEDC = 11 #Indicamos que el pin que queremos para C
LEDD = 15 #Indicamos que el pin que queremos para D
LEDE = 16 #Indicamos que el pin que queremos para E
LEDF = 18 #Indicamos que el pin que queremos para F
LEDG = 13 #Indicamos que el pin que queremos para G

BIT1 = 37 #Indicamos el pin que será entrada
BIT1 = 37 #Indicamos el pin que será entrada
BIT2 = 22 #Indicamos el pin que será entrada
BIT3 = 36 #Indicamos el pin que será entrada
BIT4 = 33 #Indicamos el pin que será entrada

GPIO.setup(LEDA, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDB, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDC, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDD, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDE, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDF, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDG, GPIO.OUT) # Indicamos que el pin será salida

GPIO.setup(BIT1, GPIO.IN) # Indicamos que el pin será entrada
GPIO.setup(BIT2, GPIO.IN) # Indicamos que el pin será entrada
GPIO.setup(BIT3, GPIO.IN) # Indicamos que el pin será entrada
GPIO.setup(BIT4, GPIO.IN) # Indicamos que el pin será entrada

try: #Inicio del try
    while True: #Inicio del bucle infinito
		
        #Verificacion de los pines activos en la entrada 
        numeroBinario = [GPIO.input(BIT1),GPIO.input(BIT2),GPIO.input(BIT3),GPIO.input(BIT4)]
        #Conversion de Binario a decimal
        numeroDecimal = (numeroBinario[0]*(2**0)) + (numeroBinario[1]*(2**1)) + (numeroBinario[2]*(2**2)) + (numeroBinario[3]*(2**3)) 

        #Evaluacion del numero decimal para definir el numero que imprime
        if numeroDecimal == 0:
            #Numero0
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDE, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.LOW) # Apaga el pin
        elif numeroDecimal == 1:
            #Número 1
            GPIO.output(LEDA, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDF, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDG, GPIO.LOW) # Apaga el pin
        elif numeroDecimal == 2:
            #Número 2
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDE, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDF, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 3:
            #Número 3
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDF, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 4:
            #Número 4
            GPIO.output(LEDA, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 5:
            #Número 5
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin 
        elif numeroDecimal == 6:
            #Número 6
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDE, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 7:
            #Número 7
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDF, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDG, GPIO.LOW) # Apaga el pin
        elif numeroDecimal == 8:
            #Número 8
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDE, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 9:
            #Número 9
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 10:
            #Número 9
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDE, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 11:
            #Número 9
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDE, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 12:
            #Número 9
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.LOW) # Enciende el pin
            GPIO.output(LEDC, GPIO.LOW) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDE, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.LOW) # Enciende el pin
        elif numeroDecimal == 13:
            #Número 9
            GPIO.output(LEDA, GPIO.LOW) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDE, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDF, GPIO.LOW) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 14:
            #Número 9
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.LOW) # Enciende el pin
            GPIO.output(LEDC, GPIO.LOW) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDE, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        elif numeroDecimal == 15:
            #Número 9
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.LOW) # Enciende el pin
            GPIO.output(LEDC, GPIO.LOW) # Enciende el pin
            GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
            GPIO.output(LEDE, GPIO.HIGH) # Apaga el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
        else:
            #En caso de que no esté entre el 0 y el 9 imprime cero dado que está fuera de rango
            GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDE, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
            GPIO.output(LEDG, GPIO.LOW) # Apaga el pin
        
        #Sleep para que el programa no se congele y compile de manera adecuada
        sleep(0.5)

except KeyboardInterrupt: #Excepción del try
    GPIO.cleanup() # Limpia los pines en caso de excepción
