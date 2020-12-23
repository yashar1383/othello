people = []
times = {}
event = {'+' : 1 , '-':-1}
count = 0
for i in range(int(input())):
               inp = input().split()[1:]
               people.append(tuple(inp))
people.sort(key=lambda x : x[0])
for i,j in people :
    #print(i,j,event[j])
    count += event[j]
    times[i] = count 
times = sorted(list(times.items()),key=lambda x : x[1],reverse = True)
#if times[0][2] == '-':
#    Hour,Min = times[0][0].split()
#    print(f"{int(Hour)}:{int(Min)}")
print(times[0][0])
    
               
