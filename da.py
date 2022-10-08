import pyautogui
import pydirectinput
from time import sleep

ok=0

DELAY_BETWEEN_COMMANDS = 1.00


def main():
    
    initializePyAutoGUI()
    countdownTimer()
    #reportMousePosition()
    cautapeecran()
    print("Gata barosane")

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    pyautogui.FAILSAFE = True


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

def holdKey(key, seconds=1.00):
    pyautogui.keyDown(key)
    sleep(seconds)
    pyautogui.keyUp(key)
    sleep(DELAY_BETWEEN_COMMANDS)


def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)
        
def cautapeecran(seconds=50):
    for i in range(0, seconds):
        if(pyautogui.locateOnScreen('tre.png',confidence=.5)):
           while(pyautogui.locateOnScreen('tre.png',confidence=.5)):
            miscalamijloc()
            miscabarastanga()
            miscabaradreapta()
        else:
            pydirectinput.keyDown('1')
            sleep(DELAY_BETWEEN_COMMANDS)
            
            

def miscalamijloc():
        pyautogui.click(x=953 ,y=671)
def miscabarastanga():
        pyautogui.dragTo(825 , 666,duration=0.1)
def miscabaradreapta():
        pyautogui.dragTo(1094 , 670,duration=0.1)


if __name__ == "__main__":
    main()