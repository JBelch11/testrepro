class bird:
    wings=2
    legs=2
    beak=1
    def __init__(self,name,weight,color):
        self.species=name
        self.weight=weight
        self.color=color
        print('Creating object %s' % self.species)
    def eat(self):
        print('I am eating')
    def make_sounds(self):
        print('I am chirping')
    def fly(self):
        print('I am flying')
    def speak(self):
        print('Hi I am a %s. I have %s legs, %s wings, and %s beak.' % (self.species,self.legs,self.wings,self.beak))
        print('I weigh %s grams and am %s in color' % (self.weight, self.color))
        

bluebird=bird('bluebird', 30, 'blue')
sparrow=bird('sparrow', 12, 'brown')
print(bluebird.legs)
print(sparrow.legs)
bluebird.fly()
bluebird.speak()
sparrow.speak()
      
