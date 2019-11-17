import json
import os
import time
import random

specialChars = ["!","@","#","$","%","^","*"]
numbers = [1,2,3,4,5,6,7,8,9,0]
alphabet = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K" "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p" ,"Q", "q", "R", "r", "S", "s", "T", "t", "U", "u","V", "v","W", "w", "X", "x", "Y", "y", "Z", "z"]

accounts = json.load(open("passwords.json"))

def clear():
    os.system('cls')

def searchData(data, location):
    for i in location:
        if i == data:
            return True

    return False

def main():
    clear()
    print("Type 'password' to generate password")
    print("Type 'add' to add website")
    print("Type site name that you want data for it")
    data = input("> ")

    if data == "add":
        addPage()

    elif data == "password":
        clear()
        print(generatePassword())
        time.sleep(5)
        main()

    if searchData(data, accounts):
        for info in accounts[data]:
            clear()
            print("Username: ")
            print(info["username"])
            print("\nE-mail: ")
            print(info["email"])
            print("\nPassword: ")
            print(info["password"])
            time.sleep(3.5)
            main()

    elif searchData(data, accounts) !=  True:
        print("We don't have account data to this site. Check if this site exists, if exsists check if you have account and check if your login data to this site is current")
        time.sleep(1.5)
        main()

def addPage():
    clear()
    print("Adding Page:")
    pageName = input("Page > ")
    username = input("Username (if doesn't exsists type 'null')> ")
    email = input("Email > ")
    password = input("Password > ")

    accounts.update({pageName:[{"username": username, "email": email, "password" : password}]})

    with open("passwords.json","w") as f:
        json.dump(accounts, f, indent = 4)

    print("Added")
    main()

def generatePassword():
    password = ""
    while True:
        password += random.choice(alphabet) + str(random.choice(numbers)) + random.choice(specialChars)

        if len(password) == 18:
            return password
            
main()