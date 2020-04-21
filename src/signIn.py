import tkinter as tk
from tkinter import IntVar
import pymysql as sql
import base64 as b64
import bcrypt as bc
import tkinter.messagebox as mb
import datetime as dt





database = "imagedb"
creds = open("secret\SqlServerUsrPass.txt", "r").readlines()
server_username = b64.b64decode(creds[0]).decode("utf-8")
server_password = b64.b64decode(creds[1]).decode("utf-8")

imagedb = sql.connect("imagecollageapcsp.mysql.database.azure.com", server_username[:-1] + "@imagecollageapcsp", server_password, database)

cursor = imagedb.cursor()


class ImageDB(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.state("zoomed")
        container = tk.Frame(self)
        

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for pages in (PageOne, PageTwo):

            frame = pages(container, self)

            self.frames[pages] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageOne)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        userNameLabel = tk.Label(self, text = "Username")
        userNameLabel.pack()
        userNameLabel.place(height = 40, width = 80, x = 580, y = 330)

        userNameInput = tk.Entry(self, bd = 5)
        userNameInput.pack()
        userNameInput.place(height = 40, width = 200 ,x = 650, y = 330)


        passWordLabel = tk.Label(self, text = "Password")
        passWordLabel.pack()
        passWordLabel.place(height = 40, width = 80, x = 580, y = 380)

        passWordInput = tk.Entry(self, bd = 5, show = "*")
        passWordInput.pack()
        passWordInput.place(height = 40, width = 200 ,x = 650, y = 380)

        logInBtn = tk.Button(self, text = "Sign In")
        logInBtn.pack()
        logInBtn.place(height = 30, width = 200, x = 650, y = 430)

        createAccountBtn = tk.Button(self, text = "Create an Account", command = lambda: controller.show_frame(PageTwo))
        createAccountBtn.pack()
        createAccountBtn.place(height = 30, width = 200, x = 650, y = 470)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        createUserNameLabel = tk.Label(self, text = "Username")
        createUserNameLabel.pack()
        createUserNameLabel.place(height = 40, width = 80, x = 580, y = 330)

        createUserNameInput = tk.Entry(self, bd = 5)
        createUserNameInput.pack()
        createUserNameInput.place(height = 40, width = 200 ,x = 650, y = 330)

        createPassWordLabel = tk.Label(self, text = "Password")
        createPassWordLabel.pack()
        createPassWordLabel.place(height = 40, width = 80, x = 580, y = 380)

        createPassWordInput = tk.Entry(self, bd = 5, show = "*")
        createPassWordInput.pack()
        createPassWordInput.place(height = 40, width = 200 ,x = 650, y = 380)

        adultcheck = IntVar()
        adultCheck = tk.Checkbutton(self,text = "Are you older than 18? Check the box if yes", variable = adultcheck)
        adultCheck.pack()
        adultCheck.place(height = 30, width = 250, x = 650, y = 410)

        createLogInBtn = tk.Button(self, text = "Create Account and Logon")
        createLogInBtn.pack()
        createLogInBtn.place(height = 30, width = 200, x = 650, y = 450)

        exitBtn = tk.Button(self, text = "Exit to Sign In screen", command = lambda: controller.show_frame(PageOne))
        exitBtn.pack()
        exitBtn.place(height = 30, width = 200, x = 650, y = 480)



app = ImageDB()
app.mainloop()



















# import pymysql as sql
# import bcrypt as bc
# import tkinter as tk
# import datetime as dt
# import base64 as b64 
# from tkinter import IntVar
# import tkinter.messagebox as mb
# import createAccount as cA





# #Establish a connection from the app to the database
# def establish_connection():

#     database = "imagedb"
#     creds = open("secret\SqlServerUsrPass.txt", "r").readlines()
#     server_username = b64.b64decode(creds[0]).decode("utf-8")
#     server_password = b64.b64decode(creds[1]).decode("utf-8")

#     imagedb = sql.connect("imagecollageapcsp.mysql.database.azure.com", server_username[:-1] + "@imagecollageapcsp", server_password, database)

#     cursor = imagedb.cursor()


# # def goToSignInScreen():
# #     create.widthraw()
# #     signIn.iconify()
# #     signIn.deiconify()



# def initSignInWindow():
#     signIn.mainloop()
    




# # Sign In window declerations
# signIn = tk.Tk("SignIn")
# signIn.geometry("1000x700")
# signIn.state('zoomed')

# userNameLabel = tk.Label(signIn, text = "Username")
# userNameLabel.pack()
# userNameLabel.place(height = 40, width = 80, x = 580, y = 330)

# userNameInput = tk.Entry(signIn, bd = 5)
# userNameInput.pack()
# userNameInput.place(height = 40, width = 200 ,x = 650, y = 330)


# passWordLabel = tk.Label(signIn, text = "Password")
# passWordLabel.pack()
# passWordLabel.place(height = 40, width = 80, x = 580, y = 380)

# passWordInput = tk.Entry(signIn, bd = 5, show = "*")
# passWordInput.pack()
# passWordInput.place(height = 40, width = 200 ,x = 650, y = 380)

# logInBtn = tk.Button(signIn, text = "Sign In")
# logInBtn.pack()
# logInBtn.place(height = 30, width = 200, x = 650, y = 430)

# createAccountBtn = tk.Button(signIn, text = "Create an Account", command = cA.createAccountScreen.goToCreateAccountScreen)
# createAccountBtn.pack()
# createAccountBtn.place(height = 30, width = 200, x = 650, y = 470)





# # open the sign in form
# initSignInWindow()