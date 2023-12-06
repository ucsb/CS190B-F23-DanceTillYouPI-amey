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
    b = 0
    # todo
    print("accuracy:")

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

    # calculateAccuracy(light_result, button_result)
