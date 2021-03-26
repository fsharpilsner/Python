
#Python implementation of USB One/Two channel Relay RS232 Serial Controller:

#https://www.kmtronic.com/index.php?route=product/product&product_id=52
#https://sigma-shop.com/manuals/usb_two_relay_manual.pdf


import serial
import time
import os
from struct import pack, unpack, calcsize


# 9600+,n+,8+,1+
# ON Command :  "FF 01 01"
# OFF Command : "FF 01 00"

#Windows
usb = serial.Serial(port='COM4', baudrate=9600,
                    bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

#Linux
#usb = serial.Serial(port='/dev/ttyUSB1', baudrate=9600,
#                    bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

#usb.open()
print(usb.isOpen)

print("connected to: " + usb.portstr)

# sends the following bytes: 255 1 0

values = bytearray([255, 1, 1])
usb.write(values)
#usb.write(serialcmd_ON)

print('send ON')

time.sleep(3)

values = bytearray([255, 1, 0])
usb.write(values)
print('send OFF')

usb.close()

#running = True
# try:
#    while running:
#        line = usb.readline()
#        mosq.publish("sensors/cc128/raw", line)
# except usb.SerialException:
#    running = False
