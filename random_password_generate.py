import tkinter as tk
from tkinter.ttk import *
from tkinter import *
import tkinter.font as tkFont
import string
import random
import pyperclip

class windowclass():

    def __init__(self,master):
        self.master =master

        helv36 = tkFont.Font(family="Helvetica",size=18,weight="bold")

        self.btn = tk.Button(
            master,
            text = "Start",
            command = self.command,
            bg="#000000",
            fg="#b7f731",
            relief="flat",
            width=30,
            font=helv36
        )

        self.btn.pack(padx=50,pady=200)

    def command(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("800x600")
        Demo2(toplevel)


class Demo2:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(
            self.master,
            highlightbackground="green",
            highlightcolor="green",
            highlightthickness=2,
            width=700,
            height=500,
            bd=0

        )

        self.randomButton = tk.Button(
            self.frame, text = "Click Here to generate random password", command = self.randomGen
        )

        self.randomButton.grid(row=0,column=1,padx=220,pady=50)


        helv36 = tkFont.Font(family="Helvetica", size=18, weight="bold")
        self.label = tk.Label(self.frame, text="This is random", font=helv36)
        self.label.grid(row=1, column=1)
        
        self.copyButton = tk.Button(
            self.frame, text = "Copy to Clipboard", command = self.copyPassword
        )
        self.copyButton.grid(row=3, column=1, pady=20)

        self.copylabel = tk.Label(self.frame)
        self.copylabel.grid(row=4,column=1)

        self.frame.grid(padx=50,pady=50)
        self.frame.grid_propagate(0)

    def randomGen(self):

        characters = string.ascii_letters+string.digits+string.punctuation
        print(characters)
        password = ''.join(random.choice(characters) for _ in range(10))

        self.label.configure(text=str(password))
        self.copylabel.configure(text="")
        
        


    def copyPassword(self):
        pyperclip.copy(self.label['text'])
        self.copylabel.configure(text="Password Copied to Clipboard Successfully")        







root = tk.Tk()
root.title("Random Password Generator")
root.geometry("800x600")


cls = windowclass(root)
root.mainloop()

