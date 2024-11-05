

class MyClass:
    def __init__(self,randomtext):
        self.displaytext=randomtext

    def showtext(self):
        print(self.displaytext)



class Character:
    def __init__(self,name,level,hp,mp):
        self.name=name
        self.level=level
        self.hp=hp
        self.mp=mp

    def __str__(self):
        return f"{self.name}: {self.level}"

    def show_hp(self):
        print(f"HP: {self.hp}")


class Player(Character):

    def __init__(self,name,level,hp,mp,ability_list):
        Character.__init__(self,name,level,hp,mp)
        self.my_characters=[]
        self.abilities=ability_list
        i=0
        self.ability_name=[]
        for ability in self.abilities:
            self.ability_name.append(ability)
            i+=1
        self.add_character(self)
        self.current_character = self

    def list_abilities(self):
        for ability in self.abilities:
            print(ability)

    def add_character(self,player):
        self.my_characters.append(player)


def attack_player(player,atk):
    player.hp-=atk
    player.show_hp()

def switch_character(player1=Player,player2=Player):
    player1.current_character = player2


test_abilities = {
    "Attack" : attack_player,
    "Defend": "",
    "Summon": switch_character,
    "Special":"",
    "Run":""
}

a= Player("David",5,100,100,test_abilities)
b= Player("John",5,100,100,test_abilities)
c= Player("Vick",5,100,100,test_abilities)
d= Player("Mary",5,100,100,test_abilities)


current_player = a

print(current_player.current_character)

current_player.abilities["Summon"](current_player,b)

print(current_player.current_character)