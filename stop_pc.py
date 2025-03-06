from tkinter import *
from tkinter import messagebox
import random
import os

class MyWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("Testeur de Chance")
        self.geometry("300x100")

        self.label = Label(self, text="Teste ta chance")
        self.label.pack()

        self.button = Button(self, text="Appui !!", relief=GROOVE, command=self.do_something)
        self.button.pack()

    def do_something(self):
        stop = random.randint(1, 2)
        if stop == 2:
            result = messagebox.askyesno("Attention", "Voulez-vous vraiment arrêter l'ordinateur ?")
            if result:
                os.system('shutdown /s /t 10')
                self.label.config(text="Pas cool")
            else:
                os.system('shutdown /s /t 10')
                self.label.config(text="Sauvé de justesse !... ou pas")
        else:
            self.label.config(text="Cool")

window = MyWindow()
window.mainloop()
