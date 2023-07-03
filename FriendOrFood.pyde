

objects = []
    
def setup():
    global objects
    size(500, 500)
    fill(0)
    noStroke()
    creature_component = Creature()
    objects.append(Object(creature = creature_component))
    
    place_food()
    
def draw():
    background(255)
    global objects

    for obj in objects:
        fill(obj.color)
        circle(obj.x,obj.y,obj.size)
        if obj.creature:
            i = 0
            while i < obj.creature.speed:
                obj.creature.move_target()
                i+=1
        
def place_food(amount = 20):
    i = 0
    while i <= amount:
        xfood = random(50,450)
        yfood = random(50,450)
        colorfood = color(252,3,3)
        objects.append(Object(x = xfood,y = yfood,name = 'food',color = colorfood, size = 5))
        i += 1
    
class Object:
    def __init__(self, x = 100, y = 50, name = 'none', creature = None, color = color(0,0,0), size = 10):
        self.x = x
        self.y = y
        self.name = name
        self.creature = creature
        self.color = color
        self.size = size
        if self.creature:
            self.creature.owner = self

class Creature:
    def __init__(self,health = 500, speed = 1, senses = 100, attributes = [], target = None):
        self.base_health = health
        self.health = health
        self.speed = speed
        self.senses = senses
        self.attributes = attributes
        self.target = target
    
    @property
    def energy_loss(self):
        energy = int((self.speed * self.owner.size * self.senses)/1000)
        return energy
    
    def eat(self, food):
        objects.remove(food)
        self.health += 200
        self.replicate()
        
    def replicate(self):
        
        creature_component = Creature(health = self.base_health, speed = self.speed, senses = self.senses, attributes = self.attributes)
        newowo = Object(x = self.owner.x, y = self.owner.y, creature = creature_component, size = self.owner.size)
        newowo.creature.mutate()
        objects.append(newowo)
    
    def mutate(self):
        if random(1,2) == 1:
            choice = random(1,3)
            change = random(-1,1)
            if choice == 1:
                self.speed += change
                self.owner.color = (50,0,0)
            elif choice == 2:
                self.senses += change*20
                self.owner.color = (00,0,50)
            elif choice == 3:
                self.owner.size +=change
                self.health += change*50
                self.owner.color = (00,50,0)
        
        
    def find_target(self):
        owo = self.owner
        food = None
        closest_dist = self.senses
        for obj in objects:
            if obj != owo:
                if dist(owo.x, owo.y, obj.x, obj.y) < closest_dist:
                    if obj.name == 'food':
                        food = obj
                        closest_dist = dist(owo.x, owo.y, obj.x, obj.y)
                        self.target = [obj.x, obj.y]
        if food == None:
            rx = random(1, 499)
            ry = random(1, 499)
            while dist(owo.x,owo.y,rx,ry) > self.senses:
                
                rx = random(1, 499)
                ry = random(1, 499)
            self.target = [rx,ry]
    
    def move(self, dx, dy):
        owo = self.owner
        owo.x += dx
        owo.y += dy
        self.health -= self.energy_loss
        if self.health <= 0:
            objects.remove(owo)
        
                
    def move_target(self):
        if self.target == None:
            self.find_target()
        owo = self.owner
        [tx,ty] = self.target
        distx = tx - owo.x
        disty = ty - owo.y
        distance = dist(owo.x, owo.y, tx, ty)
        
        if distance < 1:
            for obj in objects:
                if obj != owo:
                    if dist(owo.x, owo.y, obj.x, obj.y) < 1:
                        if obj.name == 'food':
                            self.eat(obj)
            
            self.find_target()
        else:
            dx = int(round(distx/distance))
            dy = int(round(disty/distance))
            self.move(dx,dy)
                
        
    
    
        
        
    
