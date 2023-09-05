import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#Setting up motor pins
MOTOR1EN = 4
MOTOR2EN = 17

MOTOR1A = 3
MOTOR1B = 2

MOTOR2A = 22
MOTOR2B = 27

#Setting pin to output
GPIO.setup(MOTOR1EN, GPIO.OUT)
GPIO.setup(MOTOR2EN, GPIO.OUT)
GPIO.setup(MOTOR1A, GPIO.OUT)
GPIO.setup(MOTOR1B, GPIO.OUT)
GPIO.setup(MOTOR2A, GPIO.OUT)
GPIO.setup(MOTOR2B, GPIO.OUT)

GPIO.output(MOTOR1A,0)
GPIO.output(MOTOR1B,0)

#Setting up pwm for speed
MOTOR1PWM = GPIO.PWM(MOTOR1EN, 100)
MOTOR2PWM = GPIO.PWM(MOTOR2EN,100)

MOTOR1PWM.start(0)
MOTOR2PWM.start(0)

def forward():

    GPIO.output(MOTOR1A,1)
    GPIO.output(MOTOR1B,0)
    
    GPIO.output(MOTOR2A,0)
    GPIO.output(MOTOR2B,1)

    MOTOR1PWM.ChangeDutyCycle(60)
    MOTOR2PWM.ChangeDutyCycle(100)
    time.sleep(10)

forward()

