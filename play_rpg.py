from assignment8_rrm2738 import *
import random

#create a set of inventory items
items = {"loaf of bread", "gold coin", "roll of twine",
         "candle", "amethyst crystal", "dagger"}

'''
Checks for finding a health elixir.
Health can be restored by a value between 0-5.
'''
def check_for_health_elixir(hero):
    random_chance = random.randint(0,5)
    if random_chance == 5:
        health_amt = random.randint(2,5)
        print("You have found a health elixir.")
        print("Drinking it restores your health by " \
              + str(health_amt) + ".")
        hero.restore_health(health_amt)
        print("Your current health is " + str(hero.health) + ".\n")

'''
Checks for finding inventory.
'''
def check_for_inventory(hero):
    random_chance = random.randint(0,4)
    if random_chance == 4:
        item = random.sample(items, 1)[0]
        print("You have found a " + item + ".")
        hero.add_inventory(item)
        print("Your current inventory is " + str(hero.get_inventory()) + ".\n")

'''
Determines how much damage is inflicted by running from 
an enemy (a value from 0 to half the enemy's damage power).
'''
def run(hero, enemy):
    damage = random.randint(0, enemy.damage//2)
    print("The " + enemy.name + " inflicted a damage of " \
          + str(damage) + " as you ran away.")
    health = hero.take_damage(damage)
    print("Your current health is " + str(health) + ".\n")

'''
Determines how much damage is incurred by fighting an
enemy. If hero wins, 0 damage is taken. If enemy
wins, then the enemy's full damage power is taken.
'''
def fight(hero, enemy):
    winner = random.randint(0,1)
    if winner == 0:
        print("You have defeated the " + enemy.name + ".")
    else:
        print("You have lost the fight. The " \
              + enemy.name \
              + " has inflicted a damage of " \
              + str(enemy.damage) + ".")
        health = hero.take_damage(enemy.damage)
    print("Your current health is " + str(hero.health) + ".\n")

def main():

    #create 1 hero and 4 enemies
    hero = Hero('Elsa', 40)
    goblin = Enemy('Goblin', 10, 5)
    dragon = Enemy('Dragon', 30, 10)
    ogre = Enemy('Ogre', 20, 8)
    wizard = Enemy('Wizard', 20, 10)

    #put the enemies in a set
    enemies = {goblin, dragon, ogre, wizard}

    print("You are the hero " + hero.name + ". Your current health is " \
          + str(hero.health) + ".\n")
    
    game_over = False
    while not game_over:

        #check for health elixir
        check_for_health_elixir(hero)

        #check for inventory
        check_for_inventory(hero)

        #encounter an enemy - randomly select one from the set of enemies
        enemy = random.sample(enemies, 1)[0]
        print("You have encountered a " +  enemy.name + ".")
        action = input("Do you want to run or fight?").strip()

        while action != "run" and action != "fight":
            action = input("Do you want to run or fight?").strip()

        #respond to the user's action (run or fight)     
        if action == "run":
            run(hero, enemy)

        elif action == "fight":
            fight(hero, enemy)

        #check hero's health 
        if hero.health <= 0:
            print("You are dead!\nGame over.")
            game_over = True   
            

if __name__ == '__main__':
    main()
