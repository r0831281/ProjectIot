# gpio pin 3,4,6,9
import wiringpi
import time

wiringpi.wiringPiSetup() 
coil1 = 9
coil2 = 6
coil3 = 4
coil4 = 3


wiringpi.pinMode(coil1, 1)
wiringpi.pinMode(coil2, 1)
wiringpi.pinMode(coil3, 1)
wiringpi.pinMode(coil4, 1)

gpiopins = [coil1, coil2, coil3, coil4]

step_sequence = list(range(0, 4))
step_sequence[0] = [gpiopins[0], gpiopins[1]]
step_sequence[1] = [gpiopins[1], gpiopins[2]]
step_sequence[2] = [gpiopins[2], gpiopins[3]]
step_sequence[3] = [gpiopins[0], gpiopins[3]]



def trigger():
    print("triggered")
    amount = 65
    while amount > 0:
        #do sequence for amount of steps
        for steps in step_sequence:
            for step in steps:
                wiringpi.digitalWrite(step, 1)
            time.sleep(0.002)
            for step in steps:
                wiringpi.digitalWrite(step, 0)
        amount -= 1

def lock():
    print('locking')
    lock = 130
    while lock > 0:
        #do sequence backwards for amount of steps
        for steps in step_sequence[::-1]:
            for step in steps:
                wiringpi.digitalWrite(step, 1)
            time.sleep(0.002)
            for step in steps:
                wiringpi.digitalWrite(step, 0)
        lock -= 1

def unlock():
    print('unlocking')
    lock = 130
    while lock > 0:
        for steps in step_sequence:
            for step in steps:
                wiringpi.digitalWrite(step, 1)
            time.sleep(0.002)
            for step in steps:
                wiringpi.digitalWrite(step, 0)
        lock -= 1
    
def reset():
    print("trigger reset")
    amount = 65
    while amount > 0:
        for steps in step_sequence[::-1]:
            for step in steps:
                wiringpi.digitalWrite(step, 1)
            time.sleep(0.003)
            for step in steps:
                wiringpi.digitalWrite(step, 0)
        amount -= 1



def showLocked():
    wiringpi.digitalWrite(coil4, 1)


def showUnlocked():
    wiringpi.digitalWrite(coil4, 0)

