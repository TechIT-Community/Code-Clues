import time
import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.debuff = 0

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        time.sleep(2)
        damage = max(0, self.attack_power - target.debuff)
        target.take_damage(damage)

    def take_damage(self, damage):
        print(f"{self.name} takes {damage} damage!")
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25)
        self.blocked_last_turn = False

    def slash(self, target):
        print(f"{self.name} performs a slashing attack on {target.name}!")
        time.sleep(2)
        damage = max(0, self.attack_power + 15 - target.debuff)
        target.take_damage(damage)

    def block(self):
        print(f"{self.name} is blocking!")
        time.sleep(2)
        self.debuff += 10
        self.blocked_last_turn = True

    def reset_block(self):
        self.blocked_last_turn = False

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)
        self.enchanted_last_turn = False

    def cast_spell(self, target):
        print(f"{self.name} casts a powerful spell on {target.name}!")
        time.sleep(3)
        damage = max(0, self.attack_power + 20 - target.debuff)
        target.take_damage(damage)

    def enchant(self, target):
        print(f"{self.name} enchants {target.name}!")
        time.sleep(2)
        target.debuff += 5
        self.enchanted_last_turn = True

    def reset_enchant(self):
        self.enchanted_last_turn = False

class Enemy(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

class BattleArena:
    def __init__(self):
        self.characters = []
        self.enemies_defeated = 0

    def add_character(self, character):
        self.characters.append(character)

    def start_battle(self):
        print("The battle begins!")
        time.sleep(1)
        for turn in range(5):  # Simulate 5 turns
            print(f"\nTurn {turn + 1}:")
            for character in self.characters:
                if isinstance(character, Warrior):
                    if random.choice([True, False]):
                        target = self.get_random_target(character)
                        character.slash(target)
                    else:
                        character.block()
                elif isinstance(character, Wizard):
                    if random.choice([True, False]):
                        target = self.get_random_target(character)
                        character.cast_spell(target)
                    else:
                        ally = self.get_random_ally(character)
                        character.enchant(ally)

            self.reset_actions()


    def get_random_target(self, attacker):
        targets = [c for c in self.characters if isinstance(c, Character) and c != attacker and c.health > 0]
        return random.choice(targets)

    def get_random_ally(self, caster):
        allies = [c for c in self.characters if isinstance(c, Character) and c != caster and c.health > 0]
        return random.choice(allies)

    def reset_actions(self):
        for character in self.characters:
            if isinstance(character, Warrior):
                character.reset_block()
            elif isinstance(character, Wizard):
                character.reset_enchant()


# Object creation and story execution
battle_arena = BattleArena()

warrior = Warrior("Warrior1")
wizard = Wizard("Wizard1")
enemy1 = Enemy("Enemy1", health=100, attack_power=30)
enemy2 = Enemy("Enemy2", health=80, attack_power=40)
enemy3 = Enemy("Enemy3", health=70, attack_power=30)
enemy4 = Enemy("Enemy4", health=90, attack_power=22)
enemy5 = Enemy("Enemy5", health=60, attack_power=28)

battle_arena.add_character(warrior)
battle_arena.add_character(wizard)
battle_arena.add_character(enemy1)
battle_arena.add_character(enemy2)
battle_arena.add_character(enemy3)
battle_arena.add_character(enemy4)
battle_arena.add_character(enemy5)

# Start the battle
battle_arena.start_battle()

"""
Turn 1:
Warrior1 is blocking!
Wizard1 casts a powerful spell on Enemy1!
Enemy1 takes 50 damage!

Turn 2:
Warrior1 is blocking!
Wizard1 casts a powerful spell on Enemy3!
Enemy3 takes 50 damage!

Turn 3:
Warrior1 is blocking!
Wizard1 casts a powerful spell on Enemy2!
Enemy2 takes 50 damage!

Turn 4:
Warrior1 is blocking!
Wizard1 casts a powerful spell on Enemy3!
Enemy3 takes 50 damage!
Enemy3 has been defeated!

Turn 5:
Warrior1 performs a slashing attack on Enemy5!
Enemy5 takes 40 damage!
Wizard1 casts a powerful spell on Enemy1!
Enemy1 takes 50 damage!
Enemy1 has been defeated!

Find the number of enemies defeated at the end of the battle.
"""