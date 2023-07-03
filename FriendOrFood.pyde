WIDTH = 700
HEIGHT = 700
FOODAMOUNT = 20
MAXOBJECTS = 100


objects = []
    
def setup():
    global objects
    size(WIDTH, HEIGHT)
    fill(0)
    noStroke()
    creature_component = Creature()
    objects.append(Object(creature = creature_component))
    
    place_food()
    
def draw():
    background(255)
    global objects
    active_objects = objects
    for obj in active_objects:
        fill(obj.color)
        circle(obj.x,obj.y,obj.size)
        if obj.creature:
                
            obj.creature.take_turn()
def mouseClicked():
    place_food()
        
def place_food(amount = FOODAMOUNT):
    i = 0
    if len(objects) >= MAXOBJECTS:
        return
    while i <= amount:
        if i <= amount/2:
            xfood = random(50,WIDTH - 50)
            yfood = random(50, HEIGHT - 50)
        else:
            xfood = random(WIDTH/2-WIDTH/10,WIDTH/2+WIDTH/10)
            yfood = random(HEIGHT/2-HEIGHT/10,HEIGHT/2+HEIGHT/10)
            
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
    def __init__(self,health = 2000, speed = 10, senses = 100, attributes = [], target = None, size = 10):
        self.base_health = health
        self.health = health
        self.speed = speed
        self.senses = senses
        self.attributes = attributes
        self.target = target
        self.energy_loss = 4
        self.initiative = 0
        if self.energy_loss <= 1:
            self.energy_loss = 1
   
    def calc_energy(self):
        self.energy_loss = int((self.speed * self.speed * self.owner.size * self.owner.size * self.senses)/250000)
        if self.energy_loss <= 1:
            self.energy_loss = 1
            
    def take_turn(self):
        owo = self.owner
        speed = self.speed
        if self.health <= self.base_health/10:
            speed = speed/2
        self.initiative += speed
        while self.initiative >= 10:
            self.initiative -= 10
            self.move_target()
        self.health -= self.energy_loss
        if self.health <= 0:
            objects.remove(owo)
        
    
    def eat(self, food):
        objects.remove(food)
        self.health += 500
        if self.health >= self.base_health:
            self.health = self.base_health
        self.replicate()
        
    def replicate(self):
        
        creature_component = Creature(health = self.base_health, speed = self.speed, senses = self.senses, attributes = self.attributes, size = self.owner.size)
        newowo = Object(x = self.owner.x, y = self.owner.y, creature = creature_component,color = self.owner.color, size = self.owner.size)
        newowo.creature.mutate()
        newowo.creature.calc_energy()
        objects.append(newowo)
    
    def mutate(self):
        if int(random(3)) == 1:
            choice = int(random(0,3))
            change = int(random(0,2))
            if change == 0:
                change = -1
            if choice == 0:
                self.speed += change
                self.owner.color = color(200,0,0)
                if self.speed <= 0:
                    self.speed = 1
            elif choice == 1:
                self.senses += change*20
                if self.senses <= 0:
                    self.senses = 20
                self.owner.color = color(0,0,200)
            elif choice == 2:
                self.owner.size +=change
                self.health += change*200
                self.base_health += change*200
                if self.owner.size <= 0:
                    self.owner.size = 1
                    self.base_health = 200
                    self.health = 200
                self.owner.color = color(0,200,0)
        
        
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
            rx = random(1, WIDTH-1)
            ry = random(1, HEIGHT - 1)
            while dist(owo.x,owo.y,rx,ry) > self.senses:
                
                rx = random(1, WIDTH -1 )
                ry = random(1, HEIGHT -1)
            self.target = [rx,ry]
    
    def move(self, dx, dy):
        owo = self.owner
        owo.x += dx
        owo.y += dy
        
                
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
                
        
    
    
        
        
    
