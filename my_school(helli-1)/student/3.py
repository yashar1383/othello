class student :
    def __init__(self,name , grade , class_No , Nall):
        self.name = name
        self.grade = int(grade)
        self.class_No = int(class_No)
class teacher :

    def __init__(self,name , age , field , Nall):
        self.name = name
        self.age = int(age)
        self.field = field
class Lesson :
     def __init__(self, name , teacher_name , grad , class_No ):
         self.name = name
         self.teacher_name = teacher_name
         self.grad = int(grad)
         self.class_No = int(class_No)
def create (functions_name,all):
    all = all.split(' ')
    all.append(' ')
    return functions_name(all[0] , all[1] , all[2] , all[3])
teachers = {}
students =[]
all=[]
for i in range(int(input())) :
    students.append(create(student,input()))
for i in range(int(input())):
    teachers[create(teacher,input()).name] = []
for j in range(int(input())):
    inp = input()
    s = create(Lesson,inp)
    if s.teacher_name in list(teachers.keys()) :
        teachers[s.teacher_name].append(s)
inpp=input()
index = 0
for i in teachers[inpp]:
    all.append((i.grad , i.class_No))
for i in students :
    if tuple([i.grade , i.class_No]) in all :
        index += 1
print(index)