import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
pins = [21, 17]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(pins, GPIO.OUT)
GPIO.output(dac, 0)
GPIO.output(pins, 0)
GPIO.setup(20, GPIO.IN)
flag = 1
pul = 0
period = 5 # in seconds
delay = period/512
pin = GPIO.PWM(21, 1000)
pin.start(0)

try:
    while flag:
        try:
            print("DC in percents")
            num = float(input())
            print(num)
            if num > 100 or num < 0:
                pul = 1
        except:
            print("Bad num")
            print(type(Exception))
            num = 0
        if pul:
            num = 0
            tim = time.time()
            while time.time() < tim + 10:
                num += flag
                if num > 100 or num < 0:
                    flag -= 2*flag
                    num += flag
                pin.ChangeDutyCycle(num)
                time.sleep(delay)
            flag = 1
            num = 0
            pul = 0
        else:
            print(num)
            pin.ChangeDutyCycle(num)  
        # GPIO.output(pins, 1)
        # time.sleep(period*num)
        # GPIO.output(pins, 0)
        # time.sleep(period*(1-num))
    print("flag is done")
    time.sleep(5000)

finally:
    GPIO.output(dac, 0)    
    # GPIO.setup()