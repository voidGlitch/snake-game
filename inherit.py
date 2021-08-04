class Animals:
    def __init__(self):
        self.num_eyes =2
    
    def breathe(self):  #remember to add self 
        print("inhale ,exhale")

class Fish(Animals):
    def __init__(self):
        super().__init__()  #inherit the attributes of previous class

    def breathe(self):
        super().breathe()   #inherit the code of previous class and we can add some new functionality in it
        print("doing this under water")

    def swin(self):
        print("smimming in the water")


tim = Fish()
tim.breathe()
print(tim.num_eyes)