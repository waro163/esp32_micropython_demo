from machine import ADC,Pin

adc = ADC(Pin(32,Pin.IN,Pin.PULL_DOWN))
print(adc.read())

# ADC.ATTN_0DB: 0dB 衰减，最大输入电压为 1.00v - 这是默认配置
# ADC.ATTN_2_5DB: 2.5dB 衰减，最大输入电压约为 1.34v
# ADC.ATTN_6DB: 6dB 衰减，最大输入电压约为 2.00v
# ADC.ATTN_11DB: 11dB 衰减，最大输入电压约为 3.6v
# set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.atten(ADC.ATTN_11DB)

# ADC.WIDTH_9BIT: 9 位数据
# ADC.WIDTH_10BIT: 10 位数据
# ADC.WIDTH_11BIT: 11 位数据
# ADC.WIDTH_12BIT: 12 位数据 - 这是默认配置
# set 9 bit return values (returned range 0-511)
# adc.width(ADC.WIDTH_9BIT)

# read value using the newly configured attenuation and width
import time
while True:
    print(adc.read())
    time.sleep(2)
