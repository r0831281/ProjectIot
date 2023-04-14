#pins 15, 13
import wiringpi
import time

wiringpi.wiringPiSetup()
wiringpi.softPwmCreate(15, 0, 100)
wiringpi.softPwmCreate(13, 0, 100)

def forward():
    wiringpi.softPwmWrite(15, 55)
    wiringpi.softPwmWrite(13, 0)

def backward():
    wiringpi.softPwmWrite(15, 0)
    wiringpi.softPwmWrite(13, 100)


def stop():
    wiringpi.softPwmWrite(15, 0)
    wiringpi.softPwmWrite(13, 0)


def reset():
     backward()
     time.sleep(2.8)
     forward()
     time.sleep(2.8)
     stop()

if __name__ == "__main__":
        reset()
