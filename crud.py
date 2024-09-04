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

# def update_data():
#     id=int(input("Enter employee id:"))
#     salary=int(input("Enter employee salary:"))
#     query="update emp set "
insert_data()