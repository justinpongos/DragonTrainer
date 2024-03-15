from entity import Entity
import random

class Dragon(Entity):
  """  Represents a dragon in the game. Inherits from the Entity class  """
  def basic_attack(self, hero):
    """ Roll 1 dice and subtract the damage from the hero's hp. Then return a string of the damage dealt to the hero.

    Args:
        hero (Object): Take an object that got the method take_damage

    Returns:
        String: Return a formated String
    """
    dmg = random.randint(3, 7)
    hero.take_damage(dmg)
    return f"{self.name} smashes you with its tail for {dmg} damage!"
    
  def special_attack(self, hero):
    """ Roll 1 dice and subtract the damage from the hero's hp. Then return a string of the damage dealt to the hero.

    Args:
        hero (Object): Takes an object that got the method take_damage

    Returns:
        String: Return a formated String
    """
    dmg = random.randint(4, 8)
    hero.take_damage(dmg) 
    return f"{self.name} slashes you with its claws for {dmg} damage!"
