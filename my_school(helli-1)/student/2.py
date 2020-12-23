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
n1=int(input())
for i in range(n1):
    teachers[create(teacher,input()).name] = []
n2 = int(input())
for j in range(n2):
    inp = input()
    s = create(Lesson,inp)
    if s.teacher_name in list(teachers.keys()) :
        teachers[s.teacher_name].append(s)
name = input()
print(len(teachers[name]))