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

    # __truediv__ changed from __div__ in Python 3
    def __truediv__(self, other):
        if isinstance(other,People):
            return "{} swings a lightsaber at {}.".format(self.name,other.name)
        else:
            raise TypeError()

    def __mul__(self, other):
        if isinstance(other,People):
            return "{} throws a thermal detonator at {}!".format(self.name,other.name)
        else:
            raise TypeError()        

    def __rshift__(self, other):
        if isinstance(other,People):
            return "{} uses the force to push {} away from them.".format(self.name,other.name)
        else:
            raise TypeError()                  

    def __lshift__(self, other):
        if isinstance(other,People):
            return "{} uses the force to pull {} towards them.".format(self.name,other.name)
        else:
            raise TypeError()               

    def __neg__(self):
        self.dark_side = True
        self.light_side = False
        return self

    def __pos__(self):
        self.dark_side = False
        self.light_side = True
        return self        

    def __invert__(self):
        self.light_side = not self.light_side       

    def __xor__(self, other):
        return "{} force chokes {}.".format(self.name,other.name)   

    def __eq__(self, other):
        if self.name == 'Greedo' and other.name == 'Han Solo':
            return "{} shoots {}. BECAUSE HAN SHOOTS FIRST.".format(other.name,self.name)  
        else:
            return "{} shoots {}.".format(self.name,other.name)  