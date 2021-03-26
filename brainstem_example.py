

# Communicating with Acroname USB Hub:
# https://acroname.com/store/s77-usbhub-2x4?sku=S77-USBHUB-2X4

import brainstem
import time

# Create USBStem object
print ('\nCreating USBStem and connecting to first module found')
##stem = brainstem.stem.USBStem()
stem = brainstem.stem.USBHub3p()

#result = stem.discoverAndConnect(brainstem.link.Spec.USB, 0x00B18208)

result = stem.discoverAndConnect(brainstem.link.Spec.USB) 
print(result)

#Check error
if result == (Result.NO_ERROR):
    result = stem.system.getSerialNumber()
    
    print ("Connected to USBStem with serial number: 0x%08X" % result.value)

    #Flash the LED
    print ('Flashing the user LED\n')
    for i in range(1, 11):
        stem.system.setLED(i % 2)
        time.sleep(0.5)

else:
    print ("Could not connect to device\n")

result = stem.usb.setPortEnable(3)
if(result != brainstem.result.Result.NO_ERROR):
    print(' enabling failed with error %d' % result)

#Disconnect from device.
stem.disconnect()
