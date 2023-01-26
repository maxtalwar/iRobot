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

port = "/dev/cu.usbserial-DN028709"
bot = Create2(port)