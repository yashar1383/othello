class student :
    def __init__(self,name , grade , class_No):
        self.name = name
        self.grade = grade
        self.class_No = class_No
def create_student (all):
    all = all.split(' ')
    return student(all[0] , all[1] , all[2])
give = lambda a,b : b.grade == a[0] and b.class_No == a[1]
n=int(input())
all_STU = []
for i in range(n):
    all_STU.append(create_student(input()))
m=input().split(' ')
index = 0
for i in all_STU :
    if give(m,i) == True :
        index += 1
print(index)