from machine import Pin

# http://docs.micropython.org/en/latest/library/machine.Pin.html

# Pin.IN, Pin.OUT, Pin.OPEN_DRAIN, Pin.ALT, Pin.ALT_OPEN_DRAIN
# None, Pin.PULL_UP, Pin.PULL_DOWN
p0 = Pin(0, Pin.IN, Pin.PULL_UP)

p0.mode()
p0.mode(Pin.IN)

p0.on()
p0.off()

p2 = Pin(2, Pin.OUT)
p2.off()