import machine as ma
import time
import ssd1306

i2c = ma.I2C(0)#scl=Pin(18),sda=Pin(19)

oled_width=128
oled_high = 64
oled = ssd1306.SSD1306_I2C(oled_width,oled_high,i2c)

# 8*8 汉字：我
me = [0x2a,0x68,0xff,0x24,0x76,0x2c,0x22,0x63]

def out(x, y):
    for line in range(len(me)):
        data = bin(me[line]).lstrip("0b")
        length = len(data)
        data = "0"*(8-length)+data
        for i in range(8):
            oled.pixel(x+i,y+line,int(data[i]))
    oled.show()

out(0,0)
out(123,0)
oled.show()
time.sleep_ms(600)
#oled.scroll(-4,0)
oled.show()


#oled.text("Hello World!",0,0)
#oled.show()