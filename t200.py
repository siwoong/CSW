import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
CH1=23  #left
CH2=24  #right

GPIO.setup(CH1, GPIO.OUT)
GPIO.setup(CH2, GPIO.OUT)

pwm1=GPIO.PWM(CH1,50)
pwm2=GPIO.PWM(CH2,50)

pwm.start(3) #초기시작값
pwm.start(3) #초기시작값

pwm1.ChangeDutyCycle(4)
pwm2.ChangeDutyCycle(4)