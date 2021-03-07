class Characters:
  def __init__(self, name, health):
    self.name = name
    self.health = health

  def __str__(self):
      return self.name + ' (health=' + str(self.health) + ')'


  def take_damage(self, damage):
    self.health -= damage
    return self.health

  def restore_health(self, add):
      self.health += add

class Hero(Characters):
  def __init__(self, name, health):
    super().__init__(name, health)
    self.inventory = []

  def add_inventory(self, item):
      self.inventory.append(item)

  def remove_inventory(self, item):
      self.invetory.remove(item)

  def get_inventory(self):
      return self.inventory

class Enemy(Characters):
  def __init__(self, name, health, damage):
    self.name = name
    self.health = health
    self.damage = damage
