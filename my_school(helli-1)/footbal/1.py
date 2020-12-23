class Team :
    def __init__(self , all):
        name, country, ligName, score = tuple(all.split(' '))
        self.name = name
        self.country = country
        self.ligName = ligName
        self.score = int(score)
    def biger_Theb_50(self):
        if self.score > 50:
            return 1
        else:
            return 0
all_team=[]
indexer = 0
for i in range(int(input())):
    all_team.append(Team(input("")))
for i in all_team:
    indexer += i.biger_Theb_50()
print(indexer)