import time
import keyboard as kb


class AIMiscFunctionsInvoker():
    def __init__(self):
        pass

    #type param msg in the minecraft chat
    def type_in_chat(self, msg):
        kb.press_and_release("t")
        time.sleep(0.1)
        kb.write(msg)
        time.sleep(0.1)
        kb.press_and_release("enter")