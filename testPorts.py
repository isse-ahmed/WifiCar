#If Forwards and Backwards are reversed, switch the pinouts
from gpiozero import Robot
from time import sleep

motor1A = 2
motor1B = 3
motor1PWM = 3

motor2A = 27
motor2B = 22
motor2PWM = 17



car = Robot(left=(motor2A, motor2B),right=(motor1A,motor1B))


car.forward()
sleep(10)
car.stop()
