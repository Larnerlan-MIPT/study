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