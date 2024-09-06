import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="Hpolara@5",database="machine")
cursor=con.cursor()

def insert_data():
    id=int(input("Enter employee id:"))
    name=input("Enter employee name:")
    salary=int(input("Enter employee salary:"))
    query="insert into emp values({},'{}',{})".format(id,name,salary)
    cursor.execute(query)
    con.commit()
    print("Data inserted...")

def update_data():
    id=int(input("Enter employee id:"))
    salary=int(input("Enter employee salary:"))
    query="update emp set salary={} where id={}".format(salary,id)
    cursor.execute(query)
    con.commit()
    if cursor.rowcount > 0:
        print("Data updated....")
    else:
        print("No data found")

def delete_data():
    id=int(input("Enter employee id:"))
    query="delete from emp where id={}".format(id)
    cursor.execute(query)
    con.commit()
    if cursor.rowcount > 0:
        print("Data deleted....")
    else:
        print("No data found")

def read_data():
    cursor.execute("select * from emp")
    record=cursor.fetchall()
    for i in record:
        print(i)
    print("Total records:",cursor.rowcount)

while True:
    print("\nOptions:")
    print("1. insert data")
    print("2. update data")
    print("3. delete data")
    print("4. read data")
    print("5. exit")

    ch = input("Enter your choice:")

    if ch=='1':
        insert_data()
    elif ch=='2':
        update_data()
    elif ch=='3':
        delete_data()
    elif ch=='4':
        read_data()
    elif ch=='5':
        break
    else:
        print("Invalid choice")

        
