class Object:
    def __init__(self, x = 50, y = 50, name = 'none', creature = None):
        self.x = x
        self.y = y
        self.name = name
        self.creature = creature

class Creature:
    def __init__(self, attrbutes = [], size = 50, speed = 1, target = [0,0]):
        self.attributes = attributes
        self.size = size
        self.speed = speed
        self.target = target
        
    




def setup() :
    objects = []
    size(500, 500)
    background(255)
    
    owo = Creature()
    obj = Object(creature = owo)
    objects.append(obj)
    
def draw():
    background(255)
    
    for obj in objects:
        fill(0)
        circle(obj.x,obj.y,obj.creature.size)
