import ai_main
import time
import ai_movement
import ai_misc_functions
import ai_attributes


ai = ai_main.MinecraftAI(ai_movement.AIMovement(), ai_attributes.AIAttributes(), ai_misc_functions.AIMiscFunctionsInvoker())
