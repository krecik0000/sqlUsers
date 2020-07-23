import pymysql
import os
from termcolor import colored

name = ""
password = ""
email = ""

def showUser():
    cursor.execute("SELECT * FROM Users")
    records = cursor.fetchall()
    if cursor.rowcount != 0:
        print("Total Users:",colored(cursor.rowcount, 'green'))
    else:
        print("Total Users:",colored(cursor.rowcount, 'red'))
    for row in records:
        print("----------")
        print(colored("Id","yellow") + "       | ",colored(row[0],"yellow"))
        print("----------")
        print(colored("Name","yellow") + "     | ",colored(row[1],"yellow"))
        print("----------")
        print(colored("Password","yellow") + " | ",colored(row[2],"yellow"))
        print("----------")
        print(colored("Email","yellow") + "    | ",colored(row[3],"yellow"))
        print("----------\n")
        con = 0
        try:
            print("|1|Back")
            con = int(input(":"))
            if con == 1:
                os.system("cls")
            else:
                print("Ops! incorrect key")
        except ValueError:
            print("Ops! incorrect key")
        os.system("cls")

def addUser(name,password,email):
    print("Name: ")
    name = input(":")
    print("Password: ")
    password = input(":")
    print("Email: ")
    email = input(":")
    cursor.execute("INSERT INTO Users (name, password, email) VALUES (%s,%s,%s)", (name,password,email))
    os.system("cls")

def dellUser():
    remove = ""
    print("Which User you want to remove?")
    remove = input("Type name: ")
    cursor.execute("DELETE FROM Users WHERE name=%s", remove)
    os.system("cls")

def menu(name,password,email):
    choice = 0
    while choice != 4:
        print("|1|Show list")
        print("|2|Add Users")
        print("|3|Dell Users")
        print("|4|Exit")
        try:
            choice = int(input(":"))
            os.system("cls")
            if choice == 1:
                showUser()
            elif choice == 2:
                addUser(name,password,email)
            elif choice == 3:
                dellUser()
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

