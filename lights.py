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
