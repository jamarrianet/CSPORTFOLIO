##CN/NAME: #30 SORIANO, Marriane Audrey F.
##SECTION: Balingkilat
##DATE: 08/27/2026

class Hero:
  def __init__(self,name,hp = 100):
    self.name = name
    self.hp = hp
  def take_damage(self,amount):
    self.hp -=amount


myHero = Hero("Arthur")
myHero2 = Hero("Morgana")

myHero.take_damage(10)

print(myHero.name,"'s hp is at",myHero.hp, ",while,", myHero2.name, "'s hp is at", myHero2.hp)
