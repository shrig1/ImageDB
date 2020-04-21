import pymysql as sql
import bcrypt as bc
import tkinter as tk
import datetime as dt
import base64 as b64 
from tkinter import IntVar
import tkinter.messagebox as mb
import signIn as sI







def createAccountScreen():


    def goToCreateAccountScreen():
        sI.signIn.withdraw()
        create.iconify()
        create.deiconify()





    def initCreateAccountWindow():
        create.mainloop()

    
    def createAccount():

        database = "imagedb"
        creds = open("secret\SqlServerUsrPass.txt", "r").readlines()
        server_username = b64.b64decode(creds[0]).decode("utf-8")
        server_password = b64.b64decode(creds[1]).decode("utf-8")

        imagedb = sql.connect("imagecollageapcsp.mysql.database.azure.com", server_username[:-1] + "@imagecollageapcsp", server_password, database)

        cursor = imagedb.cursor()

        username = createUserNameInput.get()
        password = bytes(createPassWordInput.get(), "utf-8")
        salt = bc.gensalt()
        dateOfCreation = str(dt.datetime.now())
        adult = str(adultcheck.get())
        if(username != "" or password != ""):
            cursor.execute("INSERT INTO users VALUES(%s, %s, %s, %s)", (username, bc.hashpw(password, salt), dateOfCreation, adult))
        else: 
            mb.showerror("Error!", "You are missing some info")




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
    adultCheck = tk.Checkbutton(create,text = "Are you older than 18? Check the box if yes", variable = adultcheck)
    adultCheck.pack()
    adultCheck.place(height = 30, width = 250, x = 650, y = 410)

    createLogInBtn = tk.Button(create, text = "Create Account and Logon", command = createAccountScreen.createAccount)
    createLogInBtn.pack()
    createLogInBtn.place(height = 30, width = 200, x = 650, y = 450)

    exitBtn = tk.Button(create, text = "Exit to Sign In screen", command = sI.goToSignInScreen)
    exitBtn.pack()
    exitBtn.place(height = 30, width = 200, x = 650, y = 480)
