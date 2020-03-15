import tkinter as tk



def initSignInWindow():
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

    passWordInput = tk.Entry(signIn, bd = 5)
    passWordInput.pack()
    passWordInput.place(height = 40, width = 200 ,x = 650, y = 380)

    logInBtn = tk.Button(signIn, text = "Sign In")
    logInBtn.pack()
    logInBtn.place(height = 30, width = 200, x = 650, y = 430)

    createAccountBtn = tk.Button(signIn, text = "Create an Account")
    createAccountBtn.pack()
    createAccountBtn.place(height = 30, width = 200, x = 650, y = 470)

    signIn.mainloop()

def initCreateAccountWindow():
    create = tk.Tk("Create your account")
    create.geometry("1000x700")
    create.state('zoomed')    

    userNameLabel = tk.Label(create, text = "Username")
    userNameLabel.pack()
    userNameLabel.place(height = 40, width = 80, x = 580, y = 330)

    userNameInput = tk.Entry(create, bd = 5)
    userNameInput.pack()
    userNameInput.place(height = 40, width = 200 ,x = 650, y = 330)


    passWordLabel = tk.Label(create, text = "Password")
    passWordLabel.pack()
    passWordLabel.place(height = 40, width = 80, x = 580, y = 380)

    passWordInput = tk.Entry(create, bd = 5)
    passWordInput.pack()
    passWordInput.place(height = 40, width = 200 ,x = 650, y = 380)

    logInBtn = tk.Button(create, text = "Create Account and Logon")
    logInBtn.pack()
    logInBtn.place(height = 30, width = 200, x = 650, y = 430)

    exitBtn = tk.Button(create, text = "Exit to Sign In screen")
    exitBtn.pack()
    exitBtn.place(height = 30, width = 200, x = 650, y = 460)


    create.mainloop()


initCreateAccountWindow()
