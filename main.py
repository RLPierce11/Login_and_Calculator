import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Calculator import infixToPostfix
from Calculator import evaluate




 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting of the different page layouts
        for F in (StartPage, Page1):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    #login validation function
    def login_clicked(self, username, password):
        if(username == "admin1234" and password == "Admin1234!"):
            #change page
            self.show_frame(Page1)
        else:
            msg = 'Username or Password is Incorrect!'
            showinfo(
                title='Login Error',
                message = msg
            )
        return

    #set answer entry text
    def setAnswer(self, answer, equation):
        answer.delete(0, "end")

        result = evaluate(infixToPostfix(equation))

        answer.insert(0, result)

  
# first window frame startpage  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Login", font = LARGEFONT)
         
        # putting the grid in its place by using grid
        label.grid(row = 0, column = 20, padx = 10, pady = 10)

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        usernameLabel = ttk.Label(self, text="Username:")
        usernameLabel.grid(row = 1, column = 20, padx = 10, pady = 5)

        usernameEntry = ttk.Entry(self, width = 50)
        usernameEntry.grid(row = 3, column = 20, padx = 10, pady = 5)

        passwordLabel = ttk.Label(self, text="Password:")
        passwordLabel.grid(row = 5, column = 20, padx = 10, pady = 5)

        passwordEntry = ttk.Entry(self, width = 50, show="*")
        passwordEntry.grid(row = 7, column = 20, padx = 10, pady = 5)


  
        button1 = ttk.Button(self, text ="submit",
        command = lambda : controller.login_clicked(usernameEntry.get(), passwordEntry.get()))
     
        # putting the button in its place by using grid
        button1.grid(row = 9, column = 20, padx = 10, pady = 10)
          
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label1 = ttk.Label(self, text ="Calculator", font = LARGEFONT)
        label1.grid(row = 2, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text layout2
        button1 = ttk.Button(self, text ="Logout",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by using grid
        button1.grid(row = 0, column = 10, padx = 10, pady = 10)

        Elabel = ttk.Label(self, text="Equation:")
        Elabel.grid(row = 4, column = 4, padx = 10)

        EEntry = ttk.Entry(self, width = 50)
        EEntry.grid(row = 5, column = 4, padx = 10)

        Esubmit = ttk.Button(self, text = "Calculate", command= lambda : controller.setAnswer(REntry, EEntry.get()))
        Esubmit.grid(row = 6, column = 4, padx = 10, pady = (0, 10))

        Rlabel = ttk.Label(self, text = "Answer:")
        Rlabel.grid(row = 7, column = 4, padx = 10)

        REntry = ttk.Entry(self, width = 50)
        REntry.grid(row = 8, column = 4, padx = 10, pady = (0, 20))


  
  
  
  
  
# Driver Code
app = tkinterApp()
app.mainloop()