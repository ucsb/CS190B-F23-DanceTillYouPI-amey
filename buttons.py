import RPi.GPIO as GPIO
import time

def initialize():
    # Set GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Define GPIO pins for buttons
    RED_PIN = 6
    YELLOW_PIN = 13
    GREEN_PIN = 19
    BLUE_PIN = 26

    # Set up GPIO pins as inputs with pull-down resistors
    GPIO.setup(RED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(YELLOW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(GREEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(BLUE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    colors = ["RED", "YELLOW", "GREEN", "BLUE"]
    results = []

    return RED_PIN, YELLOW_PIN, GREEN_PIN, BLUE_PIN, colors, results

def button_callback(channel, colors, results):
    ts = time.time()
    results.append({"ts": ts, "color": colors[channel]})
    
    print(f"{colors[channel]} Button pressed at time {ts}")

def setup_button_events(RED_PIN, YELLOW_PIN, GREEN_PIN, BLUE_PIN, colors, results):
    # Add event detection for each button
    GPIO.add_event_detect(RED_PIN, GPIO.RISING, callback=lambda channel: button_callback(0, colors, results), bouncetime=200)
    GPIO.add_event_detect(YELLOW_PIN, GPIO.RISING, callback=lambda channel: button_callback(1, colors, results), bouncetime=200)
    GPIO.add_event_detect(GREEN_PIN, GPIO.RISING, callback=lambda channel: button_callback(2, colors, results), bouncetime=200)
    GPIO.add_event_detect(BLUE_PIN, GPIO.RISING, callback=lambda channel: button_callback(3, colors, results), bouncetime=200)

def main():
    RED_PIN, YELLOW_PIN, GREEN_PIN, BLUE_PIN, colors, results = initialize()
    setup_button_events(RED_PIN, YELLOW_PIN, GREEN_PIN, BLUE_PIN, colors, results)
    
    try:
        print("Press Ctrl+C to exit")
        time.sleep(25)  # Keep the program running

    except KeyboardInterrupt:
        pass 

    finally:
        # Clean up GPIO on program exit
        GPIO.cleanup()

    return results

if __name__ == "__main__":
    main()

#import RPi.GPIO as GPIO
# import time

# # Set GPIO mode to BCM
# GPIO.setmode(GPIO.BCM)

# # Define GPIO pins for buttons
# RED_PIN = 6
# YELLOW_PIN = 13
# GREEN_PIN = 19
# BLUE_PIN = 26

# # Set up GPIO pins as inputs with pull-down resistors
# GPIO.setup(RED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(YELLOW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(GREEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(BLUE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# colors = ["RED", "YELLOW", "GREEN", "BLUE"]

# def button_callback(channel):
#     ts = time.time()
#     print(f"{colors[channel]} Button pressed at time {ts}")

# # Add event detection for each button
# GPIO.add_event_detect(RED_PIN, GPIO.RISING, callback=lambda channel: button_callback(0), bouncetime=200)
# GPIO.add_event_detect(YELLOW_PIN, GPIO.RISING, callback=lambda channel: button_callback(1), bouncetime=200)
# GPIO.add_event_detect(GREEN_PIN, GPIO.RISING, callback=lambda channel: button_callback(2), bouncetime=200)
# GPIO.add_event_detect(BLUE_PIN, GPIO.RISING, callback=lambda channel: button_callback(3), bouncetime=200)

# try:
#     print("Press Ctrl+C to exit")
#     while True:
#         time.sleep(1)  # Keep the program running

# except KeyboardInterrupt:
#     pass 

# finally:
#     # Clean up GPIO on program exit
#     GPIO.cleanup()
