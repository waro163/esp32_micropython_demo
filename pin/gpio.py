from machine import Pin

p0 = Pin(0, Pin.IN, Pin.PULL_UP)

p2 = Pin(2, Pin.OUT)
p2.off()