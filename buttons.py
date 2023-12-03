import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for buttons
RED_PIN = 17
# YELLOW_PIN = 17
# GREEN_PIN = 22
BLUE_PIN = 4

# Set up GPIO pins as inputs with pull-down resistors
GPIO.setup(RED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(YELLOW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(GREEN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BLUE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button_callback(channel):
    print(f"Button {channel} pressed")

# Add event detection for each button
GPIO.add_event_detect(RED_PIN, GPIO.FALLING, callback=lambda channel: button_callback(1), bouncetime=200)
# GPIO.add_event_detect(YELLOW_PIN, GPIO.FALLING, callback=lambda channel: button_callback(2), bouncetime=200)
# GPIO.add_event_detect(GREEN_PIN, GPIO.FALLING, callback=lambda channel: button_callback(3), bouncetime=200)
# GPIO.add_event_detect(BLUE_PIN, GPIO.FALLING, callback=lambda channel: button_callback(4), bouncetime=200)

try:
    print("Press Ctrl+C to exit")
    while True:
        time.sleep(1)  # Keep the program running

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()
