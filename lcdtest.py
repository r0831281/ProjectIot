import time
import wiringpi
import spidev
from ch7_ClassLCD import LCD
def ActivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 0)  # Actived LCD using CS
    time.sleep(0.000005)
def DeactivateLCD():
    wiringpi.digitalWrite(pin_CS_lcd, 1)  # Deactived LCD using CS
    time.sleep(0.000005)

PIN_OUT = {
    'SCLK':   14, # shared mcp3008
    'DIN':   11, # shared mcp3008
    'DC':   8,
    'CS':   7,  
    'RST':   10,
    'LED':   5,  # backlight
}
# pin 7cs
pin_CS_lcd = 7
wiringpi.wiringPiSetup()
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  # (channel, port, speed, mode)
wiringpi.pinMode(pin_CS_lcd, 1)  # Set pin to mode 1 ( OUTPUT )
ActivateLCD()
lcd_1 = LCD(PIN_OUT)
lcd_1.set_backlight(1)
DeactivateLCD()

def showArmed(sens, temp):
    ActivateLCD()
    lcd_1.clear()
    time.sleep(0.01)
    lcd_1.go_to_xy(0, 0)
    time.sleep(0.01)
    lcd_1.put_string("Armed")
    time.sleep(0.01)
    lcd_1.go_to_xy(2, 10)
    time.sleep(0.01)
    lcd_1.put_string("sens: " + str(round(24-sens)) + "/10")
    lcd_1.go_to_xy(4, 23)
    time.sleep(0.01)
    lcd_1.put_string("temp: " + str(round(temp, 1)) )
    lcd_1.refresh()
    DeactivateLCD()

def showDisarmed(counter):
    ActivateLCD()
    lcd_1.clear()
    lcd_1.go_to_xy(0, 0)
    time.sleep(0.01)
    lcd_1.put_string("Disarmed: press button")
    time.sleep(0.01)
    lcd_1.go_to_xy(2, 25)
    time.sleep(0.01)
    lcd_1.put_string("counter: " + str(counter))
    time.sleep(0.01)
    lcd_1.refresh()
    DeactivateLCD()

def putString(string):
    ActivateLCD()
    lcd_1.clear()
    lcd_1.set_backlight(1)
    lcd_1.go_to_xy(0, 0)
    time.sleep(0.01)
    lcd_1.put_string(string)
    time.sleep(0.01)
    lcd_1.refresh()
    time.sleep(0.01)
    DeactivateLCD()


if __name__ == "__main__":
    putString("srt")
    time.sleep(1)
    showArmed(1, 2)
    time.sleep(2)
    showDisarmed(3)
