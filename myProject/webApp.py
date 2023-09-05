from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    data = request.get_json()

    leftJoystickUD = data.get('leftJoystickUD')
    rightJoystickLR = data.get('rightJoystickLR')

    print(leftJoystickUD)
    print(rightJoystickLR)

