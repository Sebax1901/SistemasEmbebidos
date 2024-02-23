import RPi.GPIO as GPIO #Importación de los pines GPIO
from time import sleep # Importación del módulo sleep para hacer delays

GPIO.setmode(GPIO.BOARD) #BCM - Importación de los pines para llamarlos por la dirección física

LED = 29 #Indicamos que el pin que queremos para el led es el 29

GPIO.setup(LED, GPIO.OUT) # Indicamos que los pines GPIO serán salidas
try: #Inicio del try
   while True: #Inicio del bucle infinito
      GPIO.output(LED, GPIO.HIGH) # Enciende el pin 29
      sleep(2) # Deleay de 2 segundos
      GPIO.output(LED, GPIO.LOW) # Apaga el pin 29
      sleep(2) # Deleay de 2 segundos
except KeyboardInterrupt: #Excepción del try
   GPIO.cleanup() # Limpia los pines en caso de excepción
