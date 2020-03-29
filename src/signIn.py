import pymysql as sql
import bcrypt as bc
import tkinter as tk
import datetime as dt
import base64 as b64 
from tkinter import IntVar
import tkinter.messagebox as mb
import createAccount as cA





#Establish a connection from the app to the database
def establish_connection():

    database = "imagedb"
    creds = open("secret\SqlServerUsrPass.txt", "r").readlines()
    server_username = b64.b64decode(creds[0]).decode("utf-8")
    server_password = b64.b64decode(creds[1]).decode("utf-8")

    imagedb = sql.connect("imagecollageapcsp.mysql.database.azure.com", server_username[:-1] + "@imagecollageapcsp", server_password, database)

    cursor = imagedb.cursor()


# def goToSignInScreen():
#     create.widthraw()
#     signIn.iconify()
#     signIn.deiconify()



def initSignInWindow():
    signIn.mainloop()
    




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

createAccountBtn = tk.Button(signIn, text = "Create an Account", command = cA.createAccountScreen.goToCreateAccountScreen)
createAccountBtn.pack()
createAccountBtn.place(height = 30, width = 200, x = 650, y = 470)





# open the sign in form
initSignInWindow()