import multiprocessing
import lights
import buttons
import time

def light_process(queue):
    result = lights.main()
    queue.put(result)

def button_process(queue):
    result = buttons.main()
    queue.put(result)

def calculateAccuracy(light_result, button_result):
    total = 0

    button_index = 0
    
    for light_index in range(len(light_result) - 1):
        if button_index >= len(button_result):
            break

        lightTS = light_result[light_index]["ts"]
        lightColor = light_result[light_index]["color"]
        nextLightTS = light_result[light_index + 1]["ts"]

        buttonTS = button_result[button_index]["ts"]

        buttonPressed = False

        while buttonTS >= lightTS and buttonTS < nextLightTS:
            buttonTS = button_result[button_index]["ts"]

            if not buttonPressed:
                print("in not buttonPresssed")
                buttonColor = button_result[button_index]["color"]
                if buttonColor == lightColor:
                    total += 1
                buttonPressed = True
            
            button_index += 1

            print("stuck")
        
        print("stuck2")
    
    print("accuracy:", total / len(light_result))

if __name__ == "__main__":
    result_queue = multiprocessing.Queue()

    light_proc = multiprocessing.Process(target=light_process, args=(result_queue,))
    button_proc = multiprocessing.Process(target=button_process, args=(result_queue,))

    light_proc.start()
    button_proc.start()

    light_proc.join()  # Wait for light process to finish
    button_proc.join()  # Wait for button process to finish

    # Retrieve results from the queue
    light_result = result_queue.get()
    button_result = result_queue.get()

    print("Light result:", light_result)
    print("Button result:", button_result)

    calculateAccuracy(light_result, button_result)
