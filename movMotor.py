import RPi.GPIO as GPIO
import os
import time

#Define nombre de las entradas del puente H

enb = 18
in3 = 23
in4 = 24

clk = 17
dt = 27



GPIO.setwarnings(False)
#configura los pines segun el microprocesador Broadcom
GPIO.setmode(GPIO.BCM)

def  Giro_Favor_Reloj_MotorB():
    
	GPIO.output(in3,False)
	GPIO.output(in4,True)
	
def run():
#GPIO.setmode(GPIO.BCM)
    #global counter,clkLastState
    #print(counter)
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
    try:
        while True:
            velocidad=15
            clkState=GPIO.input(clk)
            dtState=GPIO.input(dt)
            #if a>b:
                #print('1 comparacion')
            if counter<315:
                #print('2 comparacion')
                Giro_Favor_Reloj_MotorB()
                pwm_b.ChangeDutyCycle(int(velocidad))
                print
                #print(clkState,clkLastState)
                if clkState != clkLastState:
                    #print('3 comparacion')
                    if dtState != clkState:
                        counter +=1
                        #print('4 comparacion')
                    #print(counter)
                clkLastState=clkState
                #time.sleep(0.01)
            else:
                print('bye')
                pwm_b.stop()
                #counter=0
                break
                #os.system('clear')
                #GPIO.cleanup() 
                
    except :
        pass
                
    
#run()    
#os.system('clear')
