import network
from machine import Pin, PWM
from microdot import send_file, Microdot
from motorController import MotorController

# Initialise the WLAN interface as an Access Point
wlan = network.WLAN(network.AP_IF)
wlan.config(ssid="AlexGaveUp6")
wlan.config(security=wlan.SEC_OPEN)
# wlan.config(password="1234567890")
wlan.active(True)

# The Pico W will automatically use a default IP (usually 192.168.4.1)
if wlan.active():
    print('Access Point created successfully')
    status = wlan.ifconfig()
    print(status)
else:
    raise RuntimeError('Access Point creation failed')

app = Microdot()

@app.get("/")
def index(request):
    return send_file("index.html")

@app.get("/htmx.js")
def htmx(request):
    return send_file("htmx.js")

@app.get("/style.css")
def css(request):
    return send_file("style.css")



# Car-Control Endpoints
motors = MotorController(16, 17, 15, 14, 13)

forwardLED = Pin(1, Pin.OUT)
backLED = Pin(2, Pin.OUT)

def ledsOff():
    forwardLED.off()
    backLED.off()

spkr = PWM(Pin(3))


@app.post("/forward")
def forward(request):
    spkr.freq(1000)
    spkr.duty_u16(65535//2)
    backLED.off()
    forwardLED.on()
    motors.forward()

    print("forwards")
    return "forward"

@app.post("/stop")
def stop(request):
    spkr.duty_u16(0)
    ledsOff()
    motors.stop()

    print("stop")
    return "stop"

@app.post("/back")
def back(request):
    spkr.freq(500)
    spkr.duty_u16(65535//2)
    forwardLED.off()
    backLED.on()
    motors.back()
    
    print("back")
    return "back"

@app.post("/left")
def left(request):
    spkr.duty_u16(0)
    ledsOff()
    motors.left()

    print("left")
    return "left"

@app.post("/right")
def right(request):
    spkr.duty_u16(0)
    ledsOff()
    motors.right()

    print("right")
    return "right"

app.run(port=80, debug=True)