from dragon import Dragon
import random

class FireDragon(Dragon):
  """  Represents a fire dragon. Inherits from the Dragon class  """
  def __init__(self, name, max_hp, f_shots):
    """ Use super to set the name and hp, then set the number of fire_shots the FireDragon has.

    Args:
        name (String): Set the name of the dragon
        max_hp (Int): Set the max hp a dragon can get
        fire_shots (Int): Set the fire_shots a flying dragon can have
    """
    super().__init__(name, max_hp)
    self.fire_shots = f_shots
  
  def special_attack(self, hero):
    """  Overides the special attack method from the dragon class. Roll 1 dice and subtract the damage from the hero's hp. If the dragon have 0 fire_shots left, it will return a string saying that the dragon has no fire_shots left.

    Args:
        hero (object): a hero object that has the method takes_damage

    Returns:
        String: returns a a string of the damage dealt to the hero, who is incflicting the damage, and how many fire_shots left
    """
    if self.fire_shots > 0:
      dmg = random.randint(5,9)
      hero.take_damage(dmg)
      self.fire_shots -= 1
      return f"{self.name} engulfs you in flames for {dmg} damage!"
    else:
      return f"{self.name} has no fire shots left"

  def __str__(self): 
    """  Initiates the format of the print statement of the dragons information

    Returns:
        String: returns a string print of the dragons information from the basic entity information and the dragon information added onto it.
    """
    return f"{super().__str__()} \nFire Shots remaining: {self.fire_shots}"
