from abc import ABC, abstractmethod
from random import randint

class Item(ABC):
    def __init__(self, name:str, health = 500):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self):
        pass

class Sword(Item): # Це наслідування
    def __init__(self, name, attack_power:int):
        super().__init__(name=name) #  Це виклик конструктора наслідуваного класу
        self.__attack_power = attack_power # приватний атрибут який реалізує інкапсуляцію
        self._sharp = 0
    
    def attack(self, another_item:Item): # ми не можемо створити клас без цього методу
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"Завдаємо удару мечем {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"
    
    @property
    def get_attack_power(self):
        return f"Атака меча {self.name}: {self.__attack_power + self._sharp} одиниць"
    
    def sharpening(self):
        self._sharp += 1

class Axe(Item): # Це наслідування
    def __init__(self, name, attack_power:int):
        super().__init__(name=name) #  Це виклик конструктора наслідуваного класу
        self.__attack_power = attack_power # приватний атрибут який реалізує інкапсуляцію
        self._sharp = 0
    
    def attack(self, another_item:Item):  # ми не можемо створити клас без цього методу
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return f"Завдаємо удару сокирою {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"

    @property
    def get_attack_power(self):
        return f"Атака сокири {self.name}: {self.__attack_power + self._sharp} одиниць"

S = Sword("Ескалібур", 100)
A = Axe("Кратос", 95)


class Bow(Item):  # Це наслідування
            def __init__(self, name, attack_power:int, range_power:int):
                super().__init__(name=name)
                self.__attack_power = attack_power
                self._range_power = range_power
            
            def attack(self, another_item:Item):  
                current_attack = self.__attack_power + randint(5, 15) + self._range_power
                another_item.health -= current_attack
                return f"Завдаємо удару луком {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"

            @property
            def get_attack_power(self):
                return f"Атака лука {self.name}: {self.__attack_power + self._range_power} одиниць"

            def reload(self):
                self._range_power += 1

weapons = [S, A, Bow("Лук", 80, 5)]
current_weapon = weapons[randint(0, 2)]

while S.health > 0 and A.health > 0:
            print(f"Хід: {current_weapon.name}")
            action = input("Виберіть дію (attack/sharpen/reload): ").strip().lower()

            if action == "attack":
                if isinstance(current_weapon, Bow):
                    print(current_weapon.attack(A))
                else:
                    print(current_weapon.attack(S))
            elif action == "sharpen" and isinstance(current_weapon, Sword):
                current_weapon.sharpening()
                print(f"{current_weapon.name} підсилено!")
            elif action == "reload" and isinstance(current_weapon, Bow):
                current_weapon.reload()
                print(f"{current_weapon.name} перезаряджено!")
            
            if S.health <= 0:
                print(f"Перемога за {A.name}")
                break
            if A.health <= 0:
                print(f"Перемога за {S.name}")
                break

            current_weapon = weapons[randint(0, 2)]