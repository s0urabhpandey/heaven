from database import Database
#create and connect to database
db=Database()
while True:
    print('1.add')
    print('2.view')
    print('3.exit')
    option=input("select no.>>>>")
    if option=='1':
        print("enter student details")
        nm=input("NAME:")
        cls=input('CLASS:')
        section=input("SECTION:")
        age=input("AGE:")

        if nm and cls and section and age.isnumeric():
            status=db.add(nm,cls,section,age)
            print(status.lastrowid)
            if status.lastrowid!=-1:
                print("success")
        else:
            print("invalid data")
    elif option=='2':
        data=db.view()
        for record in data:
            print(record)
    elif option=='3':
        print("bye")
        break
    else:
        print("retry!!")
