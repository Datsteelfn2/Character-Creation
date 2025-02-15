class character:
  name:None
  health:100
  magic_points=100
  def __init__(self,name,health,magic_points):
    self.name=name
    self.health=health
    self.magic=magic_points
  def print(self):
    print(f"{self.name} has a health of {self.health} and {self.magic} magic points")


class player(character):
  nick_name=None
  lives=None
  def __init__(self,nick_name,lives):
    self.nick=nick_name
    self.lives=lives
  def isAlive(self):
    if self.lives<50:
      print(f"{self.nick} Is not Alive")
    else:
      print(f"{self.nick} is alive")
rick=player("Ricky",5)
rick.isAlive()
class enemy(character):
  type=None
  strength=None
  def __init__(self,type,strength):
    self.type=type
    self.strength=strength

class orc(enemy):
  speed=None
  def __init__(self,name,speed):
    self.name=name
    self.speed=speed
orc1=orc("Adam","45mph") 
orc2=orc("Bob","30mph")

class vampire(enemy):
  day=None
  def __init__(self,name,day):
    self.name=name
    self.day=day
vamp=vampire("Dracula",False)