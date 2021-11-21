from machine import Pin, PWM

# init
p2 = PWM(Pin(2))
# create and configure in one go
p2 = PWM(Pin(2), freq=20000, duty=512)

p2.freq()             # get current frequency (default 5kHz)
p2.freq(1000)         # set frequency

p2.duty()             # get current duty cycle (default 512, 50%)
p2.duty(200)          # set duty cycle

# disable pwm output
# turn off PWM on the pin
p2.deinit()