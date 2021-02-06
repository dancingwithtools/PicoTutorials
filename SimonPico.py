# import machine, imports the Pico's functions and definitions
import machine
# imports time based functions
import utime

# imports random function gen
import random

#Wait time between button clicks
buttonWaitTime = 0.25
#Blink wait time
blinkWaitTime = 0.5
#BlinkCount for start and end
blinkCount = 3

#Global Level counters
currLevel = 1
currLevelSequence = []
levelSequence = []
ledColour = ['R','B','Y','G']
maxLevel = 5
GameStatus = 'WIN'

# Define LEDs
redLed    = machine.Pin(02, machine.Pin.OUT)
blueLed   = machine.Pin(03, machine.Pin.OUT)
yellowLed = machine.Pin(04, machine.Pin.OUT)
greenLed  = machine.Pin(05, machine.Pin.OUT)

# Define buttons
redButton    = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
blueButton   = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
yellowButton = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
greenButton  = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Variable Definitions
isNewGame = False

# indicator for game starting or ending, Blinks blinkCount times
def gameStart():
    for iCount in range(blinkCount):        
        redLed.value(1)
        blueLed.value(1)
        yellowLed.value(1)
        greenLed.value(1)
        utime.sleep(blinkWaitTime)
        redLed.value(0)
        blueLed.value(0)
        yellowLed.value(0)
        greenLed.value(0)
        utime.sleep(blinkWaitTime)

# Game status indicator
def gameWin():     
    greenLed.value(1)
    utime.sleep(blinkWaitTime)

def gameLost():     
    redLed.value(1)
    utime.sleep(blinkWaitTime)
        
# Create Level for the game
def createLevel (currLevel):    
    for icount in range(currLevel):
        levelSequence.append(random.choice(ledColour))
    return (levelSequence)

# Check Userinputs, Return true if the sequence is same as the random level generated
# Else returns false
def checkButtons (currLevel,currLevelSequence):
    iCount = 0
    print ("Current count : " , iCount)
    print ("currLevel : " , currLevel)
    while (iCount < currLevel):
        
        if redButton.value() == 1:            
            utime.sleep(buttonWaitTime)
            if currLevelSequence[iCount] == 'R' :
                iCount = iCount + 1         
            else:
                return False
            
        if blueButton.value() == 1:            
            utime.sleep(buttonWaitTime)
            if currLevelSequence[iCount] == 'B' :
                iCount = iCount + 1         
            else:
                return False
            
        if yellowButton.value() == 1:            
            utime.sleep(buttonWaitTime)
            if currLevelSequence[iCount] == 'Y' :
                iCount = iCount + 1         
            else:
                return False
            
        if greenButton.value() == 1:            
            utime.sleep(buttonWaitTime)
            if currLevelSequence[iCount] == 'G' :
                iCount = iCount + 1         
            else:
                return False
            
    # if all choices are correct then return True  
    return True

# Display the randomly generated sequence on the LEDs
def ledDisplay(currLevelSequence):
    iLen = len(currLevelSequence)
    for iCount in range(iLen):
        if currLevelSequence[iCount] == 'R' :
            redLed.value(1)
            utime.sleep(blinkWaitTime)
            redLed.value(0)
            utime.sleep(blinkWaitTime)
        if currLevelSequence[iCount] == 'B' :
            blueLed.value(1)
            utime.sleep(blinkWaitTime)
            blueLed.value(0)
            utime.sleep(blinkWaitTime)
        if currLevelSequence[iCount] == 'Y' :
            yellowLed.value(1)
            utime.sleep(blinkWaitTime)
            yellowLed.value(0)
            utime.sleep(blinkWaitTime)
        if currLevelSequence[iCount] == 'G' :
            greenLed.value(1)
            utime.sleep(blinkWaitTime)
            greenLed.value(0)
            utime.sleep(blinkWaitTime)
    
     

# Start the game with blinking lights
gameStart()

#Create levels
for iLevel in range(1,maxLevel+1):
    currLevelSequence.clear()
    currLevelSequence = createLevel(iLevel)    
    print (currLevelSequence)
    
    # Display the level in LEDs
    ledDisplay (currLevelSequence)
    
    if(checkButtons(iLevel,currLevelSequence)):
        pass
    else:
        GameStatus = 'LOST'
        break

#Final Game status
if GameStatus == 'LOST' :
    gameLost()
else:
    gameWin()
