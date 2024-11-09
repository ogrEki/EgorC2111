import random

# Убираем неиспользуемый импорт
# from pkg_resources import empty_provider

# Предполагается, что figth это функция, но она не используется в этом коде, поэтому убрал
# from main import figth

class Enemy:
    def __init__(self):  # Инициализация через __init__
        self.hp = 10
        self.attack = 2
        self.win = 2
        self.lose = 5

class Plant:
    def __init__(self):  # Инициализация через __init__
        self.hp = 2
        self.attack = 1
        self.money = 0

# Создаем объект растения
my_plant = Plant()

# Ввод действия
move = input("Полить(А), Покращити(В), Донат(D): ").upper()

if move == "A":
    napalu = random.randint(1, 5)
    napalu2 = napalu
    if napalu == 1:
        # Создаем врага
        my_enemy = Enemy()

        myhp = my_plant.hp
        myattack = my_plant.attack
        enemyhp = my_enemy.hp
        enemyattack = my_enemy.attack
        figth = random.randint(1, 3)

        if figth == 1:
            while True:
                enemyhp -= myattack
                if enemyhp <= 0:
                    my_plant.money += my_enemy.win
                    my_plant.money += random.randint(1, 5)
                    print("Враг побежден, ты получил монеты!")
                    break
                else:
                    print("Враг атакует!")

                myhp -= enemyattack
                if myhp <= 0:
                    my_plant.money -= my_enemy.lose
                    print("Ты проиграл, потерял монеты.")
                    break
                else:
                    print("Ты продолжаешь сражаться!")

        else:
            while True:
                myhp -= enemyattack
                if myhp <= 0:
                    my_plant.money -= my_enemy.lose
                    print("Ты проиграл, потерял монеты.")
                    break
                else:
                    print("Ты продолжаешь сражаться!")

    else:
        my_plant.money += random.randint(1, 5)
        print("Ты полил растение и получил монеты!")

elif move == "B":
    print("Error: эта опция еще не реализована.")

elif move == "D":
    print("Error: эта опция еще не реализована.")

else:
    print("Неверный ввод!")

print(f"Ваши монеты: {my_plant.money}")
