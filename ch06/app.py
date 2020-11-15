from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)


LED = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT, initial=GPIO.LOW)


@app.route("/")
def helloworld():
    return "hello world <button><a href='/led/on'>turn on</a></button> <button><a href='/led/off'>turn off</a></button>"

@app.route("/led/on")
def led_on():
    return "LED ON <button><a href='/led/on'>turn on</a></button> <button><a href='/led/off'>turn off</a></button>"

@app.route("/led/off")
def led_off():
    return "LED OFF<button><a href='/led/on'>turn on</a></button> <button><a href='/led/off'>turn off</a></button>"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP"

if __name__ == "__mail__":
    app.run(host="0.0.0.0")
    