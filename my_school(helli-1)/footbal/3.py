class Team :
    def __init__(self , all):
        all = tuple(all.split(' '))
        self.name = all[0]
        self.country = all[1]
        self.ligName = all[2]
        self.score = int(all[3])
    def in_lig(self,lig_name):
        return lig_name==self.ligName
all_team=[]
indexer = [0,None]
for i in range(int(input())):
    all_team.append(Team(input("")))
Team_lig = input("")
for i in all_team:
    if i.in_lig(Team_lig) and i.score > indexer[0]:
        indexer[0] , indexer[1] = i.score , i.name
print(indexer[1])