import pymysql as sql
import bcrypt as bc
import tkinter as tk
import datetime as dt
import base64 as b64 
from tkinter import IntVar
import tkMessageBox as tkMB


database = "imagedb"
creds = open("secret\SqlServerUsrPass.txt", "r").readlines()
server_username = b64.b64decode(creds[0]).decode("utf-8")
server_password = b64.b64decode(creds[1]).decode("utf-8")

imagedb = sql.connect("imagecollageapcsp.mysql.database.azure.com", server_username[:-1] + "@imagecollageapcsp", server_password, database)

cursor = imagedb.cursor()

# All my functions
def goToSignInScreen():
    create.withdraw()
    signIn.iconify()
    signIn.deiconify()

def goToCreateAccountScreen():
    signIn.withdraw()
    create.iconify()
    create.deiconify()


def initSignInWindow():
    signIn.mainloop()
    

def initCreateAccountWindow():
    create.mainloop()

    
def createAccount():
    username = createUserNameInput.get()
    password = createPassWordInput.get()
    salt = bc.gensalt()
    dateOfCreation = str(dt.datetime.now())
    adult = adultcheck.get()
    if(username != "" or password != ""):
        cursor.execute("INSERT INTO users VALUES(%s, %s, %s, %d)", (username, bc.hashpw(password, salt), dateOfCreation, adult))
    else: 
        tkMB.showerror("Error!", "You are missing some info")



# Sign In window declerations
signIn = tk.Tk("SignIn")
signIn.geometry("1000x700")
signIn.state('zoomed')

userNameLabel = tk.Label(signIn, text = "Username")
userNameLabel.pack()
userNameLabel.place(height = 40, width = 80, x = 580, y = 330)

userNameInput = tk.Entry(signIn, bd = 5)
userNameInput.pack()
userNameInput.place(height = 40, width = 200 ,x = 650, y = 330)


passWordLabel = tk.Label(signIn, text = "Password")
passWordLabel.pack()
passWordLabel.place(height = 40, width = 80, x = 580, y = 380)

passWordInput = tk.Entry(signIn, bd = 5, show = "*")
passWordInput.pack()
passWordInput.place(height = 40, width = 200 ,x = 650, y = 380)

logInBtn = tk.Button(signIn, text = "Sign In")
logInBtn.pack()
logInBtn.place(height = 30, width = 200, x = 650, y = 430)

createAccountBtn = tk.Button(signIn, text = "Create an Account", command = goToCreateAccountScreen)
createAccountBtn.pack()
createAccountBtn.place(height = 30, width = 200, x = 650, y = 470)


# Create Account decleration
create = tk.Tk("Create your account")
create.geometry("1000x700")
create.state('zoomed')    

createUserNameLabel = tk.Label(create, text = "Username")
createUserNameLabel.pack()
createUserNameLabel.place(height = 40, width = 80, x = 580, y = 330)

createUserNameInput = tk.Entry(create, bd = 5)
createUserNameInput.pack()
createUserNameInput.place(height = 40, width = 200 ,x = 650, y = 330)

createPassWordLabel = tk.Label(create, text = "Password")
createPassWordLabel.pack()
createPassWordLabel.place(height = 40, width = 80, x = 580, y = 380)

createPassWordInput = tk.Entry(create, bd = 5, show = "*")
createPassWordInput.pack()
createPassWordInput.place(height = 40, width = 200 ,x = 650, y = 380)

adultcheck = IntVar()
adultCheck = tk.Checkbutton(text = "Are you older than 18? Check the box if yes", variable = adultcheck)
adultCheck.pack()
adultCheck.place(height = 30, width = 250, x = 650, y = 410)

createLogInBtn = tk.Button(create, text = "Create Account and Logon", command = createAccount)
createLogInBtn.pack()
createLogInBtn.place(height = 30, width = 200, x = 650, y = 450)

exitBtn = tk.Button(create, text = "Exit to Sign In screen", command = goToSignInScreen)
exitBtn.pack()
exitBtn.place(height = 30, width = 200, x = 650, y = 480)






initSignInWindow()