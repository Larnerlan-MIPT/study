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