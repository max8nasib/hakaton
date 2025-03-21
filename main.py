"""
Программа мини-игра битва игрока с монстром.
"""
import random


# Класс монстра
class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        return random.randint(10, 25)


# Класс игрока
class Player:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana

    # Обычная атака
    def attack(self, weapon):
        return random.randint(weapon['min'], weapon['max'])

    # Спец атака
    def special_attack(self, weapon):
        if self.mana >= 30:
            self.mana -= 30
        return random.randint(weapon['min'] * 2, weapon['max'] * 2)


# Выбор монстра
def select_monster():
    monsters = {
        '1': Monster("Гоблин", 150),
        '2': Monster("Дракон", 100),
    }
    rand = input("Выберите монстрa(1-Гоблин, 2-Дракон): ")
    return monsters.get(rand)


# Выбор оружия
def select_weapon():
    weapons = {
        '1': {'name': 'Меч', 'min': 12, 'max': 22},
        '2': {'name': 'Топор', 'min': 10, 'max': 25},
    }
    rand = input("Выберите оружие (1-Меч, 2-Топор): ")
    return weapons.get(rand)


# Процесс битвы
def battle(player, monster, weapon):
    while player.hp > 0 and monster.hp > 0:
        act = input("Выберите атаку (1-Обычная атака, 2-спец атака): ")
        if act == '1':
            dmg = player.attack(weapon)
            monster.hp -= dmg
            print(f""
                  f"\n{player.name} атакует {monster.name}\n"
                  f"и наносит {dmg} урона!")
            print(f"У {monster.name} осталось {monster.hp} HP\n"
                  f"")
        elif act == '2':
            if player.mana <= 30:
                print("Недостаточно маны, повторите атаку!")
                continue
            dmg = player.special_attack(weapon)
            monster.hp -= dmg
            print(f""
                  f"\n{player.name} использует спец атаку\n"
                  f"и наносит {dmg} урона!")
            print(f"У {monster.name} осталось {monster.hp} HP\n"
                  f"")

        if monster.hp <= 0:
            print(f"{monster.name} был побежден! Поздравляем!")
            break

        player.hp -= monster.attack()
        print(f"{monster.name} атакует {player.name}\n"
              f"и наносит {monster.attack()} урона!")
        print(f"У {player.name} осталось {player.hp} HP и {player.mana} маны\n"
              f"")
        if player.hp <= 0:
            print(f"{player.name} к сожалению, Вы проиграли!")
            break


# Вывод программы
player_name = input("Введите имя игрока: ")
player = Player(player_name, 100, 100)
monster = select_monster()
weapon = select_weapon()


# Проверка
if monster and weapon:
    battle(player, monster, weapon)
else:
    print('Неверный выбор!')
