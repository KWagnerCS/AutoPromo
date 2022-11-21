# Open blue stack with OS
# open transact app
# enter UFL
# click on ufl
# click on guest email
# enter random name
# enter random email
# enter random password
# Click on apply promo
# add promo
# log out
# repeat for x times

import arrayNames
import os 
import time
import random
import string
from pynput.keyboard import Key, Controller, Listener
from pynput.mouse import Button, Controller as MouseController
# from tkinter import *

def on_press(key):
    if key == 'x':
        exit()

def generatePassword(length = 15):
    alphaNumerical = string.digits + string.ascii_letters
    return ''.join(random.choice(alphaNumerical) for i in range(length)) + random.choice(string.digits) + random.choice(string.ascii_uppercase)

def generateName():
    return random.choice(arrayNames.names)

def generateEmail(length = 15):
    alphaNumerical = string.digits + string.ascii_letters
    return ''.join(random.choice(alphaNumerical) for i in range(length)) + '@' + ''.join(random.choice(alphaNumerical) for i in range(6)) + '.com'

def main():
    # ask for input

    print()
    print(" _______  __   __  _______  _______  _______  ______    _______  __   __  _______ ")
    print("|   _   ||  | |  ||       ||       ||       ||    _ |  |       ||  |_|  ||       |")
    print("|  |_|  ||  | |  ||_     _||   _   ||    _  ||   | ||  |   _   ||       ||   _   |")
    print("|       ||  |_|  |  |   |  |  | |  ||   |_| ||   |_||_ |  | |  ||       ||  | |  |")
    print("|       ||       |  |   |  |  |_|  ||    ___||    __  ||  |_|  ||       ||  |_|  |")
    print("|   _   ||       |  |   |  |       ||   |    |   |  | ||       || ||_|| ||       |")
    print("|__| |__||_______|  |___|  |_______||___|    |___|  |_||_______||_|   |_||_______|")
    print()

    promoCode = input("Enter your promo code: ")
    print()
    loopAmount = int(input("Enter number of times to repeat: "))
    print()
    isOpen = input("Is BlueStacks already open? Y/N: ")
    print()

    # Create controllers
    keyboard = Controller()
    mouse = MouseController()
    timeBetween = 0.5

    '''
    #while(True):
    #    print(mouse.position)
    #    time.sleep(2)

    #with Listener(on_press=on_press) as listener:
    #    listener.join()
    '''

    # opens bluestacks emulator
    if(isOpen == 'Y'):
        os.startfile('C:\Program Files\BlueStacks_nxt\HD-Player.exe')
        print("BlueStacks launched...")
        time.sleep(timeBetween)
    else:
        os.startfile('C:\Program Files\BlueStacks_nxt\HD-Player.exe')
        print("BlueStacks launched, now loading...")
        time.sleep(15)

    # fullscreen bluestacks
    keyboard.press(Key.f11)
    keyboard.release(Key.f11)
    print("BlueStacks loaded.")
    print()
    time.sleep(timeBetween)

    # click on transact
    # 1711, 177
    mouse.position = (1711, 177)
    mouse.click(Button.left, 1)
    time.sleep(4)
    
    '''
    # LOGGOUT
    mouse.position = (685, 46)
    mouse.click(Button.left, 1)
    time.sleep(timeBetween)
    
    mouse.position = (727, 665)
    mouse.click(Button.left, 1)
    time.sleep(timeBetween)

    mouse.position = (1144, 599)
    mouse.click(Button.left, 1)
    time.sleep(2)
    '''

    print("Promos to complete: ", loopAmount)

    for i in range(loopAmount):
        # 716, 95
        mouse.position = (716, 95)
        mouse.click(Button.left, 1)
        time.sleep(timeBetween)
        # type ufl
        keyboard.type("ufl")
        time.sleep(timeBetween)
        # 725, 147
        mouse.position = (725, 147)
        mouse.click(Button.left, 1)
        time.sleep(timeBetween)
        # 960, 1048
        mouse.position = (960, 1048)
        mouse.click(Button.left, 1)
        time.sleep(timeBetween)
        # 930, 910
        mouse.position = (930, 910)
        mouse.click(Button.left, 1)
        time.sleep(timeBetween)

        # input login
        keyboard.type(generateName())
        time.sleep(timeBetween)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(timeBetween)
        keyboard.type(generateName())
        time.sleep(timeBetween)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(timeBetween)
        keyboard.type(generateEmail())
        time.sleep(timeBetween)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(timeBetween)
        keyboard.type(generatePassword())
        time.sleep(timeBetween)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(2)

        # 960, 1048
        mouse.position = (960, 1048)
        mouse.click(Button.left, 1)
        time.sleep(timeBetween)
        # 683, 45
        mouse.position = (683, 45)
        mouse.click(Button.left, 2)
        time.sleep(timeBetween)
        # 732, 359
        mouse.position = (732, 359)
        mouse.click(Button.left, 1)
        time.sleep(timeBetween)
        # input promo
        keyboard.type(promoCode)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)

        # LOGGOUT
        # 732, 595
        mouse.position = (732, 595)
        mouse.click(Button.left, 1)
        time.sleep(timeBetween)
        # 1146, 602
        mouse.position = (1146, 602)
        mouse.click(Button.left, 1)
        time.sleep(2)

        print("Promo #", i+1, " completed.")

    print("Promos completed, now closing...")
    # close bluestacks
    os.system('TASKKILL /F /IM HD-Player.exe')


if __name__ == "__main__":
    main()