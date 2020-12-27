class MinecraftAI:
    def __init__(self, movement, attributes_tracker, misc_functions_invoker):
        self.movement = movement
        self.attributes_tracker = attributes_tracker
        self.misc_funcs = misc_functions_invoker

        print("AI INIT")