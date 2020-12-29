import ai_main
import time
import ai_movement
import ai_misc_functions
import ai_attributes



ai = ai_main.MinecraftAI(ai_movement.AIMovement(), ai_attributes.AIAttributes(), ai_misc_functions.AIMiscFunctionsInvoker())


ai.movement.move_forward(5)
ai.movement.move_backward(5)

time.sleep(1)
ai.movement.jump()
time.sleep(0.4)
ai.movement.jump()