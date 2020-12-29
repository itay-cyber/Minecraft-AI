import time
import pyKey as pk
import psutil

class AIMiscFunctionsInvoker():
    def __init__(self):
        print("Functions class invoked")

    #type param msg in the minecraft chat
    def type_in_chat(self, msg):
        pk.press(key="T", sec=0.1)

        time.sleep(0.1)

        pk.sendSequence(seq=msg)

        time.sleep(0.1)
        
        pk.press(key="ENTER")



    def checkIfProcessRunning(self, processName):
        '''
        Check if there is any running process that contains the given name processName.
        '''
        #Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;