class Animal:
    def __init__(self, has_legs, has_wings, can_swim, can_make_sound):
        self.has_legs = has_legs
        self.has_wings = has_wings
        self.can_swim = can_swim
        self.can_make_sound = can_make_sound

    def make_sound(self):
        print "Sound behavior not implemented."

# has_a is the wrong choice in this particular case
class Dog:
    def __init__(self):
        self.prototype = Animal( has_legs=True,
                                 has_wings=False,
                                 can_swim=True,
                                 can_make_sound=True )

    def make_sound(self):
        print "Woof!"

def output():
    a = Animal(has_legs=True,has_wings=True,can_swim=True,can_make_sound=True)
    a.make_sound()
    a.ad_hoc_attribute = 5

    print "---"

    d = Dog()
    print d.prototype.can_swim
    d.make_sound()

