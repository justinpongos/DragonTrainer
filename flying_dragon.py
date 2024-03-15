from dragon import Dragon
import random

class FlyingDragon(Dragon):
  """  Represents a Flying dragon. Inherits from the Dragon class  """
  def __init__(self, name, max_hp, swoops):
    """ Use super to set the name and hp, then set the number of swoops the FlyingDragon has.

    Args:
        name (String): Set the name of the dragon
        max_hp (Int): Set the max hp a dragon can get
        swoops (Int): Set the swoops a flying dragon can have
    """
    super().__init__(name, max_hp)
    self.swoops = swoops

  def special_attack(self, hero):
    """  Overides the special attack method from the dragon class. Roll 1 dice and subtract the damage from the hero's hp. If the dragon have 0 swoops left, it will return a string saying that the dragon has no swoops left.

    Args:
        hero (object): a hero object that has the method takes_damage

    Returns:
        String: returns a a string of the damage dealt to the hero, who is incflicting the damage, and how many swoops left
    """
    if self.swoops > 0:
      dmg = random.randint(5,8)
      hero.take_damage(dmg)
      self.swoops -= 1
      return f"{self.name} swoops you for {dmg} damage!"
    else:
      return f"{self.name} has no swoops left"

  def __str__(self):
    """Initiates the format of the print statement of the dragons information

    Returns:
        String: String: returns a string print of the dragons information from the basic entity information and the dragon information added onto it.
    """
    return f"{super().__str__()} \nSwoop attacks remaining: {self.swoops}"
