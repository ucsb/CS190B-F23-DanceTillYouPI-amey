import RPi.GPIO as GPIO
import time

# Set GPIO pins for R, G, B
PIN_R = 23
PIN_G = 24
PIN_B = 25

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up PWM for each color
GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_G, GPIO.OUT)
GPIO.setup(PIN_B, GPIO.OUT)

# Set PWM frequency (Hz)
PWM_FREQ = 100

# Create PWM instances for R, G, B
pwm_r = GPIO.PWM(PIN_R, PWM_FREQ)
pwm_g = GPIO.PWM(PIN_G, PWM_FREQ)
pwm_b = GPIO.PWM(PIN_B, PWM_FREQ)

def set_color(r, g, b):
    # Normalize values to the range 0-100
    r = max(0, min(100, r))
    g = max(0, min(100, g))
    b = max(0, min(100, b))

    # Map normalized values to PWM duty cycles (0-100)
    duty_cycle_r = (r / 100.0) * 100
    duty_cycle_g = (g / 100.0) * 100
    duty_cycle_b = (b / 100.0) * 100

    # Set PWM duty cycles for R, G, B
    pwm_r.ChangeDutyCycle(duty_cycle_r)
    pwm_g.ChangeDutyCycle(duty_cycle_g)
    pwm_b.ChangeDutyCycle(duty_cycle_b)

# Example: Set color to Red (100% intensity)
set_color(0, 0, 255)

# Allow some time for the color to be visible (adjust as needed)
time.sleep(2)

# Clean up GPIO
pwm_r.stop()
pwm_g.stop()
pwm_b.stop()
GPIO.cleanup()