import tkinter as tk
from tkinter import IntVar


LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_attributes(self, '-fullscreen', True)
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

        
# class StartPage(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#         label = tk.Label(self, text="Start Page", font=LARGE_FONT)
#         label.pack(pady=10,padx=10)

#         button = tk.Button(self, text="Visit Page 1",
#                             command=lambda: controller.show_frame(PageOne))
#         button.pack()

#         button2 = tk.Button(self, text="Visit Page 2",
#                             command=lambda: controller.show_frame(PageTwo))
#         button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        # label.pack(pady=10,padx=10)

        # button1 = tk.Button(self, text="Back to Home",
        #                     command=lambda: controller.show_frame(StartPage))
        # button1.pack()

        # button2 = tk.Button(self, text="Page Two",
        #                     command=lambda: controller.show_frame(PageTwo))
        # button2.pack()
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
        # label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        # label.pack(pady=10,padx=10)

        # button1 = tk.Button(self, text="Back to Home",
        #                     command=lambda: controller.show_frame(StartPage))
        # button1.pack()

        # button2 = tk.Button(self, text="Page One",
        #                     command=lambda: controller.show_frame(PageOne))
        # button2.pack()
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



app = SeaofBTCapp()
app.mainloop()