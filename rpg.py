import random

class Character:
    """Player character"""
    def __init__(self, name):
        self.name = name
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack_power = 20
        self.exp = 0
        self.level = 1
        self.next_level_exp = 100

    def show_status(self):
        """print current conditon"""
        print(f"\n[condition of {self.name}]")
        print(f"Lv. {self.level}")
        print(f"HP: {self.hp} / {self.max_hp}")
        print(f"striking power: {self.attack_power}")
        print(f"experience: {self.exp} / {self.next_level_exp} ")
        print("-" * 20)

    def attack(self, target):
        """give damage by attacking"""
        damage = random.randint(self.attack_power -2, self.attack_power +2)
        print(f"\n 🤺attack of {self.name}, give {target.name} {damage}")
        target.take_damage(damage)

    def take_damage(self, damage):
        """getting damage"""
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        print(f"❤️ {self.name}stamina: {self.hp}/{self.max_hp}")

    def gain_exp(self, amount):
        """experience point and level up"""
        print(f"⭐{amount} gained experience point")
        self.exp += amount
        if self.exp >= self.next_level_exp:
            self.level_up()
    
    def level_up(self):
        """plus level-up"""
        self.level += 1
        self.exp -= self.next_level_exp
        self.next_level_exp = int(self.next_level_exp * 1.2)
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack_power += 5
        print(f"\n 🥳Congratulation! your level increased at {self.level}")
        print(f"💪maximum stamina increased at {self.max_hp}, aggressive strength increased at {self.attack_power} \n")

class Monster:
    """Monster class"""
    def __init__(self, name, hp, attack_power, exp_reward):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.exp_reward = exp_reward

    def attack(self, target):
        """Giving damage by attacking"""
        damage = random.randint(self.attack_power -1, self.attack_power +1)
        print(f"\n 👾attack of {self.name}! give {target.name} {damage}")
        target.take_damage(damage)
    def take_damage(self, damage):
        """gain damage"""
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        print(f"👾 stamina of {self.name}: {self.hp}/{self.max_hp}")

def get_random_monster():
    """generating random monster"""
    mosters = [
    Monster("slim", 30, 5, 20),
    Monster("goblin", 50, 8, 40),
    Monster("oak", 80, 12, 70),
    Monster("dragon", 200, 25, 30),
    ]

    return random.choice(mosters)

def battle(player, monster):
    """cambat ready"""
    print(f"\n 🚨 {monster.name} appeared")

    while monster.hp > 0 and player.hp > 0:
        print(f"\n-- turn of {player.name}")
        print("1. attack")
        print("2. escaping")
        choice = input("choose behavior: ")

        if choice == "1":
            player.attack(monster)
            if monster.hp > 0:
                monster.attack(player)
        elif choice == '2':
            print("successfuly escaped")
            return
        else:
            print("wrong input")
            continue

        if player.hp == 0:
            print(f"🦴{player.name}lost.. Game over")
            return
        
        if monster.hp == 0:
            print(f"\n🏆defeat {monster.name}")
            player.gain_exp(monster.exp_reward)
        



def main():
    print("=" * 45)
    print("   Welcome to RPG game.")
    print("=" * 45)
    name = input("Put player's name: ")
    player = Character(name)

    while True:
        print("=" * 20)
        print("1. 🌳go for exploration")
        print("2. 📆check condition")
        print("3. 🔚end")
        print("=" * 20)
        choice = input("what would you do?: ")

        if choice == '1':
            monster = get_random_monster()
            battle(player, monster)
            if player.hp ==0:
                break
        elif choice == '2':
            player.show_status()
        elif choice == '3':
            print("Game is over. It was a fun experience. 🤚")
            break
        else:
            print("It is wrong input.")
    

main()