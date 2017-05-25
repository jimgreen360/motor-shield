import PiMotor
import time

       #"""Procedure to test LED Arrows on Motor Hat"""



def run():


            a = PiMotor.Arrow(1)
            b = PiMotor.Arrow(2)
            c = PiMotor.Arrow(3)
            d = PiMotor.Arrow(4)
            a.on()
            time.sleep(1)
            a.off()
            time.sleep(1)
            b.on()
            time.sleep(1)
            b.off()
            time.sleep(1)
            c.on()
            time.sleep(1)
            c.off()
            time.sleep(1)
            d.on()
            time.sleep(1)
            d.off()
            time.sleep(1)
try:
    
    while True:    
        run()
    
except KeyboardInterrupt:
    print("\nExiting Motor Shield Testing\n")

