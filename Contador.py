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

GPIO.setup(LEDA, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDB, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDC, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDD, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDE, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDF, GPIO.OUT) # Indicamos que el pin será salida
GPIO.setup(LEDG, GPIO.OUT) # Indicamos que el pin será salida

try: #Inicio del try
	while True: #Inicio del bucle infinito
         
         # Numero 0
		GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDE, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDG, GPIO.LOW) # Apaga el pin
		sleep(0.5)
         # Numero 1
		GPIO.output(LEDA, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDF, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDG, GPIO.LOW) # Apaga el pin
		sleep(0.5)
         # Numero 2
		GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDC, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDE, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDF, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
		sleep(0.5)
         # Numero 3
		GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDF, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
		sleep(0.5)
		# Numero 4
		GPIO.output(LEDA, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
		sleep(0.5)
		# Numero 5
		GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDB, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
		sleep(0.5)
		# Numero 6
		GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDB, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
		# Numero 7
		GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDF, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDG, GPIO.LOW) # Apaga el pin
		sleep(0.5)
		# Numero 8
		GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDE, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
		sleep(0.5)
		# Numero 9
		GPIO.output(LEDA, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDB, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDC, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDD, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDE, GPIO.LOW) # Apaga el pin
		GPIO.output(LEDF, GPIO.HIGH) # Enciende el pin
		GPIO.output(LEDG, GPIO.HIGH) # Enciende el pin
		sleep(0.5)

except KeyboardInterrupt: #Excepción del try
      GPIO.cleanup() # Limpia los pines en caso de excepción
