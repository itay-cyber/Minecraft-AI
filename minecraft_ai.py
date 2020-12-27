from pynput import mouse
import keyboard
import time
import pyautogui
import pyKey

#reference to mouse
mouse_obj = mouse.Controller()


#jump
def jump():
    pyKey.pressKey(key="SPACEBAR")
    pyKey.releaseKey(key="SPACEBAR")


#move left
def move_left(hold_time):
    keyboard.press("a")
    time.sleep(hold_time)
    keyboard.release("a")

#move right
def move_right(hold_time):
    keyboard.press("d")
    time.sleep(hold_time)
    keyboard.release("d")

#move forward
def move_forward(hold_time):
    keyboard.press("w")
    time.sleep(hold_time)
    keyboard.release("w")

#move backward
def move_backward(hold_time):
    keyboard.press("s")
    time.sleep(hold_time)
    keyboard.release("s")

#type param msg in the minecraft chat
def type_in_chat(msg):
    keyboard.press_and_release("t")
    time.sleep(0.1)
    keyboard.write(msg)
    time.sleep(0.1)
    keyboard.press_and_release("enter")

#sprint forward
def sprint_fw(hold_time):
    keyboard.press("ctrl+w")
    time.sleep(hold_time)
    keyboard.release("ctrl+w")

#sprint backward
def sprint_bw(hold_time):
    keyboard.press("ctrl+s")
    time.sleep(hold_time)
    keyboard.release("ctrl+s")

#sprint right forward
def sprint_rfw(hold_time):
    keyboard.press("ctrl+w+d")
    time.sleep(hold_time)
    keyboard.release("ctrl+w+d")

#sprint right backward
def sprint_rbw(hold_time):
    keyboard.press("ctrl+d+a")
    time.sleep(hold_time)
    keyboard.release("ctrl+d+a")

#sprint left forward
def sprint_lfw(hold_time):
    keyboard.press("ctrl+w+a")
    time.sleep(hold_time)
    keyboard.release("ctrl+w+a")

#sprint left backward
def sprint_lbw(hold_time):
    keyboard.press("ctrl+s+a")
    time.sleep(hold_time)
    keyboard.release("ctrl+s+a")

    



time.sleep(10)

sprint_fw(4)

time.sleep(1)

sprint_bw(4)

time.sleep(1)

jump()

time.sleep(1)

type_in_chat("Completed")

