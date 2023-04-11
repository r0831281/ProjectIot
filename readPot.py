import wiringpi
import time

wiringpi.wiringPiSetup() 

def ActivateADC ():
    wiringpi.digitalWrite(pin_CS_adc, 0)       # Actived ADC using CS
    time.sleep(0.000005)
def DeactivateADC():
    wiringpi.digitalWrite(pin_CS_adc, 1)       # Deactived ADC using CS
    time.sleep(0.000005)
def readadc(adcnum): 
    if ((adcnum > 7) or (adcnum < 0)): 
        return -1 
    revlen, recvData = wiringpi.wiringPiSPIDataRW(1, bytes([1,(8+adcnum)<<4,0]))
    time.sleep(0.000005)
    adcout = ((recvData[1]&3) << 8) + recvData[2] 
    return adcout  
#Setup


pin_CS_adc = 16                                 #We will use w16 as CE, not the 
wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin_CS_adc, 1)            # Set pin to mode 1 ( OUTPUT )     
wiringpi.wiringPiSPISetupMode(1, 0, 500000, 0)  #(channel, port, speed, mode)


def readPot():    
    ActivateADC()
    tmp0 = readadc(0) # read channel 0
    DeactivateADC()
    return tmp0

def readTemp():  
    ActivateADC()
    tmp1 = readadc(1) # read channel 1
    DeactivateADC()
    tempinC = (tmp1 * (3.3 /1023)) * 100
    print(str(tempinC), "tempinC")
    return round(tempinC, 2)

if __name__ == "__main__":
    while True:
        print(readPot())
        print(readTemp())
        time.sleep(1)