# Minecraft-AI
A minecraft AI made by @itay-cyber and @ccm7676


USABLE FOR PLAYING AROUND AND HAVING A "HANDS-OFF" MINECRAFT EXPERIENCE


Steps:

1. Clone the repo (git clone or github desktop)
2. Cd into the downloaded directory
3. run the command `pip install -r requirements.txt`
4. Launch Minecraft
5. Run the command "python start.py"
6. Follow the start process
7. Now your bot is set up. Go into "start.py" and change up the code for the AI to move, jump, or soon-to-be mine.



# Minecraft-AI Docs

_ai.movement_

The movement class for the AI. Contains functions that are below:

1. `ai.movement.move_forward(block_amount)`

This function takes param `block_amount`. This specifies the amount of blocks to walk. Function to move forward in game.

2. `ai.movement.move_backward(block_amount)`

This function works the same as `move_forward()` but is the func to make the AI move backwards in game.

3. `ai.movement.move_right(block_amount)`

Function to move right in game. 

4. `ai.movement.move_left(block_amount)`

5. `ai.movement.sprint_fw(block_amount)`

A function that works the same as `move_forward()` but sprints instead of moving (forward)

6. `ai.movement.sprint_bw(block_amount)`

Sprint backwards.

7. The static method `AIMovement.get_all_movement_functions`

Prints out all possible movement functions. 


_ai.misc_functions_

The miscellaneous functions class for the AI. Contains functions that are below:

1. `ai.misc_functions.type_in_chat(msg)`

A function to write a message into the Minecraft chat. Takes param `msg` which is the message to write.

2. `ai.misc_functions.get_block()`

Function to middle-click the block being looked at and put it into hotbar

3. `ai.misc_functions.switch_to_hotbar_slot(slot)`

Function that switches to slot `slot` of your hotbar. Minimum number 1 largest number 9

4. `ai.misc_functions.place_block()`

Places a block at the block being looked at.

5. Coming soon.

We are still working on the main functionality of the AI, so come back later to check out new features!

# ! WARNING ! MINECRAFT MUST BE LAUNCHED AND YOU MUST BE IN MINECRAFT FOR THE AI TO WORK PROPERlY


DOCS WRITTEN BY @itay-cyber

