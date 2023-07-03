

objects = []
    
def setup():
    global objects
    size(500, 500)
    fill(0)
    noStroke()
    creature_component = Creature()
    objects.append(Object(creature = creature_component))
    
def draw():
    background(255)
    global objects

    for obj in objects:
        circle(obj.x,obj.y,obj.creature.mass)
    
class Object:
    def __init__(self, x = 100, y = 50, name = 'none', creature = None):
        self.x = x
        self.y = y
        self.name = name
        self.creature = creature
        if self.creature:
            self.creature.owner = self

class Creature:
    def __init__(self, mass = 50, speed = 1, senses = 1, attributes = [], target = [1,1]):
        self.mass = mass
        self.speed = speed
        self.senses = senses
        self.attributes = attributes
        self.target = target
        
        
    
