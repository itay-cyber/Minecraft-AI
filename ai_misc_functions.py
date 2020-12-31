import time
import pyKey as pk
import mouse


class AIMiscFunctionsInvoker():

    tag = "[MISC]"

    def __init__(self):
        pass

    #type param msg in the minecraft chat
    def type_in_chat(self, msg):

        msg.replace(" ", "")
        
        pk.pressKey("T")
        pk.releaseKey("T")
        time.sleep(0.1)
        pk.sendSequence(msg)
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
        

        
