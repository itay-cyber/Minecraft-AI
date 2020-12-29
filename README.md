# Minecraft-AI
A minecraft AI made by @itay-cyber and @ccm7676


USABLE FOR PLAYING AROUND AND HAVING A "HANDS-OFF" MINECRAFT EXPERIENCE


Steps:

1. Clone the repo (git clone or github desktop)
2. Cd into the downloaded directory
3. Launch Minecraft
4. Run the command "python start.py"
5. Follow the start process
6. Now your bot is set up. Go into "start.py" and change up the code for the AI to move, jump, or soon-to-be mine.



# Minecraft-AI Docs

ai.movement

The movement class for the AI. Contains functions that are below:

1. `ai.movement.move_forward(hold_time)`

This function takes param `hold_time`. This specifies the amount of time to hold the W key which is the forward moving key in Minecraft.

2. `ai.movement.move_backward(hold_time)`

This function works the same as `move_forward()` but is the func to make the AI move backwards in game.

3. `ai.movement.move_right(hold_time)`

Pretty much understandable by now.. 

4. `ai.movement.move_left(hold_time)`

5. `ai.movement.sprint_fw(hold_time)`

A function that works the same as `move_forward()` but sprints instead of moving (forward)

6. `ai.movement.sprint_bw(hold_time)`

Sprint backwards.

7. The static method `AIMovement.get_all_movement_functions`

Prints out all possible movement functions. 


ai.misc_functions

The miscellaneous functions class for the AI. Contains functions that are below:

1. `ai.misc_functions.type_in_chat(msg)`

A function to write a message into the Minecraft chat. Takes param `msg` which is the message to write.

2. Coming soon.

We are still working on the main functionality of the AI, so come back later to check out new features!

# !WARNING! MINECRAFT MUST BE LAUNCHED AND YOU MUST BE IN MINECRAFT FOR THE AI TO WORK PROPERlY!!!

