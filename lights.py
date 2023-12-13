import pigpio
import time
import random

# Set GPIO pins for R, G, B
PIN_R = 23
PIN_G = 24
PIN_B = 25

def initialize():
    # Connect to the pigpio daemon
    pi = pigpio.pi()

    # Set initial PWM values to 0
    pi.set_PWM_dutycycle(PIN_R, 0)
    pi.set_PWM_dutycycle(PIN_G, 0)
    pi.set_PWM_dutycycle(PIN_B, 0)
    
    return pi

def set_color(pi, r, g, b):
    # Normalize values to the range 0-255
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    # Set PWM duty cycles for R, G, B
    pi.set_PWM_dutycycle(PIN_R, 255 - r)
    pi.set_PWM_dutycycle(PIN_G, 255 - g)
    pi.set_PWM_dutycycle(PIN_B, 255 - b)

    return time.time()

# setting the RGB values for red, yellow, green, and blue
COLORS = [[255, 0, 0], [255, 80, 0], [0, 255, 0], [0, 0, 255]]
COLORNAMES = ["RED", "YELLOW", "GREEN", "BLUE"]

def showLight(pi, results, prevColor):
    rand = random.randrange(4)
    while rand == prevColor:
        rand = random.randrange(4)

    color = COLORS[rand]
    ts = set_color(pi, color[0], color[1], color[2])
    results.append({"ts": ts, "color": COLORNAMES[rand]})
    
    # print("Light", COLORNAMES[rand], "is flashing at time", ts)

    return results, rand

def main():
    pi = initialize()
        
    results = []
    prevColor = -1

    # === TIMING ===

    time.sleep(1.47)
    results, prevColor = showLight(pi, results, prevColor)
    for i in range(53):
        time.sleep(0.7)
        results, prevColor = showLight(pi, results, prevColor)

    # === END TIMING ===
        
    # Allow some time for the color to be visible (adjust as needed)
    # time.sleep(2)

    pi.set_PWM_dutycycle(PIN_R, 100)
    pi.set_PWM_dutycycle(PIN_G, 100)
    pi.set_PWM_dutycycle(PIN_B, 100)
    time.sleep(1)

    # Clean up GPIO
    pi.stop()

    results.append({"ts": results[-1]["ts"] + 0.7, "color": "PURPLE"})

    return results

if __name__ == "__main__":
    main()


# import pigpio
# import time
# import random

# # Set GPIO pins for R, G, B
# PIN_R = 23
# PIN_G = 24
# PIN_B = 25

# # Connect to the pigpio daemon
# pi = pigpio.pi()

# # Set initial PWM values to 0
# pi.set_PWM_dutycycle(PIN_R, 0)
# pi.set_PWM_dutycycle(PIN_G, 0)
# pi.set_PWM_dutycycle(PIN_B, 0)

# def set_color(r, g, b):
#     # Normalize values to the range 0-255
#     r = max(0, min(255, r))
#     g = max(0, min(255, g))
#     b = max(0, min(255, b))

#     # Set PWM duty cycles for R, G, B
#     pi.set_PWM_dutycycle(PIN_R, 255 - r)
#     pi.set_PWM_dutycycle(PIN_G, 255 - g)
#     pi.set_PWM_dutycycle(PIN_B, 255 - b)
#     return time.time()

# # setting the RGB values for red, yellow, gren, and blu
# colors = [[255, 0, 0], [255, 80, 0], [0, 255, 0], [0, 0, 255]]
# colorNames = ["red", "yellow", "green", "blue"]
# prevColor = -1

# for i in range(0, 15):
#     rand = random.randrange(4)
#     while rand == prevColor:
#         rand = random.randrange(4)

#     color = colors[rand]
#     ts = set_color(color[0], color[1], color[2])
    
#     print("Light", colorNames[rand], "is flashing at time", ts)
    
#     time.sleep(random.uniform(2, 3))
#     prevColor = rand
    
# # Allow some time for the color to be visible (adjust as needed)
# # time.sleep(2)

# pi.set_PWM_dutycycle(PIN_R, 255)
# pi.set_PWM_dutycycle(PIN_G, 255)
# pi.set_PWM_dutycycle(PIN_B, 255)
# time.sleep(1)

# # Clean up GPIO
# pi.stop()
