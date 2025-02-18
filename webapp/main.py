from flask import Flask, request, render_template
from gpiozero import Buzzer
import time

#Crear un objeto
app = Flask(__name__)
buzzer = Buzzer(18)

@app.route("/")
def home():
    
    return render_template("temp_buzzer2.html")

@app.route("/buzzer_control",methods=["POST"])
def buzzer_control():
    accion = request.form.get('action')
    if accion=="on":
        buzzer.on()
    elif accion == "off":
        buzzer.off()

if __name__ == "__main__":
    app.run()
