import PiMotor
import time


def run():
    
    Ping = PiMotor.Sensor("ULTRASONIC",60)
    Ping.trigger()
    if Ping.Triggered:
        print("Boundry Breached")

try:
    
    while True:    
        run()
    
except KeyboardInterrupt:
    print("\nExiting Motor Shield Testing\n")    
