import pyKey as pk
import time


"""

Libs used: pyKey: https://github.com/andohuman/pyKey
Psutil
Time

"""


class AIMovement():
    def __init__(self):
        print("Movement class initialized")

    #jump
    def jump(self):
        pk.pressKey("SPACEBAR")
        time.sleep(0.1)
        pk.releaseKey("SPACEBAR")
        

    #move left
    def move_left(self, hold_time):
        pk.pressKey("A")
        time.sleep(hold_time)
        pk.releaseKey("A")

    #move right
    def move_right(self, hold_time):
        pk.pressKey("D")
        time.sleep(hold_time)
        pk.releaseKey("D")

    #move forward
    def move_forward(self, hold_time):
        pk.pressKey("W")
        time.sleep(hold_time)
        pk.releaseKey("W")


    #move backward
    def move_backward(self, hold_time):
        pk.pressKey("S")
        time.sleep(hold_time)
        pk.releaseKey("S")

    #sprint forward
    def sprint_fw(self, hold_time):
        pk.pressKey("CTRL")
        pk.pressKey("W")
        time.sleep(hold_time)
        pk.releaseKey("CTRL")
        pk.releaseKey("W")


    #sprint backward
    def sprint_bw(self, hold_time):
        pk.pressKey("CTRL")
        pk.pressKey("S")
        time.sleep(hold_time)
        pk.releaseKey("CTRL")
        pk.releaseKey("S")

    #sprint right forward
    def sprint_rfw(self, hold_time):
        pk.pressKey("CTRL")
        pk.pressKey("W")
        pk.pressKey("D")
        time.sleep(hold_time)
        pk.releaseKey("CTRL")
        pk.releaseKey("W")
        pk.releaseKey("D")

    #sprint right backward
    def sprint_rbw(self, hold_time):
        pk.pressKey("CTRL")
        pk.pressKey("D")
        pk.pressKey("S")
        time.sleep(hold_time)
        pk.releaseKey("CTRL")
        pk.releaseKey("D")
        pk.releaseKey("S")

    #sprint left forward
    def sprint_lfw(self, hold_time):
        pk.pressKey("CTRL")
        pk.pressKey("W")
        pk.pressKey("A")
        time.sleep(hold_time)
        pk.releaseKey("CTRL")
        pk.releaseKey("W")
        pk.releaseKey("A")

    #sprint left backward
    def sprint_lbw(self, hold_time):
        pk.pressKey("CTRL")
        pk.pressKey("S")
        pk.pressKey("A")
        time.sleep(hold_time)
        pk.releaseKey("CTRL")
        pk.releaseKey("S")
        pk.releaseKey("A")

    @staticmethod
    #getting all movement functions. for people who want to make their AI do different things
    def get_all_movement_functions(self):
        print("""move_left, move_right, move_backward, move_forward, sprint_fw, sprint_bw, sprint_rfw, sprint_rbw, sprint_lfw, sprint_lbw. All funcs take arg "hold_time".
            Arg is required.""")

    