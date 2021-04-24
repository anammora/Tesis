import RPi.GPIO as GPIO
import os
import time

#Define nombre de las entradas del puente H

enb = 18
in3 = 23
in4 = 24

OutA = 17
OutB = 27



GPIO.setwarnings(False)
#configura los pines segun el microprocesador Broadcom
GPIO.setmode(GPIO.BCM)

def  Giro_Favor_Reloj_MotorB():
    
	GPIO.output(in3,False)
	GPIO.output(in4,True)
	
def run():
#GPIO.setmode(GPIO.BCM)
    #global counter,OutALast
    #print(counter)
    #configura los pines como salidas

    GPIO.setup(enb,GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    GPIO.setup(OutA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(OutB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Define las salidas PWM q
    pwm_b = GPIO.PWM(enb,500)

    #inicializan los PWM con un duty Cicly de cero
    pwm_b.start(0)
    # funciones de sentido de giro de los motores

    counter = 0
    OutALast = GPIO.input(OutA)
    try:
        while True:
            velocidad=15
            OutAState=GPIO.input(OutA)
            OutBState=GPIO.input(OutB)
            #if a>b:
                #print('1 comparacion')
            if counter<317:
                #print('2 comparacion')
                Giro_Favor_Reloj_MotorB()
                pwm_b.ChangeDutyCycle(int(velocidad))
                print
                #print(OutAState,OutALast)
                if OutAState != OutALast:
                    #print('3 comparacion')
                    if OutBState != OutAState:
                        counter +=1
                        #print('4 comparacion')
                    #print(counter)
                OutALast=OutAState
                #time.sleep(0.01)
            else:
                print('bye')
                pwm_b.stop()
                #counter=0
                break
                #os.system('clear')
                #GPIO.cleanup() 
                
    except :
        GPIO.cleanup() 
        pass
GPIO.cleanup()    
                
    
#run()    
#os.system('clear')
