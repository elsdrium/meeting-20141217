class Animal(object):
    def __init__(self, has_legs, has_wings, can_swim, can_make_sound):
        self.has_legs       = has_legs
        self.has_wings      = has_wings
        self.can_swim       = can_swim
        self.can_make_sound = can_make_sound

    def make_sound(self):
        print "Sound behavior undefined"

# is_a is the correct choice in this particular case
class Dog(Animal):
    def __init__(self):
        self.has_legs       = True
        self.has_wings      = False
        self.can_swim       = True
        self.can_make_sound = True

    def make_sound(self):
        print "Not this:"
        super(Dog, self).make_sound()
        print "This!"
        print "Woof!"

def output():
    a = Animal(has_legs=True,has_wings=True,can_swim=True,can_make_sound=True)
    a.make_sound()
    a.ad_hoc_attribute = 5

    print "---"

    d = Dog()
    d.make_sound()

