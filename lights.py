import usb.core
import usb.util
import time

# Define USB device parameters
VENDOR_ID = 0x0424  # Replace with your USB device's vendor ID
PRODUCT_ID = 0x9514  # Replace with your USB device's product ID
INTERFACE = 0

# USB control request parameters
REQUEST_TYPE = usb.util.CTRL_OUT | usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_RECIPIENT_DEVICE
REQUEST = 0x09
VALUE = 0x0200
INDEX = 0x00
print("finding now")
# Find the USB device
dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if dev is None:
    raise ValueError("USB device not found.")

try:
    print("dev: ", dev)

    # Detach the kernel driver if active
    if dev.is_kernel_driver_active(INTERFACE):
        dev.detach_kernel_driver(INTERFACE)

    # Set the active configuration. The device may have multiple configurations.
    dev.set_configuration()

    # Access the USB interface
    usb.util.claim_interface(dev, INTERFACE)

    # Example: Turn on the LED
    print("Turning on the LED...")
    dev.ctrl_transfer(REQUEST_TYPE, REQUEST, VALUE, INDEX, b"\x01")

    # Wait for a moment
    time.sleep(2)

    # Example: Turn off the LED
    print("Turning off the LED...")
    dev.ctrl_transfer(REQUEST_TYPE, REQUEST, VALUE, INDEX, b"\x00")

finally:
    # Release the USB interface
    usb.util.release_interface(dev, INTERFACE)

    # Attach the kernel driver if it was detached
    dev.attach_kernel_driver(INTERFACE) if dev.is_kernel_driver_active(INTERFACE) else None


# import RPi.GPIO as GPIO
# import time

# # Pin configuration - Modify based on your actual setup
# red_pin = 27    # GPIO pin connected to the red channel of the RGB LED strip
# green_pin = 17  # GPIO pin connected to the green channel of the RGB LED strip
# blue_pin = 22   # GPIO pin connected to the blue channel of the RGB LED strip

# # Setup GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(red_pin, GPIO.OUT)
# GPIO.setup(green_pin, GPIO.OUT)
# GPIO.setup(blue_pin, GPIO.OUT)

# # Helper function to set the color
# def set_color(red_value, green_value, blue_value):
#     GPIO.output(red_pin, red_value)
#     GPIO.output(green_pin, green_value)
#     GPIO.output(blue_pin, blue_value)

# try:
#     while True:
#         # Red
#         print("Red")
#         set_color(GPIO.HIGH, GPIO.LOW, GPIO.LOW)  # Turn on red, turn off others
#         time.sleep(1)

#         # Green
#         print("Green")
#         set_color(GPIO.LOW, GPIO.HIGH, GPIO.LOW)  # Turn on green, turn off others
#         time.sleep(1)

#         # Blue
#         print("Blue")
#         set_color(GPIO.LOW, GPIO.LOW, GPIO.HIGH)  # Turn on blue, turn off others
#         time.sleep(1)

# except KeyboardInterrupt:
#     print("\nExiting...")
#     GPIO.cleanup()  # Clean up GPIO on Ctrl+C exit