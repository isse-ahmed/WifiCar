from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO

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

app = Flask(__name__, template_folder="templates")

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    data = request.get_json()

    leftJoystickUD = round(float(data.get('leftJoystickUD')),2)
    rightJoystickLR = round(float(data.get('rightJoystickLR')),2)
    
    moveMotors(leftJoystickUD,rightJoystickLR)
    print(leftJoystickUD)
    #print(rightJoystickLR)

    # Process the data and prepare a response
    response_data = {'result': 'Data processed successfully'}

    # Return a JSON response
    return jsonify(response_data)


def convertFloat(value):
    # Convert the value to a positive integer in the range 0-100
    positive_value = abs(int(value * 100))
    
    return positive_value


def moveMotors(speedMotor,directionMotor):
    
    if(speedMotor<-0.05):
        print(f"less than 0, value is {speedMotor}, dutyCycle is {convertFloat(speedMotor)}")
        GPIO.output(MOTOR1A,0)
        GPIO.output(MOTOR1B,1)
        MOTOR1PWM.ChangeDutyCycle(convertFloat(speedMotor))
    elif(speedMotor>0.05):
        print(f"less greater 0, value is {speedMotor}, dutyCycle is {convertFloat(speedMotor)}")
        GPIO.output(MOTOR1A,1)
        GPIO.output(MOTOR1B,0)
        MOTOR1PWM.ChangeDutyCycle(convertFloat(speedMotor))
    else:
        print(f"is 0, value is {speedMotor}, dutyCycle is {convertFloat(speedMotor)}")
        GPIO.output(MOTOR1A,0)
        GPIO.output(MOTOR1B,0)
        MOTOR1PWM.ChangeDutyCycle(0)
        
        
    if(directionMotor<-0.05):
        print(f"less than 0, value is {directionMotor}, dutyCycle is {convertFloat(directionMotor)}")
        GPIO.output(MOTOR2A,0)
        GPIO.output(MOTOR2B,1)
        MOTOR2PWM.ChangeDutyCycle(convertFloat(directionMotor))
    elif(directionMotor>0.05):
        print(f"less greater 0, value is {directionMotor}, dutyCycle is {convertFloat(directionMotor)}")
        GPIO.output(MOTOR2A,1)
        GPIO.output(MOTOR2B,0)
        MOTOR2PWM.ChangeDutyCycle(convertFloat(directionMotor))
    else:
        print(f"is 0, value is {directionMotor}, dutyCycle is {convertFloat(directionMotor)}")
        GPIO.output(MOTOR2A,0)
        GPIO.output(MOTOR2B,0)
        MOTOR2PWM.ChangeDutyCycle(0)
    
