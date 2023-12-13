import multiprocessing
import lights
import buttons
import time
import boto3
import os
import pygame
from decimal import Decimal
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.getenv('AWS_ACCESS_KEY')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('REGION')
dynamodb_table = os.getenv('TABLE_NAME')
dynamodb_table_id = 'dance-til-you-pi-id'

def light_process(queue):
    result = lights.main()
    queue.put(result)

def button_process(queue):
    result = buttons.main()
    queue.put(result)

def multiplier(buttonTS, lightTS, nextLightTS):
    reaction = buttonTS - lightTS
    lightTime = nextLightTS - lightTS
    # return 0.8 + 0.2 * (lightTime - reaction) / lightTime
    return 1 - abs((lightTS + nextLightTS) / 2 - buttonTS)

def calculateScore(light_result, button_result):
    # light_result = [{'ts': 1, 'color': 'RED'}, {'ts': 2, 'color': 'GREEN'}, {'ts': 3, 'color': 'YELLOW'}, {'ts': 4, 'color': 'GREEN'}, {'ts': 5, 'color': 'BLUE'}, {'ts': 7, 'color': 'PURPLE'}]
    # button_result = [{'ts': 1.5, 'color': 'RED'}, {'ts': 1.8, 'color': 'GREEN'}, {'ts': 3.5, 'color': 'YELLOW'}, {'ts': 4.5, 'color': 'GREEN'}, {'ts': 5.5, 'color': 'BLUE'}]

    total = 0

    button_index = 0
    
    for light_index in range(len(light_result) - 1):
        # print("light index:", light_index)
        lightTS = light_result[light_index]["ts"]
        lightColor = light_result[light_index]["color"]
        nextLightTS = light_result[light_index + 1]["ts"]
        
        if button_index >= len(button_result):
            break

        buttonTS = button_result[button_index]["ts"]

        buttonPressed = False

        while button_index < len(button_result):
            buttonTS = button_result[button_index]["ts"]

            if buttonTS >= lightTS and buttonTS < nextLightTS: # in the light window

                if not buttonPressed:
                    # print("in not buttonPresssed")
                    buttonColor = button_result[button_index]["color"]
                    if buttonColor == lightColor:
                        total += multiplier(buttonTS, lightTS, nextLightTS)
                    buttonPressed = True

                    # print("current light ts: " + str(lightTS))
                    # print("used button ts: " + str(buttonTS))
                    # print("next light ts: " + str(nextLightTS))
            
            if buttonTS >= nextLightTS:
                break
            
            button_index += 1
            # print("button index:", button_index)
            # print("button index: " + str(button_index))

            # print("while loop")
        
        # print("for loop")
    
    return total / (len(light_result) - 1)

def get_next_id():
    id_table = dynamodb.Table(dynamodb_table_id)
    response = id_table.update_item(
        Key={'table_name': 'dance-til-you-pi-scores'},
        UpdateExpression='SET id = id + :val',
        ExpressionAttributeValues={':val': 1},
        ReturnValues='UPDATED_NEW'
    )
    return response['Attributes']['id']

if __name__ == "__main__":
    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    table = dynamodb.Table(dynamodb_table)
    
    pygame.mixer.init()
    pygame.mixer.music.load("pimusic.mp3")

    name = input("Enter player name: ")
    print()
    print("Welcome,", name + "!")
    print("Press the buttons to the beat of the song!")
    print()
    time.sleep(1)
    
    pygame.mixer.music.play()
    
    print("Game starting in 3 seconds...")
    time.sleep(1)
    print("Game starting in 2 seconds...")
    time.sleep(1)
    print("Game starting in 1 seconds...")
    time.sleep(1)
    print("GO!")

    result_queue = multiprocessing.Queue()

    light_proc = multiprocessing.Process(target=light_process, args=(result_queue,))
    button_proc = multiprocessing.Process(target=button_process, args=(result_queue,))

    time.sleep(8)

    light_proc.start()
    button_proc.start()

    light_proc.join()  # Wait for light process to finish
    button_proc.join()  # Wait for button process to finish

    # Retrieve results from the queue
    light_result = result_queue.get()
    button_result = result_queue.get()




    # print("Light result size:", len(light_result))
    # print("Button result size:", len(button_result))

    print("==========")
    score = round(calculateScore(light_result, button_result), 5) * 100
    print("score:", score)

    # do database st*ff here
    next_id = get_next_id()

    score_to_add = {
        'id': next_id,
        'name': name,
        'accuracy' : Decimal("{:.5f}".format(score))
    }

    # print("light:", light_result)
    # print("button:", button_result)

    try:
        response = table.put_item(Item=score_to_add)
        print("Your score has been added to the database. Check it out!")
    except Exception as e:
        print("Error adding item:", str(e))

