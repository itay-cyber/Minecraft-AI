import sys
import os
import time
import psutil

def checkIfProcessRunning(processName):
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




class MinecraftAI:

    tag = "[MAIN]"

    def __init__(self, movement, attributes_tracker, misc_functions_invoker):
        self.movement = movement
        self.attributes_tracker = attributes_tracker
        self.misc_funcs = misc_functions_invoker
        self.minecraft_running = False

        print("{} AI INIT".format(self.tag))
    

        #currently only works on windows :(
        
        if (sys.platform == "win32"):
            if (checkIfProcessRunning("javaw.exe")):
                print("{} Program detected that Minecraft's main java process is running".format(self.tag))
                print("{} Continue with the program? 1/0: ".format(self.tag))

                oneOrZero = int(input())

                if (oneOrZero == 1):
                    self.minecraft_running = True
                    
                    secs = int(input("{} Starting the program.. Please say how much secs of countdown you want: ".format(self.tag)))

                    print("{} The program will start in {} seconds.".format(self.tag, str(secs)))
                    time.sleep(secs)
                    self.main()

                elif (oneOrZero == 0):
                    self.minecraft_running = False
                    print("{} Terminating...".format(self.tag))
                    exit(1)
                else:
                    print("{} Input not accepted. Please write 1 or 0.".format(self.tag))
                    exit(1)
            
            else:
                print("{} Minecraft might not be running on your computer. Please launch Minecraft. Without it, the program cannot continue".format(self.tag))
                self.minecraft_running = True
                exit(1)

        else:
            print("{} Minecraft launch check could not be made. ".format(self.tag))
            secs = int(input("{} Starting the program.. Please say how much secs of countdown you want: ".format(self.tag)))

            print("{} The program will start in {} seconds.".format(self.tag, str(secs)))

                
                

        
    def main(self):
        if (self.minecraft_running):
            print("{} Executing main sequence of actions...".format(self.tag))

        else:
            print("{} Minecraft is not running right now. Terminating...".format(self.tag))
            quit(1)
            