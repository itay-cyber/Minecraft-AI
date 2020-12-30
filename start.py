import ai_main
import time
import ai_movement
import ai_misc_functions
import ai_attributes
import pyKey


ai = ai_main.MinecraftAI(ai_movement.AIMovement(), ai_attributes.AIAttributes(), ai_misc_functions.AIMiscFunctionsInvoker())

ai.movement.move_forward(5)
ai.movement.move_left(5)
ai.movement.move_forward(6)
ai.movement.sprint_rfw(10)

ai.movement.jump()

ai.movement.sprint_rfw(10)

ai.movement.jump()
