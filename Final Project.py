from tkinter import *

def main_screen():
    screen= Tk()
    screen.geometry("300x250")
    screen.title("Login and Register")
    Label(text= "", bg = "grey", font = ("Times New Roman", 13)).pack()
    Label(text= "").pack()
    Button(text = "Login").pack()
    Button(text= "Register").pack()

    screen.mainloop()

main_screen()