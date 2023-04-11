import wiringpi
import time

pinIn = 1
pinOut = 0

wiringpi.wiringPiSetup()
wiringpi.pinMode(pinOut, 1)
wiringpi.pinMode(pinIn, 0)


def sendBurst():
    wiringpi.digitalWrite(pinOut, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(pinOut, 0)


def read():
        sendBurst()

        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while wiringpi.digitalRead(pinIn) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while wiringpi.digitalRead(pinIn) == 1:
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        print(str(round(distance, 2))+ "cm")
        time.sleep(0.5)
        return round(distance, 2)

if __name__ == "__main__":
     read()