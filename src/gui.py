from tkinter import *



def initWindow():
    signIn = Tk("ImageDB")
    signIn.geometry("1000x700")
    signIn.state('zoomed')

    userNameLabel = Label(signIn, text = "Username")
    userNameLabel.pack()
    userNameLabel.place(height = 40, width = 80, x = 580, y = 330)

    userNameInput = Entry(signIn, bd = 5)
    userNameInput.pack()
    userNameInput.place(height = 40, width = 200 ,x = 650, y = 330)


    passWordLabel = Label(signIn, text = "Password")
    passWordLabel.pack()
    passWordLabel.place(height = 40, width = 80, x = 580, y = 380)

    passWordInput = Entry(signIn, bd = 5)
    passWordInput.pack()
    passWordInput.place(height = 40, width = 200 ,x = 650, y = 380)

    logInBtn = Button(signIn, text = "Sign In")
    logInBtn.pack()
    logInBtn.place(height = 30, width = 200, x = 650, y = 430)

    createAccountBtn = Button(signIn, text = "Create an Account")
    createAccountBtn.pack()
    createAccountBtn.place(height = 30, width = 200, x = 650, y = 470)

    signIn.mainloop()


initWindow()