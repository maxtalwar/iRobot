import time
from pycreate2 import Create2

def drive(left, right):
    bot.drive_direct(left, right)
    time.sleep(2)

def turn(amount=1):
    bot.drive_direct(100*amount, -100*amount)
    time.sleep(2)

def start():
    bot.start()
    bot.safe()

def stop_bot():
    bot.drive_stop()

# port = "/dev/cu.usbserial-DN028709" <- on Most Mac Devices
# port = "COM1", "COM2", "COM3", or "COM4" <- on most windows devices. You can find the connected devices in device manager under ports, one of the device names should be the one you choose here (eg COM3)
port = "/dev/cu.usbserial-DN028709"
bot = Create2(port)