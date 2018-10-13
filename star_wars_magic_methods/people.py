class People(object):
    light_side = True
    
    def __init__(self, name, dark_side=False):
        self.name = name
        self.dark_side = dark_side
        self.light_side = not dark_side
    
    def __str__(self):
        return self.name

    def __call__(self):
        return "Help me "+self.name+", you're my only hope."
