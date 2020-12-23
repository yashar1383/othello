class Student:

    def __init__(self, username):
        self.username = username

    def show(self):
        print(self.username)

new_std = Student("Mojtaba")
students = [new_std]

while True:
    cmd = input("command? ")
    if cmd == "add student":
        username = input("username? ")
        new_std = Student(username)
        students.append(new_std)
    elif cmd=='show students':
        for st in students:
            st.show()
    elif cmd=='show student':
        un=input('username? ')
        fl=True
        for st in students:
            if st.username ==un:
                st.show()
                fl=False
                break
        if fl:
            print('yaft nashod')
    elif cmd=='del student':
        un=input('username? ')
        c=0
        for st in students:
            if st.username ==un:
                students.pop(c)
                break
            c+=1
        else:
            print('yaft nashod')

