import pyautogui
import pydirectinput
from time import sleep

ok=1

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
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
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
        if(pyautogui.locateOnScreen('tre.png',confidence=.6)):
            ok=1
        else:
            ok=0
        if(ok==1):
            miscalamijloc()
        if(ok==1):
            miscabarastanga()
        if(ok==1):
            miscabaradreapta()
        if(ok==0):
            sleep(DELAY_BETWEEN_COMMANDS)
            pydirectinput.keyDown('1')
            

def miscalamijloc():
        pyautogui.click(x=953 ,y=671,duration=0.2)
def miscabarastanga():
        pyautogui.dragTo(825 , 666,duration=0.2)
def miscabaradreapta():
        pyautogui.dragTo(1094 , 670,duration=0.3)
        


if __name__ == "__main__":
    main()