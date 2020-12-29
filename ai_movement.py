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
    def move_left(self, block_amount):
        pk.press(key="A",sec=block_amount / 4.317)

    #move right
    def move_right(self, block_amount):
        pk.press(key="D",sec=block_amount / 4.317)
    #move forward
    def move_forward(self,block_amount):
        pk.press(key="W",sec=block_amount / 4.317)
        
        
        


    #move backward
    def move_backward(self, block_amount):
        pk.press(key="S",sec=block_amount / 4.317)

    #sprint forward
    def sprint_fw(self, block_amount):
        pk.pressKey("LCTRL")
        pk.pressKey("W")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("LCTRL")
        pk.releaseKey("W")


    #sprint backward
    def sprint_bw(self, block_amount):
        pk.pressKey("LCTRL")
        pk.pressKey("S")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("LCTRL")
        pk.releaseKey("S")

    #sprint right forward
    def sprint_rfw(self, block_amount):
        pk.pressKey("LCTRL")
        pk.pressKey("W")
        pk.pressKey("D")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("LCTRL")
        pk.releaseKey("W")
        pk.releaseKey("D")

    #sprint right backward
    def sprint_rbw(self, block_amount):
        pk.pressKey("LCTRL")
        pk.pressKey("D")
        pk.pressKey("S")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("LCTRL")
        pk.releaseKey("D")
        pk.releaseKey("S")

    #sprint left forward
    def sprint_lfw(self,block_amount):
        pk.pressKey("LCTRL")
        pk.pressKey("W")
        pk.pressKey("A")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("LCTRL")
        pk.releaseKey("W")
        pk.releaseKey("A")

    #sprint left backward
    def sprint_lbw(self, block_amount):
        pk.pressKey("LCTRL")
        pk.pressKey("S")
        pk.pressKey("A")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("LCTRL")
        pk.releaseKey("S")
        pk.releaseKey("A")

    @staticmethod
    #getting all movement functions. for people who want to make their AI do different things
    def get_all_movement_functions(self):
        print("""move_left, move_right, move_backward, move_forward, sprint_fw, sprint_bw, sprint_rfw, sprint_rbw, sprint_lfw, sprint_lbw. All funcs take arg "block_amount".
            Arg is required.""")

    