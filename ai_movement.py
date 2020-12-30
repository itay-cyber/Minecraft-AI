import pyKey as pk
import time


"""

libs used: pyKey: https://github.com/andohuman/pyKey
psutil (pip3/pip install psutil)
time (builtin)

"""
"""

Created by https://www.github.com/itay-cyber
Created by https://www.github.com/ccm7676

"""



class AIMovement():

    tag = "[MOVEMENT]"

    def __init__(self):
        print("{} Movement class initialized".format(self.tag))

    #jump
    def jump(self):
        pk.pressKey("SPACEBAR")
        time.sleep(0.1)
        pk.releaseKey("SPACEBAR")

        print("{} Jumped".format(self.tag))
        

    #move left
    def move_left(self, block_amount):
        pk.pressKey("A")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("A")

        print("{} Moved left {} blocks".format(self.tag, block_amount))

        

    #move right
    def move_right(self, block_amount):
        pk.pressKey("D")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("D")

        print("{} Moved right {} blocks".format(self.tag, block_amount))

    #move forward
    def move_forward(self,block_amount):
        pk.pressKey("W")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("W")
        
        print("{} Moved forward {} blocks".format(self.tag, block_amount))
        
        


    #move backward
    def move_backward(self, block_amount):
        pk.pressKey("S")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("S")

        print("{} Moved backward {} blocks".format(self.tag, block_amount))

    #sprint forward
    def sprint_fw(self, block_amount):
        pk.pressKey("CTRL")
        pk.pressKey("W")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("CTRL")
        pk.releaseKey("W")

        print("{} Sprinted forward {} blocks".format(self.tag, block_amount))


    #sprint backward
    def sprint_bw(self, block_amount):
        pk.pressKey("CTRL")
        pk.pressKey("S")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("CTRL")
        pk.releaseKey("S")

        print("{} Sprinted backward {} blocks".format(self.tag, block_amount))

    #sprint right forward
    def sprint_rfw(self, block_amount):
        pk.pressKey("CTRL")
        pk.pressKey("W")
        pk.pressKey("D")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("CTRL")
        pk.releaseKey("W")
        pk.releaseKey("D")

        print("{} Sprinted in the right-forward direction {} blocks".format(self.tag, block_amount))

    #sprint right backward
    def sprint_rbw(self, block_amount):
        pk.pressKey("CTRL")
        pk.pressKey("D")
        pk.pressKey("S")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("CTRL")
        pk.releaseKey("D")
        pk.releaseKey("S")

        print("{} Sprinted in the right backward direction {} blocks".format(self.tag, block_amount))

    #sprint left forward
    def sprint_lfw(self,block_amount):
        pk.pressKey("CTRL")
        pk.pressKey("W")
        pk.pressKey("A")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("CTRL")
        pk.releaseKey("W")
        pk.releaseKey("A")

        print("{} Sprinted in the left-forward direction {} blocks".format(self.tag, block_amount))

    #sprint left backward
    def sprint_lbw(self, block_amount):
        pk.pressKey("CTRL")
        pk.pressKey("S")
        pk.pressKey("A")
        time.sleep(block_amount / 4.317)
        pk.releaseKey("CTRL")
        pk.releaseKey("S")
        pk.releaseKey("A")


        print("{} Sprinted in the left-backward direction {} blocks".format(self.tag, block_amount))
    @staticmethod
    #getting all movement functions. for people who want to make their AI do different things
    def get_all_movement_functions(self):
        print("""{} move_left, move_right, move_backward, move_forward, sprint_fw, sprint_bw, sprint_rfw, sprint_rbw, sprint_lfw, sprint_lbw. All funcs take arg "block_amount".
            Arg is required.""")

    
