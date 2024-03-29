12/14
- Completed final report and readme file


12/12
- Successfully controlled audio output to speaker through Python script on RPi
- Synchronized light flashes to short clip from “Blinding Lights” by the Weeknd
- Modified scoring system
- Constructed physical game enclosure and decorations
- Completed final presentation + demo


12/9
- Amey Updates: Finished IOT component
  - Game results stored into dynamodb table and displayed on local html file


12/6/23
- We are considering splitting the remaining work into 3 parts
  - Managing Audio/Visual aspect 
  - Syncing button presses and light flashes
  - IOT aspect → storing accuracy / points and sending to device

Audio/Visual requirements - JUSTIN
  - 60 seconds of light flashes synchronized to a song
  - Song must be played through connected speaker

Syncing button presses and light flashes - ANUSHKA
  - Record timestamps for light flashes
  - Check if timestamp for button press is between the timestamps for the light flashes
  - record/track correct presses and output the overall accuracy

IOT/display table data - AMEY
  - Sending accuracy data into dynamo DB tables
  - Display data on html server/file (query DB table)
  - Show current score and top 5 scores all time


12/3/23
- Attached and sensed buttons successfully
- Program that reads in button presses


12/2/23
- Created program to have the lights flash random colors
- Worked on attaching/ sensing buttons, could not get it to work because we need resistors


11/28/23
- Went to OH and got Lights.py to work
  - Figured out how to connect the wires on the Led strip to the pi
- Next meeting, will try to get the lights to flash random colors and program the buttons


11/18/23
- Started writing Python script for Raspberry Pi to control LEDs and detect button input
- Confused how to control LED strip through USB, might have to control them with GPIO instead, unless we can figure out how to use py usb module to control through USB


11/16/23
- Breadboard + wires picked up
- Buttons and LED strips acquired → we have all hardware necessary
- We’ll meet up Saturday 4pm - 5:45pm to start putting things together
- First prototype
  - Buttons directly onto breadboard
  - Figure out how to control LEDs with Pi
  - Have LED’s flash red blue green yellow in random order
  - Click buttons according to LED Flash
- Will get cardboard after prototyping to better hold the parts


11/10/23
- Buttons Arrived - Amey
- Messaged instructors about breadboard + wire rentals - Justin
- Also an option to buy a breadboard kit off amazon 


11/9/23
Updates:
- LED light strips arrived - Anushka


11/3/23
Updates:
- Talked to ULA during section, mini version of DDR pad will be more feasible
- Wiring the led strip to the pi: https://www.youtube.com/watch?app=desktop&v=aNlaj1r7NKc

Questions:
- Do we want to sync music with light flashes on the pad?
- Might hardcode values for a 30-45 second audio clip for the demo

Items we have:
- Raspberry PI
- JBL Speaker for audio

Items to buy:
- 4 buttons (need arrow key stickers to put on them) ~ 25pc $10
- Mini LED strip
- 2 breadboards

Items to buy in the future:
- Case that’ll go over breadboards, which buttons will sit on and LEDs will wrap around


11/2/23
Brainstorm:
- IOT aspect
  - We want to be able to display the scoreboard and send the scores to other people / an online database
- Need to buy
  - Force sensitive resistor pads 
- Questions
  - Do we want to make a mini version of the DDR pad so it works with 2 fingers
    - Pros: makes it easier to build, cheaper
    - Cons: tiny, probably not as fun
  - Meeting times:
    - Tuesday and Thursday 11-12
- Basic Timeline:
  - Week 5 (10/29 - 11/4)
    - Finalize project idea (small finger board vs large feet board)
    - Before next meeting, 
  - Week 6 (11/5 - 11/11)
    - Purchase parts
  - Week 7 (11/12 - 11/18)
  - Week 8 (11/19 - 11/25)
  - Week 9 (11/26 - 12/2)
  - Week 10 (12/3 - 12/9)
  - Week 11 (12/10 - 12/14)
    - Due Thursday, Dec 14

Online Tutorials for DDR
https://www.youtube.com/watch?v=nXjj9IXUaA4


10/18/23
No Blockers

Team Initial Brainstorm:
Diy Link: https://imgur.com/gallery/vjYcK 
Surface ideas
Yoga mat
Wood board?
Rubber mat

Force sensitive pads: https://core-electronics.com.au/guides/force-sensitive-pads-raspberry-pi/\\

What if we made a mini finger-style version - Justin

General components:
Board
Needs sensors
Leds for arrows
Wires 

Randomized timing / lighting up arrows

Basic single pad diagram: https://imgur.com/AK6RJxN
