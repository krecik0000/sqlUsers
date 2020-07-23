import pymysql

name = ""
password = ""
email = ""

def addUser(name,password,email):
    print("Name: ")
    name = input(":")
    print("Password: ")
    password = input(":")
    print("Email: ")
    email = input(":")
    cursor.execute("INSERT INTO Users (name, password, email) VALUES (%s,%s,%s)", (name,password,email))

def menu(name,password,email):
    choice = 0
    while choice != 4:
        print("|1|Show list")
        print("|2|Add Users")
        print("|3|Dell Users")
        print("|4|Exit")
        try:
            choice = int(input(":"))
            if choice == 1:
                cursor.execute("SELECT * FROM Users")
                records = cursor.fetchall()
                print("Total Users: ", cursor.rowcount)
                for row in records:
                    print("----------")
                    print("Id       | ", row[0])
                    print("----------")
                    print("Name     | ", row[1])
                    print("----------")
                    print("Password | ", row[2])
                    print("----------")
                    print("Email    | ", row[3])
                    print("----------\n")
            elif choice == 2:
                addUser(name,password,email)
            elif choice == 3:
                print("3")
            elif choice == isinstance(choice, str) and choice != 1 and choice != 2 and choice != 3 and choice != 4:
                print("Ops! incorrect key")
        except ValueError:
            print("Ops! incorrect key")

db = pymysql.connect("localhost","root","","python" ) #connecting to Database

cursor = db.cursor()

create = """CREATE TABLE IF NOT EXISTS Users (
    id_user INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(20) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_user)
) DEFAULT CHARSET=utf8"""

try:
   cursor.execute(create)
   menu(name,password,email)
   db.commit()
except:
   db.rollback()

db.close()

