from machine import Pin

p0 = Pin(0, Pin.IN, Pin.PULL_UP)
p2 = Pin(2, Pin.OUT)
p2.off()

def ledon(p):
    if p2.value():
        p2.off()
    else:
        p2.on()

def ledoff(p):
    p2.off()

p0.irq(trigger=Pin.IRQ_FALLING, handler = ledon)

#p0.irq(trigger=Pin.IRQ_RISING, handler = ledoff)

while True:
    pass