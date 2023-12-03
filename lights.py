import pigpio
import time
import random

# Set GPIO pins for R, G, B
PIN_R = 23
PIN_G = 24
PIN_B = 25

# Connect to the pigpio daemon
pi = pigpio.pi()

# Set initial PWM values to 0
pi.set_PWM_dutycycle(PIN_R, 0)
pi.set_PWM_dutycycle(PIN_G, 0)
pi.set_PWM_dutycycle(PIN_B, 0)

def set_color(r, g, b):
    # Normalize values to the range 0-255
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Set PWM duty cycles for R, G, B
    pi.set_PWM_dutycycle(PIN_R, 255 - r)
    pi.set_PWM_dutycycle(PIN_G, 255 - g)
    pi.set_PWM_dutycycle(PIN_B, 255 - b)

# setting the RGB values for red, yellow, gren, and blu
colors = [[255, 0, 0], [255, 80, 0], [0, 255, 0], [0, 0, 255]]
colorNames = ["red", "yellow", "green", "blue"]
prevColor = -1

for i in range(0, 30):
    rand = random.randrange(4)
    while rand == prevColor:
        rand = random.randrange(4)

    color = colors[rand]
    set_color(color[0], color[1], color[2])
    ts = time.time()
    
    # print(ts, colorNames[rand])
    
    time.sleep(random.uniform(0.4, 1.2))
    prevColor = rand
    
# Allow some time for the color to be visible (adjust as needed)
# time.sleep(2)

pi.set_PWM_dutycycle(PIN_R, 255)
pi.set_PWM_dutycycle(PIN_G, 255)
pi.set_PWM_dutycycle(PIN_B, 255)
time.sleep(1)

# Clean up GPIO
pi.stop()
