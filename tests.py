class Student:
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    # Function to display student details
    def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")
        if input():
           print()

    # Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if (ls[i].rollno == rn):
                return i

    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]

    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll

def accept():
    name = input("1.Enter name")
    roll = int(input("2.Enter roll"))
    marks1 = int(input("3.Enter marks one"))
    marks2 = int(input("3.Enter marks two"))
    obj = Student(name, rollno=roll, m1=marks1,m2=marks2)
    ls.append(obj)
    return obj
# Create a list to add Students
ls = []
# an object of Student class
# obj = Student('', 0, 0, 0)
while True:
    print("\n\t\t****STUDENT MANAGEMENT SYSTEM****")
    print("\nOperations used, ")
    print("\n1.Accept Student details:")
    print("\n2.Display Student Details:")
    print("\n3.Search Details of a Student:")
    print("\n4.Delete Details of Student")
    print("\n5.Update Student Details\n6.Exit")
    print("\n6.Exit\n")

    ch = int(input("Enter choice:"))
    if (ch == 1):
        obj = accept()

    elif (ch == 2):
        print("\n")
        print("\nList of Students\n")
        for i in range(ls.__len__()):
            obj.display(ls[i])
            break

    elif 3 == ch:
        print("\n Student Found, ")
        s = obj.search(2)
        obj.display(ls[s])
        break

    elif ch == 4:
        obj.delete(2)
        print(ls.__len__())
        print("List after deletion")
        for i in range(ls.__len__()):
            obj.display(ls[i])
            break

    elif ch == 5:
        obj.update(3, 2)
        print(ls.__len__())
        print("List after updation")
        for i in range(ls.__len__()):
            obj.display(ls[i])
            break

    else:
        print("Thank You !")
        break