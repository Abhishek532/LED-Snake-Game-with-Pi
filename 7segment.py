import RPi.GPIO as IO
import time
DISPLAY = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(25,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(27,IO.OUT)
IO.setup(17,IO.OUT)
IO.setup(4,IO.OUT)
IO.setup(24,IO.OUT)
IO.setup(23,IO.OUT)
def PORT(pin):
    if(pin&0x01 == 0x01):
        IO.output(25,1)
    else:
        IO.output(25,0)
    if(pin&0x02 == 0x02):
        IO.output(22,1)
    else:
        IO.output(22,0)
    if(pin&0x04 == 0x04):
        IO.output(27,1)
    else:
        IO.output(27,0)
    if(pin&0x08 == 0x08):
        IO.output(17,1)
    else:
        IO.output(17,0)
    if(pin&0x10 == 0x10):
        IO.output(4,1)
    else:
        IO.output(4,0)
    if(pin&0x20 == 0x20):
        IO.output(24,1)
    else:
        IO.output(24,0)
    if(pin&0x40 == 0x40):
        IO.output(23,1)
    else:
        IO.output(23,0)
for i in range(2):
    for x in range(10):
        pin = DISPLAY[x]
        PORT(pin)
        time.sleep(1)
