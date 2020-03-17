import pymysql as sql
import bcrypt 
import tkinter as tk
import base64 

database = "imagedb"
creds = open("C:\\Users\Administrator\Desktop\ImageDB\secret\SqlServerUsrPass.txt", "r")
print(creds)

imagedb = sql.connect("imagecollageapcsp.mysql.database.azure.com", "theLordAndSavior@imagecollageapcsp", "MyNameJeff69420", database)

cursor = imagedb.cursor()

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
    cursor.execute("INSERT imagedb FROM users WHERE username =%s'", (createUserNameInput.get(), ))


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

createLogInBtn = tk.Button(create, text = "Create Account and Logon")
createLogInBtn.pack()
createLogInBtn.place(height = 30, width = 200, x = 650, y = 430)

exitBtn = tk.Button(create, text = "Exit to Sign In screen", command = goToSignInScreen)
exitBtn.pack()
exitBtn.place(height = 30, width = 200, x = 650, y = 460)





initSignInWindow()