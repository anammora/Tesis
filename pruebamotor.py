#! /usr/bin/env python
import RPi.GPIO as GPIO
import os
import time
#Define nombre de las entradas del puente H

enb = 18
in3 = 23
in4 = 24
#configura los pines segun el microprocesador Broadcom
GPIO.setmode(GPIO.BCM)
#configura los pines como salidas

GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
#Define las salidas PWM q
pwm_b = GPIO.PWM(enb,500)
#inicializan los PWM con un duty Cicly de cero
pwm_b.start(0)
# funciones de sentido de giro de los motores

def  Giro_Favor_Reloj_MotorB():
	GPIO.output(in3,False)
	GPIO.output(in4,True)

def Giro_Contra_Reloj_MotorB():
	GPIO.output(in3,True)
	GPIO.output(in4,False)
#limpia la pantalla
os.system('clear')
print("Elija motor[A-B], el sentido [F-R] y la velocidad [0-100]")
print("ejemplo 'AF50' MOTOR A Foward a 50%. de velocidad")
print("CTRL-C para salir")
print
try:
	while True:
		cmd = raw_input("inserte el comando ")
		cmd = cmd.lower()
		motor = cmd[0]
		direccion =cmd[1]
		velocidad =cmd[2:5]


		if motor == "b":
			if direccion == "f":
				Giro_Favor_Reloj_MotorB()
				print("motor B, CW, vel="+velocidad)
			elif direccion == "r":
				Giro_Contra_Reloj_MotorB()
			else:
				print("comando no reconocido")
			pwm_b.ChangeDutyCycle(int(velocidad))
			print
		else:
			print
			print("comando no reconocido")
			print
except KeyboardInterrupt:
	
	pwm_b.stop()
	GPIO.cleanup()
	os.system('clear')
	print
	print("Programa Terminado por el usuario")
	print
	exit()
