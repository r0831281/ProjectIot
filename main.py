import lcdtest
import DcMotor
import SonarReading
import stepper
import time
import wiringpi
import readPot
import requests
import stream

ubeacUrl = "http://orangetraptm.hub.ubeac.io/iotsmousetrap"
UID = "IotPi"
resetButton = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(resetButton, 0)
triggered = True
luikAfstand = 24
triggercounter = 0

lcdtest.putString('starting.....')
while True:
    try:
        if triggered:
            lcdtest.showDisarmed(triggercounter) 
            time.sleep(0.1)
            stepper.showLocked()
            time.sleep(0.01)
            if not wiringpi.digitalRead(resetButton):
                lcdtest.putString('resetting.....')
                time.sleep(0.02)
                stepper.unlock()
                DcMotor.backward()
                time.sleep(2.9)
                DcMotor.stop()
                time.sleep(1)
                stepper.reset()
                DcMotor.forward()
                time.sleep(2.8)
                DcMotor.stop()
                time.sleep(0.01)
                stream.stopStream()
                triggered = False
        else:
            temp = readPot.readTemp()
            print(temp, "temp")
            stepper.showUnlocked()
            readingPot = readPot.readPot()
            time.sleep(0.01)
            reading1 = SonarReading.read()
            time.sleep(0.01)
            reading2 = SonarReading.read()
            print('Distance reading', reading1)
            sens = readingPot/100
            sens = luikAfstand - sens
            time.sleep(0.01)
            lcdtest.showArmed(sens, temp)
            if (reading1 < sens) & (reading2 < sens):
                triggercounter += 1
                stream.startStream()
                data = {
                    "id": UID,
                    "sensors": [{
                    "id": "temperature",
                    "data": temp
                    },
                    {"id": "Counter",
                    "data" : triggercounter
                    },
                    {"id": "distance to trigger",
                     "data" : sens}]
                }
                r = requests.post(ubeacUrl, verify=False, json=data)
                stepper.trigger()
                time.sleep(1)
                stepper.lock()
                print("counter:", str(triggercounter))
                triggered = True
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        stream.stopStream()
        break