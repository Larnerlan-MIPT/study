import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac + leds, GPIO.OUT)
GPIO.setup([troyka], GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup([comp], GPIO.IN)
GPIO.output(dac + leds, 0)

flag = 1
num = 0
mask = 0x80


def dac_write(num):
    mask_dac = 0x80
    bin_num = []
    while mask_dac:
        k = 0
        if mask_dac & num:
            k = 1
        mask_dac >>= 1
        bin_num.append(k)
    GPIO.output(dac, bin_num)


def decimal2binary(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]


def alg1():
    for i in range(0, 256):
        num = decimal2binary(i)
        # print(i*3.3/255, " V")
        GPIO.output(dac, num)
        time.sleep(0.0007)

        if GPIO.input(comp) == 1:
            # print(i*3.3/256, " V")
            break
    return i


def alg2():
    val = 0
    for i in range(0, 8):
        val += 2 ** (7 - i)
        # print(i*3.3/255, " V")
        GPIO.output(dac, decimal2binary(val))
        time.sleep(0.0007)

        if GPIO.input(comp) == 1:
            # print(i*3.3/256, " V")
            val -= 2 ** (7 - i)
    return val


try:
    print("1, 2?")
    inp = int(input())
    while True:
        leds_num = [0 for i in range(8)]
        if inp == 1:
            num = alg1()
        elif inp == 2:
            num = alg2()

        print(num * 3.3 / 256, " V")
        time.sleep(0.001)
        GPIO.output(dac, decimal2binary(num))
        time.sleep(0.001)
        counter = 7
        while num > 0:
            leds_num[counter] = 1
            num -= 32
            counter -= 1
        GPIO.output(leds, leds_num)
finally:
    GPIO.output(dac, 0)
    print("dead")
    print(Exception.type())
