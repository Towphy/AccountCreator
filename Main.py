from termcolor import colored
import os
from tinydb import TinyDB, Query
import time

import socket
getIp = socket.gethostbyname(socket.gethostname())

db = TinyDB('Users.json')
UsersDb = Query()

LoginErrorMsg = ""


def StartUp():
	LoC = input("Login or Signup?: ")
	if LoC.lower() == "login":
		Login()
	elif LoC.lower() == "signup":
		CreateAccount()
	else:
		print("Error: Try Again | Spelling Error")

def Login():
	global LoginErrorMsg
	os.system('cls' if os.name == 'nt' else 'clear')

	print(f"LOGIN\n\n{LoginErrorMsg}")
	EnterUsername = input("Username: ")
	EnterPassword = input("Password: ")
	SearchUsername = db.search(UsersDb.Username == EnterUsername)
	if not SearchUsername:
		LoginErrorMsg =  colored("[Error]", "red", attrs = ["bold"]) + " Username Does Not Exist"
		Login()
	else: 
		if EnterPassword != SearchUsername[0].get("Password"):
			LoginErrorMsg = colored("[Error]", "red", attrs = ["bold"]) + " Wrong Password"
			Login()
		else:
			print("\nSuccessfully Logined")
			


CreateAccErrorMsg = ""

def CreateAccount():
	global CreateAccErrorMsg
	print(f"-~=Account Creation=~-\n\n{CreateAccErrorMsg}")
	makeUsername = input("Username: ")
	makePassword = input("Password: ")
	SearchUsername = db.search(UsersDb.Username == makeUsername)
	if not SearchUsername:
		print("Successfully Created Account")
		db.insert({'Username': makeUsername, 'Password': makePassword, "ip" : getIp})
		print("\nReloading In 5 Seconds")
		time.sleep(5)
		Login()

	else:
		CreateAccErrorMsg = colored("[Error]", "red", attrs = ["bold"]) + " Username Is Already In Use"
		os.system('cls' if os.name == 'nt' else 'clear')
		CreateAccount()


StartUp()
