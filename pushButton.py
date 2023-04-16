import wiringpi

resetButton = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(resetButton, 0)
#test reset button
def read():
    while True:
        if wiringpi.digitalRead(resetButton):
            print('active hi')
        else:
            print('acitve low')
if __name__ = "__main__":
    read()
