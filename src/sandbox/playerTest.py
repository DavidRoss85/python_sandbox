

class Character:
    def __init__(self,name,level,hp,mp,atk,blk):
        self.name=name
        self.level=level
        self.hp=hp
        self.mp=mp
        self.atk=atk
        self.blk=blk
        self.max_hp = hp
        self.max_mp = mp
        self.curr_atk = atk
        self.curr_blk = blk
        self.target = self
        self.team = None
        self.command_dict={
            "Attack":self.attack,
            "Defend":self.defend,
        }

    def attack(self):
        print(f"{self.name} attacks {self.target.name}")
        self.target.receive_attack(self.curr_atk)

    def defend(self):
        pass

    def receive_attack(self,atk):
        self.hp -= atk
        print(f"{self.name} loses {atk} HP")

    def update_dictionary(self,command):
        self.command_dict.update(command)

    def call_command(self,command):
        self.command_dict[command]()

    def __str__(self):
        return (
            f"{self.name}: \n"
            f" LEVEL: {self.level}\t"
            f" HP: {self.hp}\t"
            f" MP: {self.mp}\t"
            f" ATK: {self.atk}\t"
            f" DEF: {self.blk}"
        )

class Fighter(Character):
    def __init__(self,name, level, hp, mp, atk, blk):
        Character.__init__(self,name,level,hp, mp, atk, blk)
        self.fighter_commands={
            "Get pumped": self.fight_stuff
        }

    def fight_stuff(self):
        print("fight")


class Magus(Character):
    def __init__(self, name, level, hp, mp, atk, blk):
        Character.__init__(self, name, level, hp, mp, atk, blk)
        self.magus_commands={
            "Perform Magic": self.magic_stuff
        }

    def magic_stuff(self):
        print("Magic stuff")


class Playable(Magus,Fighter):
    def __init__(self,name, level, hp, mp, atk, blk):
        Magus.__init__(self,name, level,hp,mp,atk,blk)
        Fighter.__init__(self, name, level, hp, mp, atk, blk)
        self.update_dictionary(self.fighter_commands)
        self.update_dictionary(self.magus_commands)



class Team:
    def __init__(self,name,members):
        self.name = name
        self.members = members
        self.current_character = members[0]

    def add_team_member(self, player):
        if player.team is None:
            self.members.append(player)
            print(f"{player.name} joined {self.name}")
        else:
            print(f"{player.name} is already on a team")

    def switch(self,player):
        self.current_character=player
        print(f"{self.name} switched to {player.name}")

    def attack(self):
        self.current_character.attack()

    def list_members(self):
        print(f"{self.name}:")
        for member in self.members:
            print(member)

    def aim(self,target):
        self.current_character.target = target


a = Playable("Me",1,100,100,1,1)
b = Playable("Johnny",1,100,100,1,1)
c = Playable("Mika",1,100,100,1,1)
d = Playable("Tan",1,100,100,1,1)
e = Playable("Sari",1,100,100,1,1)
f = Playable("Doti",1,100,100,1,1)

team1= Team(" *** Player 1 ***",[a,b,c])
team2= Team(" *** CPU ***",[d,e,f])

team1.list_members()
print("\nvs\n")
team2.list_members()

print("\n\n")
team1.switch(a)
team1.aim(team2.current_character)
team1.attack()

team2.switch(f)
team2.aim(team1.current_character)
team2.attack()

team1.current_character.call_command("Attack")




