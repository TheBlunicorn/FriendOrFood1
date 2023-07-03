WIDTH = 700
HEIGHT = 700
FOODAMOUNT = 50
MAXOBJECTS = 200
HEALTH = 2000
MUTATION_CHANCE = 25
AUTOFOOD = True
FOODINTERVAL = 700


objects = []
counter = 0
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
    global objects, counter
    active_objects = objects
    for obj in active_objects:
        fill(obj.color)
        if obj.creature:
            if obj.creature.check_attribute('carnivore'):
                square(obj.x,obj.y,obj.size)
            else:
                circle(obj.x,obj.y,obj.size)
        else:
            circle(obj.x,obj.y,obj.size)
        if obj.creature and objects.count(obj) > 0:
                
            obj.creature.take_turn()
    if AUTOFOOD == True:
        counter +=1
        if counter >= FOODINTERVAL:
            place_food()
            counter = 0
        
def mouseClicked():
    place_food()
        
def place_food(amount = FOODAMOUNT):
    i = 0
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
    def __init__(self, x = WIDTH/2, y = HEIGHT/2, name = 'none', creature = None, color = color(0,0,0), size = 10):
        self.x = x
        self.y = y
        self.name = name
        self.creature = creature
        self.color = color
        self.size = size
        if self.creature:
            self.creature.owner = self

class Creature:
    def __init__(self,health = HEALTH, speed = 10, senses = 100, target = None, size = 10):
        self.attributes = []
        self.base_health = health
        self.health = health
        self.speed = speed
        self.senses = senses
        self.target = target
        self.energy_loss = 4
        self.initiative = 0
        if self.energy_loss <= 1:
            self.energy_loss = 1
                
    def check_attribute(self, check):
        result = False
        for attr in self.attributes:
           if attr == check:
               result = True
               break
        return result

   
    def calc_energy(self):
        self.energy_loss = int((self.speed * self.speed * self.owner.size * self.owner.size * self.senses)/250000)
        if self.energy_loss <= 1:
            self.energy_loss = 1
            
    def take_turn(self):
        owo = self.owner
        if self.health <= 0:
            objects.remove(owo)
        else:
            energy = self.energy_loss
            speedy = self.speed
            if self.health <= self.base_health/10:
                speedy = speedy/2
            if self.check_attribute('chilling'):
                    self.find_target()
                    if self.check_attribute('chilling'):
                        self.health += int(self.energy_loss/2)
                        energy = energy/2
                        speedy = 1
            self.initiative += speedy
            while self.initiative >= 10:
                self.initiative -= 10
                self.move_target()
            self.health -= energy
            if self.health <= 0:
                objects.remove(owo)
        
    
    def eat(self, food):
        objects.remove(food)
        self.health += HEALTH/4
        if self.health >= self.base_health:
            self.health = self.base_health
        self.replicate()
        
    def attack(self, target):
        target.creature.health = 0
        print('creature eaten')
        self.health += HEALTH
        if self.health >= self.base_health:
            self.health = self.base_health
        self.replicate()
        print('carnivore reproduced')
        
    def replicate(self):
        if len(objects) >= MAXOBJECTS:
            return
        creature_component = Creature(health = self.base_health, speed = self.speed, senses = self.senses, size = self.owner.size)
        newowo = Object(x = self.owner.x, y = self.owner.y, creature = creature_component,color = self.owner.color, size = self.owner.size)
        for obj in self.attributes:
            newowo.creature.attributes.append(obj)
        newowo.creature.mutate()
        newowo.creature.calc_energy()
        objects.append(newowo)
    
    def mutate(self):
        if int(random(100)) <= MUTATION_CHANCE:
            choice = int(random(0,5))
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
                self.health += change*HEALTH/10
                self.base_health += change*HEALTH/10
                if self.owner.size <= 0:
                    self.owner.size = 1
                    self.base_health = HEALTH/10
                    self.health = HEALTH/10
                self.owner.color = color(0,200,0)
            elif choice == 4:
                selection = int(random(0,3))
                if selection <= 1:
                    if self.check_attribute('carnivore') == False:
                        self.attributes.append('carnivore')
                    else:
                        self.attributes.remove('carnivore')
                elif selection == 2:
                    if self.check_attribute('lazy') == False:
                        self.attributes.append('lazy')
                        print('new lazy creature')
                    else:
                        self.attributes.remove('lazy')
                    
                        
        
        
    def find_target(self):
        owo = self.owner
        food = None
        closest_dist = self.senses
        for obj in objects:
            if obj != owo:
                if dist(owo.x, owo.y, obj.x, obj.y) < closest_dist:
                    if obj.name == 'food' and self.check_attribute('carnivore') == False:
                        food = obj
                        closest_dist = dist(owo.x, owo.y, obj.x, obj.y)
                        self.target = [obj.x, obj.y]
                        if self.check_attribute('chilling'):
                            self.attributes.remove('chilling')
                    elif obj.creature and self.check_attribute('carnivore'):
                        if obj.size < owo.size-1:
                            food = obj
                            closest_dist = dist(owo.x, owo.y, obj.x, obj.y)
                            self.target = [obj.x, obj.y]
                            if self.check_attribute('chilling'):
                                self.attributes.remove('chilling')
                            
        if food == None:
            if self.check_attribute('lazy') and self.check_attribute('chilling') == False:
                self.attributes.append('chilling')
            
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
        if distance < 2:
            for obj in objects:
                if obj != owo:
                    if dist(owo.x, owo.y, obj.x, obj.y) < 2:
                        if obj.name == 'food' and self.check_attribute('carnivore') == False:
                            self.eat(obj)
                            break
                        elif  obj.creature and self.check_attribute('carnivore'):
                            if obj.size < owo.size-1 and obj.creature.health > 0:
                                self.attack(obj)
                                break
            self.find_target()
        else:
            dx = int(round(distx/distance))
            dy = int(round(disty/distance))
            self.move(dx,dy)
                
        
    
    
        
        
    
