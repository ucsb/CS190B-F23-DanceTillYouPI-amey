![unnamed](https://github.com/ucsb/CS190B-F23-DanceTillYouPI-amey/assets/59379464/dfe7d4a1-00a3-4749-b369-83a046063571)

# CS190B-F23-DanceTillYouPI-amey

Dance Till You Pi is a play on the phrase, “Dance till you die”. Inspired by games we love playing in arcades, such as "Dance Dance Revolution," or DDR, this is a mini version of such rhythm/timing games! Dance Till You Pi game rewards players with good coordination, reaction time, and a musical ear. React to the colored light flash and press the matching colored buttons on every beat! In contrast to typical DDR games, which are large and expensive, our version is much more compact and can be enjoyed from the comfort of your room!

Link to the repo which holds our Python scoreboard site app, which should be ran locally: https://github.com/ucsb/CS190B-F23-DanceTillYouPI_site-amey

## System/Hardware Requirements

- Hardware
  - Raspberry Pi 3+ with the correct materials wired according to the circuit design in `CS190B_F23_DanceTillYouPI.pdf`
  - Speaker connected to the RPi through the 3.5mm audio input port
- Additional system tools
  - Python 3.9+

## Installation and the first step

The following should be done on the RPi:

```
git clone https://github.com/ucsb/CS190B-F23-DanceTillYouPI-amey.git
cd ./CS190B-F23-DanceTillYouPI-amey
sudo apt-get update
sudo apt-get install pigpio
sudo apt-get install python3-rpi.gpio
sudo apt-get install python3-pygame
sudo pigpiod
python3 ./game_controller.py
```

### Environment variables

Environment variables for a dynamoDB to store the leaderboard must be set prior to running the game.

- `AWS_ACCESS_KEY`
  - An AWS access key associated with an IAM account.
- `AWS_SECRET_ACCESS_KEY`
  - The secret key associated with the access key. This is essentially the "password" for the access key.
- `REGION`
  - The AWS Region to send the request to.
- `TABLE_NAME`
  - The name of the DynamoDB table to store the leaderboard.
