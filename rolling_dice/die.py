from random import randint

class Die:
    
    def __init__(self, num_sides= 6):
        self.numsides = num_sides
        
    def roll(self):
        return randint(1, self.numsides)

