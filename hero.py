from entity import Entity
import random

class Hero(Entity):
  """  A class that represents a hero. Inherits from the Entity class  """
  def sword_attack(self, dragon):
    """Roll 2 dices and subtract the damage from the dragon's hp. Then return a string of the damage dealt to the dragon.

    Args:
        dragon (Object): Take an object that got the method take_damage

    Returns:
        String: Return a formated String
    """
    first_roll = random.randint(1, 6)
    second_roll = random.randint(1, 6)
    total_dmg = first_roll + second_roll
    dragon.take_damage(total_dmg)
    return f"You slash the {dragon.name} with your sword for {total_dmg} damage."
    
  def arrow_attack(self, dragon):
    """ Roll 1 dice and subtract the damage from the dragon's hp. Then return a string of the damage dealt to the dragon.

    Args:
        dragon (Object): Take an object that got the method take_damage

    Returns:
        String: Return a formated String
    """
    first_roll = random.randint(1, 12)
    dragon.take_damage(first_roll)
    return f"You hit the {dragon.name} with an arrow for {first_roll} damage."