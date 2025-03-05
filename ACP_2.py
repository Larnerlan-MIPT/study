# import RPi.GPIO as GPIO
# import time

# dac = [8, 11, 7, 1, 0, 5, 12, 6]
# comp = 14
# troyka = 13
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(dac, GPIO.OUT)
# GPIO.setup([troyka], GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup([comp], GPIO.IN)
# GPIO.output(dac, 0)

# flag = 1
# num = 0
# mask = 0x80

# def dac_write(num):
#     mask_dac = 0x80
#     bin_num = []
#     while mask_dac:
#         k = 0
#         if mask_dac&num:
#            k = 1
#         mask_dac >>= 1
#         bin_num.append(k)
#     GPIO.output(dac, bin_num)


# try:
#     while flag:
#         while mask:
#             num |= mask
#             dac_write(num)
#             time.sleep(0.1)
#             if GPIO.input(comp):
#                 num ^= mask
#             mask >>= 1
#             # print(num*3.3/256, " V")
#         print(num*3.3/256, " V")
#         time.sleep(1)
#         dac_write(0)
#         num = 0
#         time.sleep(1)
#         mask = 0x80

#     print("flag is done")
#     time.sleep(5000)

# finally:
#     GPIO.output(dac, 0)
#     print("dead")
#     print(Exception.type())


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


# n = [128, 64, 32, 16, 8, 4, 2, 1]

def main():
    val = 128
    # if i == 8:
    #     return val

    # val += numbers[i]

    # bin_val = decimal2binary(val)
    # GPIO.output(dac, bin_val)

    # time.sleep(0.1)
    # if GPIO.input(comp) == 1:
    #     val -= numbers[i]
    #     return val

    # return main(i + 1, val)
    # bin_val = decimal2binary(val)
    # GPIO.output(dac, bin_val + n[0])
    # time.sleep(0.01)

    GPIO.output(dac, decimal2binary(val))
    if GPIO.input(comp) == 0:
        val += 128

    else:

    time.sleep(0.01)
    GPIO.output(dac, decimal2binary(val + 64))
    if GPIO.input(comp) == 0:
        val += 64

    time.sleep(0.01)
    GPIO.output(dac, decimal2binary(val + n[2]))
    if GPIO.input(comp) == 0:
        val += n[2]

    time.sleep(0.01)
    GPIO.output(dac, decimal2binary(val + n[3]))
    if GPIO.input(comp) == 0:
        val += n[3]

    time.sleep(0.01)
    GPIO.output(dac, decimal2binary(val + n[4]))
    if GPIO.input(comp) == 0:
        val += n[4]

    time.sleep(0.01)
    GPIO.output(dac, decimal2binary(val + n[5]))
    if GPIO.input(comp) == 0:
        val += n[5]

    time.sleep(0.01)
    GPIO.output(dac, decimal2binary(val + n[6]))
    if GPIO.input(comp) == 0:
        val += n[6]

    time.sleep(0.01)
    GPIO.output(dac, decimal2binary(val + n[7]))
    if GPIO.input(comp) == 0:
        val += n[7]

    return val

    val = 0
    for i in range(0, 8):
        val += 2 ** (7 - i)
        # print(i*3.3/255, " V")
        GPIO.output(dac, decimal2binary(val))
        time.sleep(0.01)

        if GPIO.input(comp) == 1:
            # print(i*3.3/256, " V")
            val -= 2 ** (7 - i)
    return val


try:
    while True:
        a = main()
        print(a * 3.3 / 255, 'V')
finally:
    GPIO.output(dac, 0)

