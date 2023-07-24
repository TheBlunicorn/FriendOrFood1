noLoop()
WIDTH = 1600
HEIGHT = 1000
FOODAMOUNT = 12
MAXOBJECTS = 200
HEALTH = 4000
MUTATION_CHANCE = 40
AUTOFOOD = True
FOODINTERVAL = 200
coloryellow = color(244,255,0)
colorgreen = color(0,255,0)
colorred = color(255,0,0)
colorblue = color(255,255,255)
colorpink = color(252,3,207)
objects = []
counter = 0
def setup():
    imageMode(CENTER)
    global uwu000, uwu100, uwu010, uwu110, uwu001, uwu101, uwu011, uwu111, startBtn, title, f, displayname
    global foodpear, foodapple, foodblueberry, foodcherry, foodlemon, foodorange, foodstarfruit
    displayname =''
    startBtn = loadImage("IMG_FoF_start.PNG")
    title = loadImage("IMG_FoF_title.PNG")
    uwu000 = loadImage("data/IMG_uwu_000.PNG")
    uwu100 = loadImage("data/IMG_uwu_100.PNG")
    uwu010 = loadImage("data/IMG_uwu_010.PNG")
    uwu110 = loadImage("data/IMG_uwu_110.PNG")
    uwu001 = loadImage("data/IMG_uwu_001.PNG")
    uwu101 = loadImage("data/IMG_uwu_101.PNG")
    uwu011 = loadImage("data/IMG_uwu_011.PNG")
    uwu111 = loadImage("data/IMG_uwu_111.PNG")
    foodpear = loadImage("data/IMG_FoF_pear.PNG")
    foodapple = loadImage("data/IMG_FoF_apple.PNG")
    foodblueberry = loadImage("data/IMG_FoF_blueberry.PNG")
    foodcherry = loadImage("data/IMG_FoF_cherry.PNG")
    foodlemon = loadImage("data/IMG_FoF_lemon.PNG")
    foodorange = loadImage("data/IMG_FoF_orange.PNG")
    foodstarfruit = loadImage("data/IMG_FoF_starfruit.PNG")
    f = loadFont("ArcadeClassic-16.vlw")
    global objects
    size(WIDTH, HEIGHT)
    fill(0)
    noStroke()
    creature_component = Creature()
    objects.append(Object(name = 'Qualli',creature = creature_component))
    
    place_food()
    
def draw():
    background(255)
    global objects, counter, f
    active_objects = objects
    for obj in active_objects:
        if obj.creature:
            tint(obj.color)
            image(obj.sprite, obj.x,obj.y,obj.size*4,obj.size*4)
        else:
            tint(255,255,255)
            image(obj.sprite, obj.x,obj.y,obj.size*4,obj.size*4)
        if obj.creature and objects.count(obj) > 0:
                
            obj.creature.take_turn()
    if AUTOFOOD == True:
        counter +=1
        if counter >= FOODINTERVAL and len(objects) < MAXOBJECTS:
            place_food()
            counter = 0
    textFont(f,16)
    fill(0)
    get_name_under_mouse()
    text(displayname,mouseX+25,mouseY+25)
    fill(0,20)
    rectMode(CENTER)
    rect(width/2+30, HEIGHT/2+30, title.width, title.height/2);
    image(title, width/2 ,300)
    image(startBtn, width/2, height/1.4, startBtn.width / 3, startBtn.height / 3)
 
def get_name_under_mouse():
    global displayname
    x = mouseX
    y = mouseY
    for obj in objects:
        if x-8 <= obj.x <= x+8 and y-8 <= obj.y <= y+8:
            displayname = obj.name
            return
          
def mouseClicked():
    if WIDTH/2 - startBtn.width/2 < mouseX < WIDTH/2 + startBtn.width/2 and HEIGHT/2 - startBtn.height/1.4 < mouseY < HEIGHT/1.4 + startBtn.height/2:
        loop()
        title.width=0
        startBtn.width=0
