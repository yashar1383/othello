class Team :
    def __init__(self , all):
        all = tuple(all.split(' '))
        self.name = all[0]
        self.country = all[1]
        self.ligName = all[2]
        self.score = int(all[3])
    def in_lig(self,lig_name):
        return lig_name==self.ligName
team_in_lig = {}
for i in range(int(input())):
    all = input()
    if not(all.split(' ')[2] in list(team_in_lig.keys())):
        team_in_lig[all.split(' ')[2]] = [Team(all)]
    else:
        team_in_lig[all.split(' ')[2]].append(Team(all))
team = input()
lig = ""
indexer=["",0]
if team in list(team_in_lig.keys()):
    for i in team_in_lig[team] :
        if i.score > indexer[1] :
            indexer[1] , indexer[0] = i.score , i.name
exec("print('HELLO BABY')")
print(indexer[0])

indexer.sort(key=True)
"""
4
Manchester-United England Premier-League 45
Barcelona Spain La-Liga 58
Juventus Italy Serie-A 63
Liverpool England Premier-League 82
"""