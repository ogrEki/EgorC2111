import random

print('Увага усі відповіді на вибори писати на англійській(ENG)!')

magazin = 0

class Stats:
    def __init__(self):
        self.hp = 100
        self.money = 50
        self.attack = 2

class Ghoul:
    def __init__(self):
        self.hp = 1000
        self.money = 50
        self.attack = 10

your_hero = Ghoul()  # Зміна для звичайного героя
your_hero2 = Stats()  # Зміна для випадкового героя
your_hero2.hp = random.randint(50, 150)
your_hero2.money = random.randint(20, 70)

# Обработка выбора героя
while True:
    star = input("Вибір героя Гуль (G), Випадковий (N): ")
    if star == "G":
        print("Ви обрали героя Гуль")
        print("Життя:", your_hero.hp, "Монети:", your_hero.money, "Атака:", your_hero.attack)
        your_hero2 = your_hero
        break
    elif star == "N":
        print("Ви обрали випадкового героя")
        print("Життя:", your_hero2.hp, "Монети:", your_hero2.money, "Атака:", your_hero2.attack)
        your_hero = your_hero2
        break
    else:
        print("Неправильний вибір. Будь ласка, виберіть G або N.")

# Обработка выбора магазина или босса
while True:
    vubir = input("Магазин(N), Бос(B): ")
    if vubir == "N":
        while True:
            vubir2 = input("Сапоги Гермеса:20(S), Опудало сороконіжки:50(O), Вихід(B): ")
            if vubir2 == "S":
                print("Дякую за покупку!")
                your_hero.hp += 20
                your_hero.money -= 20
                magazin = 1
                break
            elif vubir2 == "O":
                print('Дякую за покупку!')
                your_hero.hp -= 20
                your_hero.money -= 50
                your_hero.attack += 30
                magazin = 2
                break
            elif vubir2 == "B":
                print("Вихід з магазину.")
                break
            else:
                print("Неправильний вибір. Будь ласка, виберіть S, O або B.")
        break
    elif vubir == "B":
        print("Ви йдете у печеру до босса")
        break
    else:
        print("Неправильний вибір. Будь ласка, виберіть N або B.")

print("Життя:", your_hero.hp, "Монети:", your_hero.money, "Атака:", your_hero.attack)

if magazin == 1 or magazin == 2:
    while True:
        vubir3 = input("У вас є новий шмот, підете на босса?: Так(Y), Ні(N): ")
        if vubir3 == "Y":
            print("Ви йдете на босса!")
            break
        elif vubir3 == "N":
            print("Ви вирішили не йти на босса.")
            break
        else:
            print("Неправильний вибір. Будь ласка, виберіть Y або N.")
