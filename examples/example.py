from wlgamepad import WLGamepad
import RPi.GPIO as GPIO
import time

# initilize controller
controller = WLGamepad()

# setup communication with controller
controller.setup_controller()

try:
    while True:
        # read pressed keys and coordinates from stick
        state = controller.read_controller()
        # print values
        print(  f"Buttons: {state['buttons']} | \t\t"
                f"Sticks: {state['sticks']} | ")
        time.sleep(0.1)
except KeyboardInterrupt:
    # cleanup communication
    GPIO.cleanup()
