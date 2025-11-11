from machine import Pin

class MotorController:
    def __init__(self, rightForwardPin, rightBackPin, leftForwardPin, leftBackPin, enablePin):
        self.rightForward = Pin(rightForwardPin, Pin.OUT)
        self.rightBack = Pin(rightBackPin, Pin.OUT)
        self.leftForward = Pin(leftForwardPin, Pin.OUT)
        self.leftBack = Pin(leftBackPin, Pin.OUT)
        self.enable = Pin(enablePin, Pin.OUT)
    
    def forward(self):
        self.enable.off()
        self.rightBack.off()
        self.leftBack.off()
        self.rightForward.on()
        self.leftForward.on()
        self.enable.on()
    
    def back(self):
        self.enable.off()
        self.rightForward.off()
        self.leftForward.off()
        self.rightBack.on()
        self.leftBack.on()
        self.enable.on()
    
    def right(self):
        self.enable.off()
        self.rightBack.off()
        self.leftForward.off()
        self.leftBack.on()
        self.rightForward.on()
        self.enable.on()

    def left(self):
        self.enable.off()
        self.leftBack.off()
        self.rightForward.off()
        self.leftForward.on()
        self.rightBack.on()
        self.enable.on()
    
    def stop(self):
        self.enable.off()
        self.leftBack.off()
        self.rightForward.off()
        self.rightBack.off()
        self.leftForward.off()