def mousePressed():
    place_clickfood()
        
def place_food(amount = FOODAMOUNT):
    if len(objects) >= MAXOBJECTS:
        return
    i = 0
    while i <= amount:
        if i <= amount/2:
            xfood = random(50,WIDTH - 50)
            yfood = random(50, HEIGHT - 50)
        else:
            xfood = random(WIDTH/2-WIDTH/10,WIDTH/2+WIDTH/10)
            yfood = random(HEIGHT/2-HEIGHT/10,HEIGHT/2+HEIGHT/10)
            
        colorfood = color(255,255,255)
        objects.append(Object(x = xfood,y = yfood,name = 'food',color = colorfood, size = 5))
        i += 1
def place_clickfood():
    colorfood = color(255,255,255)
    xdiverge = random(-10,10)
    ydiverge = random(-10,10)
    objects.append(Object(x = mouseX+xdiverge,y = mouseY+ydiverge,name = 'food',color = colorfood, size = 5))
    
    
class Object:
    def __init__(self, x = WIDTH/2, y = HEIGHT/2, name = 'none', creature = None, color = color(255,255,255), size = 10, sprite = None):
        self.x = x
        self.y = y
        self.name = name
        self.creature = creature
        self.color = color
        self.size = size
        self.sprite = sprite
        if self.creature:
            self.creature.owner = self
            self.sprite = uwu000
        else:
            choice = int(random(0,8))
            
            if choice == 0:
                self.sprite = foodpear
            elif choice == 1:
                self.sprite = foodapple
            elif choice == 2:
                self.sprite = foodblueberry
            elif choice == 3:
                self.sprite = foodcherry
            elif choice == 4:
                self.sprite = foodlemon
            elif choice == 5:
                self.sprite = foodorange
            else:
                self.sprite = foodstarfruit
                
    def get_name(self):
        newname = ''
        name1 = ['Fr','B','Gn','Schn','M','V','K','F','X','W','R','T','H','Qu','Kr','Sh','Ch','D','L','S','']
        name2 = ['e','o','u','a','i','y','au','eu','oo','oi','ou','ei','uh','ee','ah','ae','ar','a','o','u','']
        name3 = ['di','zo','da','lo','sha','ge','te','shi','fu','ki','kto','ge','li','phi','nu','ru','me','re','we','be','']
        name4 = ['nand','bert','sam','ter','rk','l','r','gam','ner','pus','ger','le','m','lim','dil','bri','leon','lauch','tier','ling','']
        newname += (name1[int(random(1,20))])
        newname += (name2[int(random(1,20))])
        newname += (name3[int(random(1,20))])
        newname += (name4[int(random(1,20))])
        print(newname)
        self.name = newname
        
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
        self.energy_loss = int((self.speed * self.speed * self.owner.size * self.senses)/10000)
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
            if self.check_attribute('horns'):
                speedy -=1
            if self.check_attribute('hands'):
                speedy -=1
            if self.check_attribute('carnivore'):
                speedy +=2
            if self.check_attribute('chilling'):
                    self.find_target()
                    if self.check_attribute('chilling'):
                        #self.health += int(self.energy_loss/2)
                        energy = int(energy*2/3)
                        if energy <1:
                            energy = 1
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
        if target.creature.check_attribute('horns'):
            self.health -= self.base_health/2
            
            if self.health <= 0:
                self.health = 0
                print('ouch!')
                return
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
        newowo = Object(x = self.owner.x, y = self.owner.y, name = self.owner.name, creature = creature_component,color = self.owner.color, size = self.owner.size)
        for obj in self.attributes:
            newowo.creature.attributes.append(obj)
        newowo.creature.mutate()
        newowo.creature.updatesprite()
        newowo.creature.calc_energy()
        objects.append(newowo)
    
    def mutate(self):
        if int(random(100)) <= MUTATION_CHANCE:
            r = red(self.owner.color)
            g = green(self.owner.color)
            b = blue(self.owner.color)
            choice = int(random(0,5))
            change = int(random(0,2))
            if change == 0:
                change = -1
            if choice == 0:
                self.speed += change
                if self.speed <= 0:
                    self.speed = 1
                r = int(self.speed*255/20)
                if r >= 255:
                    r = 255
                #self.owner.color = color(r,g,b)
            elif choice == 1:
                self.senses += change*20
                if self.senses <= 0:
                    self.senses = 20
                g = int(self.senses*255/200)
                if g >= 255:
                    g = 255
                #self.owner.color = color(r,g,b)
            elif choice == 2:
                self.owner.size +=change
                self.health += change*HEALTH/10
                self.base_health += change*HEALTH/10
                if self.owner.size <= 0:
                    self.owner.size = 1
                    self.base_health = HEALTH/10
                    self.health = HEALTH/10
                b = int(self.owner.size*255/20)
                if b >= 255:
                    b = 255
                #self.owner.color = color(r,g,b)
            elif choice == 4:
                selection = int(random(0,11))
                self.owner.get_name()
                if selection <= 5:
                    if self.check_attribute('carnivore') == False:
                        self.attributes.append('carnivore')
                    else:
                        self.attributes.remove('carnivore')
                elif selection == 6:
                    if self.check_attribute('lazy') == False:
                        self.attributes.append('lazy')
                        print('new lazy creature')
                elif selection <= 8:
                    if self.check_attribute('horns') == False:
                        self.attributes.append('horns')
                        print('new horny creature')
                    else:
                        self.attributes.remove('horns')
                elif selection <= 10:
                    if self.check_attribute('hands') == False:
                        self.attributes.append('hands')
                        print('new handy creature')
                    else:
                        self.attributes.remove('hands')
        if int(random(100)) <= MUTATION_CHANCE/2:
            self.owner.get_name()
            selection = int(random(0,6))
            if selection == 1:
                self.owner.color = colorred
            elif selection == 2:
                self.owner.color = colorgreen
            elif selection == 3:
                self.owner.color = coloryellow
            elif selection == 4:
                self.owner.color = colorblue
            elif selection == 5:
                self.owner.color = colorpink
                        
    def updatesprite(self):
        if self.check_attribute('carnivore'):
            if self.check_attribute('horns'):
                if self.check_attribute('hands'):
                    self.owner.sprite = uwu111
                else:
                    self.owner.sprite = uwu110
            else:
                if self.check_attribute('hands'):
                    self.owner.sprite = uwu101
                else:
                    self.owner.sprite = uwu100
                
        else:
            if self.check_attribute('horns'):
                if self.check_attribute('hands'):
                    self.owner.sprite = uwu011
                else:
                    self.owner.sprite = uwu010
            else:
                
                if self.check_attribute('hands'):
                    self.owner.sprite = uwu001
                else:
                    self.owner.sprite = uwu000
                    
                        
        
        
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
                        if obj.size < owo.size-1 or (self.check_attribute('hands') and obj.size <= owo.size and not obj.creature.check_attribute('carnivore')):
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
        grabdist = 3
        if self.check_attribute('hands'):
            grabdist +=2
        if distance < grabdist:
            for obj in objects:
                if obj != owo:
                    if dist(owo.x, owo.y, obj.x, obj.y) < grabdist:
                        if obj.name == 'food' and self.check_attribute('carnivore') == False:
                            self.eat(obj)
                            break
                        elif  obj.creature and self.check_attribute('carnivore'):
                            if (obj.size < owo.size-1 or (self.check_attribute('hands') and obj.size <= owo.size and not obj.creature.check_attribute('carnivore'))) and obj.creature.health > 0:
                                self.attack(obj)
                                break
            self.find_target()
        else:
            dx = int(round(distx/distance))
            dy = int(round(disty/distance))
            self.move(dx,dy)
                
        
    
    
        
        
    
