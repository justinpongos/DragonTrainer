#  Name: Louis Pavlovsky & Justin Pongos
#  Date: 3/4/2024

#  Desc: Dragon Trainer, a game program where a user must defeat three dragons in order to pass the trails. The user will be able to select which of the three dragons to attack and which attack to use, between either sword or arrow. When the hero aka the user attacks a random dragon returns a random attack either a regular or a special one. The damage given by any entity is random depending on the range of the entity each having their own set of possible range of damage. After every attack and counter attack the heroes health is displayed to show how much damage it has taken aswell as the damage it has inflicted on the dragons. When the heroes health reaches zero or all the dragons are defeated, the game will end congratulating you on your victory.
import entity
import hero
import dragon
import fire_dragon
import flying_dragon
import check_input
import random

def main():
  #  Creates dragon objects and hero objects
  dragons = [dragon.Dragon("Deadly Nadder", 10), fire_dragon.FireDragon("Gronckle", 15, 3), flying_dragon.FlyingDragon("Timberjack", 20, 5)]
  name = input("What is your name, challenger?\n")
  hero_obj = hero.Hero(name, 50)
  drag_count = 3
  print(f"Welcome to dragon training, {name}\nYou must defeat 3 dragons.")

  while hero_obj.hp > 0 and len(dragons) > 0:
    #  Displays the health of the hero and the dragons, aswell as the amount of special attacks they have left
    print(f"\n{hero_obj}")
    for i in range(len(dragons)):
      print(f"{i+1}. Attack {dragons[i]}")
      
    #  Displays which ever dragon the user chooses to attack and with what weapon
    dragon_selection = check_input.get_int_range("Choose a dragon to attack: ", 1, drag_count)
    print(f"\nAttack with:\n1. Arrow (1 D12)\n2. Sword (2 D6)")
    weapon_selection = check_input.get_int_range("Enter weapon: ", 1, 2)
    print("")
    if weapon_selection == 1:
        print(hero_obj.arrow_attack(dragons[dragon_selection - 1]))    
    elif weapon_selection == 2:
        print(hero_obj.sword_attack(dragons[dragon_selection - 1]))

    #  Removes the dragon from the list if it is defeated, aswell as decreases the dragon count by 1.
    if dragons[dragon_selection - 1].hp == 0:
        dragons.pop(dragon_selection - 1)
        drag_count -= 1
      
    #  Selects a random dragon to perform a basic or a special attack.
    if len(dragons) != 0:
      rand_dragon_attack = random.randint(1,len(dragons))
      rand_attack_type = random.randint(1,2)
      if rand_attack_type == 1:
        print(dragons[rand_dragon_attack - 1].basic_attack(hero_obj))
      elif rand_attack_type == 2:
        print(dragons[rand_dragon_attack - 1].special_attack(hero_obj))

  if hero_obj.hp <= 0:
    print("\nDefeat")
  else:
    print("\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")
main()