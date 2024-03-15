class Entity():
  """  Represents an entity in the game  """
  
  def __init__(self, name, max_hp):
    """  Sets the name and max_hp using the parameters. Sets the hp to max_hp.

    Args:
        name (String): The name of the entity.
        max_hp (Int): The maximum health an entity can have.
    """
    self._name = name
    self._hp = max_hp
    self._max_hp = max_hp

  @property
  def name(self):
    """  Decorater to get the name of the entity and return it.

    Returns:
        String: returns string of the name of the entity.
    """
    return self._name

  @property
  def hp(self):
    """  Decorater to get the hp of the entity and return it.

    Returns:
        Int: return integer of the hp of the entity.
    """
    return self._hp

  def take_damage(self, dmg):
    """  Initiates damage to the entity. Subtracts the damage from the entity's hp. If the hp is less than 0, it sets it back to 0

    Args:
        dmg (Int): The total amount of damage that is made.
    """
    self._hp = self._hp - dmg
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    """  Initiates the format of the print statement of an entity's information

    Returns:
        String: Returns string print of the entity's information.
    """
    return f"{self._name}: {self._hp}/{self._max_hp}"