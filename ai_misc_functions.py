import time
import pyKey as pk
import mouse
from pynput.keyboard import Controller, Key

keyboard = Controller()

class AIMiscFunctionsInvoker():

    tag = "[MISC]"

    def __init__(self):
        pass

    #type param msg in the minecraft chat
    def type_in_chat(self, msg):
        pk.pressKey("T")
        pk.releaseKey("T")

        msg = msg.lower()

        msg = list(msg)

        print(msg)
        
        time.sleep(1)

        for char in range(len(msg)):
            
            print(msg[char])

            msg[char] = msg[char].replace(" ", "SPACEBAR")
            
            

            pk.pressKey(msg[char])
            pk.releaseKey(msg[char])
            time.sleep(0.1)

        pk.pressKey("ENTER")
        pk.releaseKey("ENTER")
        
        


    
    #switch to a certain hotbar slot
    def switch_to_hotbar_slot(self, slot):
        
        possible_slots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        
        if (slot in possible_slots):
            pk.pressKey(str(slot))
            pk.releaseKey(str(slot))

        else:
            print("Cannot switch to slot \"{}\"!".format(str(slot)))
    


    def place_block(self):
        mouse.click("right")

        print("Placed block")




    def get_block(self):
        mouse.click("middle")

        print("Got block. Function only works in creative mode.")
        

        
