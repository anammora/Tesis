import RPi.GPIO as GPIO
import os
import time

#Define nombre de las entradas del puente H

enb = 18
in3 = 23
in4 = 24

clk = 17
dt = 27

a=3
b=2

#configura los pines segun el microprocesador Broadcom
GPIO.setmode(GPIO.BCM)
#configura los pines como salidas

GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Define las salidas PWM q
pwm_b = GPIO.PWM(enb,500)

#inicializan los PWM con un duty Cicly de cero
pwm_b.start(0)
# funciones de sentido de giro de los motores

counter = 0
clkLastState = GPIO.input(clk)

def  Giro_Favor_Reloj_MotorB():
	GPIO.output(in3,False)
	GPIO.output(in4,True)

try:
    while True:
        velocidad=10
        clkState=GPIO.input(clk)
        dtState=GPIO.input(dt)
        
        if a>b:
            if counter<3274:
                Giro_Favor_Reloj_MotorB()
                pwm_b.ChangeDutyCycle(int(velocidad))
                if clkState != clkLastState:
                    if dtState != clkState:
                        counter +=1
                clkLastState=clkState
            else:
                pwm_b.stop()
                GPIO.cleanup()
                os.system('clear')
            
except KeyboardInterrupt:
	
	pwm_b.stop()
	GPIO.cleanup()
	os.system('clear')
	print
	print("Programa Terminado por el usuario")
	print
	exit()
        

