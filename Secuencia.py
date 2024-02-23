import RPi.GPIO as GPIO #Importación de los pines GPIO
from time import sleep # Importación del módulo sleep para hacer delays

GPIO.setmode(GPIO.BOARD) #BCM - Importación de los pines para llamarlos por la dirección física

LEDGPIO4 = 7 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO5 = 29 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO6 = 31 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO12 = 32 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO13 = 33 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO16 = 36 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO17 = 11 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO18 = 12 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO19 = 35 #Indicamos que el pin que queremos para el led es el 29
LEDGPIO20 = 38 #Indicamos que el pin que queremos para el led es el 29


GPIO.setup(LEDGPIO4, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO5, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO6, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO12, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO13, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO16, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO17, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO18, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO19, GPIO.OUT) # Indicamos que el pin 31 será salidas
GPIO.setup(LEDGPIO20, GPIO.OUT) # Indicamos que el pin 31 será salidas


try: #Inicio del try
   while True: #Inicio del bucle infinito
      GPIO.output(LEDGPIO4, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO5, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO6, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO12, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO13, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO16, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO17, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO18, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO19, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO20, GPIO.HIGH) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
      GPIO.output(LEDGPIO20, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO4, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO5, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO6, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO12, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO13, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO16, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO18, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO17, GPIO.LOW) # Enciende el pin 31
      GPIO.output(LEDGPIO19, GPIO.LOW) # Enciende el pin 31
      sleep(0.5) # Deleay de 30 segundos
except KeyboardInterrupt: #Excepción del try
   GPIO.cleanup() # Limpia los pines en caso de excepción
