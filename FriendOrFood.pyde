

objects = []
    
def setup():
    global objects
    size(500, 500)
    fill(0)
    noStroke()
    
    objects.append(Object())
    
def draw():
    background(255)
    global objects

    for obj in objects:
        circle(obj.x,obj.y,50)
    
class Object:
    def __init__(self, x = 100, y = 50, name = 'none', creature = None):
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
        
    
