import sys
import os
import time






class MinecraftAI:
    def __init__(self, movement, attributes_tracker, misc_functions_invoker):
        self.movement = movement
        self.attributes_tracker = attributes_tracker
        self.misc_funcs = misc_functions_invoker
        self.minecraft_running = False

        print("AI INIT")
    

        #currently only works on windows :(
        
        if (sys.platform == "win32"):
            if (self.misc_funcs.checkIfProcessRunning("javaw.exe")):
                print("Program detected that Minecraft's main java process is running")
                print("Continue with the program? 1/0: ")

                oneOrZero = int(input())

                if (oneOrZero == 1):
                    self.minecraft_running = True
                    
                    secs = int(input("Starting the program.. Please say how much secs of countdown you want: "))

                    print("The program will start in {} seconds.".format(str(secs)))
                    time.sleep(secs)
                    self.main()

                elif (oneOrZero == 0):
                    self.minecraft_running = False
                    print("Terminating...")
                    exit(1)
                else:
                    print("Input not accepted. Please write 1 or 0.")
                    exit(1)
            
            else:
                print("Minecraft might not be running on your computer. Please launch Minecraft. Without it, the program cannot continue")
                self.minecraft_running = True
                exit(1)
                
                

        
    def main(self):
        if (self.minecraft_running):
            print("Executing main sequence of actions...")

        else:
            print("Minecraft is not running right now. Terminating...")
            quit(1)
            
        
    