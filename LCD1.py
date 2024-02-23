import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

TOGGLE_1 = 29
LCD_RS = 19
LCD_E = 21
LCD_D4 = 15
LCD_D5 = 16
LCD_D6 = 18
LCD_D7 = 22

bits_datos = [LCD_RS,LCD_E,LCD_D4,LCD_D5,LCD_D6,LCD_D7]

LCD_CHR = True
LCD_CMD = False
LCD_CHARS = 16
LINE_1 = 0x80
LINE_2 =0xC0

GPIO.setup(TOGGLE_1,GPIO.IN)

for salidas in bits_datos:
    GPIO.setup(salidas, GPIO.OUT)

def lcd_init():
    lcd_write(0x33,LCD_CMD)
    lcd_write(0x32,LCD_CMD)
    lcd_write(0x06,LCD_CMD)
    lcd_write(0x0C,LCD_CMD) 
    lcd_write(0x28,LCD_CMD)
    lcd_write(0x01,LCD_CMD)
    sleep(0.0005)
    
def lcd_write(bits, mode):

    GPIO.output(LCD_RS,mode)

    GPIO.output(LCD_D4,False)
    GPIO.output(LCD_D5,False)
    GPIO.output(LCD_D6,False)
    GPIO.output(LCD_D7,False)

    if bits&0x10==0x10:
        GPIO.output(LCD_D4,True)

    if bits&0x20==0x20:
        GPIO.output(LCD_D5,True)

    if bits&0x40==0x40:
        GPIO.output(LCD_D6,True)
    
    if bits&0x80==0x80:
        GPIO.output(LCD_D7,True)

    lcd_toggle_enable()

    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)

    if bits&0x01==0x01:
        GPIO.output(LCD_D4,True)

    if bits&0x02==0x02:
        GPIO.output(LCD_D5,True)

    if bits&0x04==0x04:
        GPIO.output(LCD_D6,True)

    if bits&0x08==0x08:
        GPIO.output(LCD_D7,True)

    lcd_toggle_enable()

def lcd_toggle_enable():
    sleep(0.0005)
    GPIO.output(LCD_E, True)
    sleep(0.0005)
    GPIO.output(LCD_E, False)
    sleep(0.0005)

def lcd_texto(message, line):

    message = message.ljust(LCD_CHARS," ")
    lcd_write(line, LCD_CMD)

    for i in range(LCD_CHARS):
        lcd_write(ord(message[i]),LCD_CHR)

def LCD(hora):
    lcd_init()
    lcd_texto(hora,LINE_1)
    sleep(0.01)

try:
    while True:

        if(GPIO.input(TOGGLE_1)== 1):
            LCD('Sistemas Embebidos')

        else:
            LCD('UNIVERSIDAD ECCI')
        sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()