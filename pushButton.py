import wiringpi

resetButton = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(resetButton, 0)

def read():
    while True:
        if wiringpi.digitalRead(resetButton):
            print('active hi')
        else:
            print('acitve low')

read()