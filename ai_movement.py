import keyboard as kb 
import time


class AIMovement():
    def __init__(self):
        print("Movement class initialized")

    #@ccm767 can u try to implement jump function i tried but couldn't find a way.

    #move left
    def move_left(self, hold_time):
        kb.press("a")
        time.sleep(hold_time)
        kb.release("a")

    #move right
    def move_right(self, hold_time):
        kb.press("d")
        time.sleep(hold_time)
        kb.release("d")

    #move forward
    def move_forward(self, hold_time):
        kb.press("w")
        time.sleep(hold_time)
        kb.release("w")

    #move backward
    def move_backward(self, hold_time):
        kb.press("s")
        time.sleep(hold_time)
        kb.release("s")

    #sprint forward
    def sprint_fw(self, hold_time):
        kb.press("ctrl+w")
        time.sleep(hold_time)
        kb.release("ctrl+w")

    #sprint backward
    def sprint_bw(self, hold_time):
        kb.press("ctrl+s")
        time.sleep(hold_time)
        kb.release("ctrl+s")

    #sprint right forward
    def sprint_rfw(self, hold_time):
        kb.press("ctrl+w+d")
        time.sleep(hold_time)
        kb.release("ctrl+w+d")

    #sprint right backward
    def sprint_rbw(self, hold_time):
        kb.press("ctrl+d+a")
        time.sleep(hold_time)
        kb.release("ctrl+d+a")

    #sprint left forward
    def sprint_lfw(self, hold_time):
        kb.press("ctrl+w+a")
        time.sleep(hold_time)
        kb.release("ctrl+w+a")

    #sprint left backward
    def sprint_lbw(self, hold_time):
        kb.press("ctrl+s+a")
        time.sleep(hold_time)
        kb.release("ctrl+s+a")

    @staticmethod
    #getting all movement functions. for people who want to make their AI do different things
    def get_all_movement_functions(self):
        print("""move_left, move_right, move_backward, move_forward, sprint_fw, sprint_bw, sprint_rfw, sprint_rbw, sprint_lfw, sprint_lbw. All funcs take arg "hold_time".
            Arg is required.""")

    