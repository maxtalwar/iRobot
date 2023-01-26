from pycreate2 import Create2
import time

if __name__ == "__main__":
    port = "/dev/cu.usbserial-DN028709"
    bot = Create2(port)

def drive(left, right):
    bot.drive_direct(left, right)
    time.sleep(2)

def turn(amount):
    bot.drive_direct(100*amount, -100*amount)
    time.sleep(2)

def start():
    bot.start()
    bot.full()

# start the robot
start()

# drive the robot
drive(left=100, right=100)

# turn the robot
turn(amount=1)

# stop the robot
bot.drive_stop()