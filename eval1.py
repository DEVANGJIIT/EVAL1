emp={ }
n=int(input("Enter no of inital entries "))
for i in range(0,n):
    ID=int(input("Enter id "))
    name=input("Enter name ")
    department=input("Enter department ")
    salary=int(input("Enter salary "))

    empval={
        "name":name,
        "department":department,
        "salary":salary
        }
    emp[ID]=empval



def add_details():
    ID=int(input("Enter id "))
    name=input("Enter name ")
    department=input("Enter department ")
    salary=int(input("Enter salary "))

    empval={
        "name":name,
        "department":department,
        "salary":salary
        }
    emp[ID]=empval

def emp_search():
    Id=int(input("Enter id of the emp "))
    print("name of the emp is ",emp[Id]["name"])
    print("department of the emp is ",emp[Id]["department"])
    print("salary of the emp is ",emp[Id]["salary"])

def update_detail():
    Id=int(input("Enter id of the emp "))
    print("1-change name ")
    print("2-change department ")
    print("3-change salary ")
    choice=int(input("Enter you choice "))
    if choice==1:
        name=input("enter new name ")
        emp[Id]["name"]=name
    elif choice==2:
        department=input("enter new department ")
        emp[Id]["department"]=department

    elif choice==3:
        salary=int(input("enter new salary "))
        emp[Id]["salary"]=salary

    else:
        print("wrong input")

    
def department_data():
    a=[]
    for Id in emp:
        a.append(emp[Id]["department"])

    set(a)
    for department in a:
        print("for department= ",department)
        for Id in emp:
            if emp[Id]["department"]==department:
                print("Id of the emp is ",Id)
                print("name of the emp is ",emp[Id]["name"])
                print("department of the emp is ",emp[Id]["department"])
                print("salary of the emp is ",emp[Id]["salary"])
   
        



print()
print("1-add details ")
print("2-update details ")
print("3-search emp ")
print("4-department wise data ")
print("5-to end")

while(1):
    choice=int(input("Enter you choice "))

    if choice==1:
        add_details()
        print()

    elif choice==2:
        update_detail()
        print()
       
    elif choice==3:
        emp_search()
        print()
        
    elif choice==4:
        department_data()
        print()
        
    elif choice==5:
        break

    else:
        print("wrong input")

   



