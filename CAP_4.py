# first
import RPi.GPIO as GPIO
import time
import sys

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)
flag = 1

#try:
try:
    while flag:
        try: 
            num = input()
            if num == 'q':
                break

            num = int(num)
            
            if num < 0 or num > 255:
                print('0 < ... < 255')
                break

        except ValueError:
            print('not Z')
            num = 0
        except Exception:
            print('bad num')
            num = 0
        

        # except num > 255:
        #     print('Bad num')

        mask = 0x80
        bin_num = []
        while mask:
            k = 0
            if mask&num: 
                k = 1
            mask >>= 1
            bin_num.append(k)
        print(bin_num, num*3.3/256, " V")
        GPIO.output(dac, bin_num)
    print("flag is done")
    time.sleep(5000)

finally:
    GPIO.output(dac, 0)    
    # GPIO.setup()

# second

import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)
flag = 1
period = 1 # in seconds
delay = period/10
deriv = 1
level = 127



def decimal2binary(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]
        

try:
    while flag:
        try:
            level += deriv
            if level > 255 or level < 0:
                deriv = -1*deriv
                level += deriv
            time.sleep(delay)
        except:
            print("Nope", type(Exception))
            num = 0
        print(int(level), "{:.2f}".format(int(level)*3.3/256), 'V')
        GPIO.output(dac, decimal2binary(level))
    print("flag is done")
    time.sleep(5000)
finally:
    print("Everything is done")
    GPIO.output(dac, 0)
  
#third

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
