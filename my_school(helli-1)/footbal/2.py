class Team :
    def __init__(self , all):
        all = tuple(all.split(' '))
        self.name = all[0]
        self.country = all[1]
        self.ligName = all[2]
        self.score = int(all[3])
    def biger_Theb_50(self):
        if self.score > 50:
            return 1
        else:
            return 0
class Player :
    def __init__(self , all):
        all = tuple(all.split(' '))
        self.name = all[0]
        self.country = all[1]
        self.age = int(all[2])
        self.team = all[3]
    def in_his_country(self):
        for i in all_team:
            if i.name == self.team and i.country == self.country:
                return 1
            else:
                return 0
all_team=[]
all_player = []
indexer = 0
for i in range(int(input())):
    all_player.append(Player(input("")))
for i in range(int(input())):
    all_team.append(Team(input("")))

for i in all_player:
    indexer += i.in_his_country()
print(indexer)