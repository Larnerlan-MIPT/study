import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup([troyka], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup([comp], GPIO.IN)
GPIO.output(dac, 0)

flag = 1
num = 0

def decimal2binary(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]


def main():
    for i in range(0, 256):
        num = decimal2binary(i)
        #print(i*3.3/255, " V")
        GPIO.output(dac, num)
        time.sleep(0.0007)

        if GPIO.input(comp) == 1:
            print(i*3.3/256, " V")
            break

try:
    while True:
        main()
finally:
    GPIO.output(dac, 0)

