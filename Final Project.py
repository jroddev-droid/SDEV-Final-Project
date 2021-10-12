from tkinter import *
import os

def delete2():                                                                          #Deletes the window that pops up
    screen3.destroy()

def delete3():                                                                          #Deletes the window that pops up
    screen4.destroy()

def delete4():                                                                          #Deletes the window that pops up
    screen5.destroy()

def login_success():                                                                    #Function that is a pop up window for when the login is a success
    global screen3                                                                      #globalized screen 3
    screen3 = Toplevel(screen)
    screen3.title("Login Successful")
    screen3.geometry("150x100")
    Label(screen3, text = "Login Success").pack()                                       #shows login success in screen 3
    Button(screen3, text = "OK", command = delete2).pack()                              #shows button on screen 3

def password_not_recognized():                                                          #Function that is a pop up window for when the password is not recognized
    global screen4                                                                      #globalized screen 4
    screen4 = Toplevel(screen)
    screen4.title("Password not Recognized")
    screen4.geometry("150x100")
    Label(screen4, text = "Password not recognized").pack()                                       
    Button(screen4, text = "OK", command = delete3).pack()                            

def user_not_found():                                                                   #Function that is a pop up window for when the user is not found
    global screen5                                                                      #globalized screen 3
    screen5 = Toplevel(screen)
    screen5.title("User not Found")
    screen5.geometry("150x100")
    Label(screen5, text = "User Not Found").pack()                                       #shows login success in screen 3
    Button(screen5, text = "OK", command = delete4).pack()

def register_user():                                                                    #Function that gives register button functionality
    print("is working")

    username_info = username.get()
    password_info = password.get()
                                               
    file = open(username_info, "w")
    file.write(username_info+"/n")                                                      # /n Leaves a line between username and password so it is not stored on same line and is easier to read, opens to write mode
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)                                                       #This will clear the fields when the user has entered information
    password_entry.delete(0, END)                                                       #This will clear the fields when the user has entered information

    Label(screen1, text = "Registration has been succesfull.", fg = "green", font = ("Times New Roman", 13)).pack()    #Prompt tells user his registration has been succesful with a in screen 1 in Times New Roman font, size 13 font, and green foreground
 

def login_verify():                                                                     #Function that will ouptut another window depending if the user has been verified
    
    username1 = username_verify.get()                                                   #gathers user name and passwords and validates them to check if users account actually exists or it doesnt
    password1 = password_verify.get()                                                   #gathers user name and passwords and validates them to check if users account actually exists or it doesnt
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()                                                        #Lists all files within the current directory as a list
    if username1 in list_of_files:                                                      # It sees if there is the file, username1, in list of files
        file1 = open(username1, "r")                                                    #opens username 1 in read mode so we are able to read it.
        verify = file1.read().splitlines()                                              #Reads all lines within text file and will split it into a list
        if password1 in verify: 
            login_success()                                                             #is the output if successfull
        else:
            password_not_recognized()
    else:                                                                               #Used if we dont have the username in the directory
        user_not_found()



def register():                                                                         #Function for the register button
    global screen1                                                                      #globalizes screen 1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username                                                                     #globalized username
    global password                                                                     #globalized password
    global username_entry
    global password_entry
    username = StringVar()                                                              #created entries and assigned them to this text variable 
    password = StringVar()                                                              #created entries and assigned them to this text variable 

    Label(screen1, text = "Create Username and Password").pack()
    Label(screen1, text = "").pack()                                                     #Creates an empty space for organization
    Label(screen1, text = "Username * ").pack()                                          #Opens and placed is screen 1, Asterisk denotes that username is required
    
    username_entry = Entry(screen1, textvariable = username)                            #Opens and placed in screen 1, Entry for username is set to username and stored in variable username_entry 
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()                                         #Opens and placed in screen 1. Asterisk denotes that password is required
    password_entry = Entry(screen1, textvariable = password)                          #Opens and placed in screen 1, Entry for password is password and stored in variable password_entry
    password_entry.pack()
    Label(screen1, text = "").pack()                                                                          #Button runs and saves information entered 
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()              #Button assigned to function register_user                     


def login():                                                                               #Function for the login button
    global screen2                                                                         #globalizes screen2
    screen2 = Toplevel(screen)                                                             #set to first screen that was created
    screen2.title("Login")                                                                 #Screen 2 title was set to Login
    screen2.geometry("300x250")
    Label(screen2, text = "Enter details below to login").pack()
    Label(screen2, text= "").pack()                                                         #Created empty label for space

    global username_verify                                                                 #globalized username_verify
    global password_verify                                                                 #globalized password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1                              
    global password_entry1
    
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable= username_verify)                                 #Entry field that will sit on screen 2 and its text variable set to username verify                             
    username_entry1.pack()
    Label(screen2, text = "").pack()                                                                #Created blank label used to create space and for it to look a little neater
    Label(screen2, text = "Password *").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)                                 #Entry field that will sit on screen 2 and its text variable set to password verify                             
    password_entry1.pack()
    Label(screen2, text = "").pack()                                                                #Blank label for space and organization
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()          #Buttton that will be displayed on screen 2 with its text of Login and added dimensions, its command is to go  to login_verify

def main_screen():                                                                                  #This is the main screen function
    global screen                                                                                   #globalizes screen to be able to get accessed form another function
    screen= Tk()                                                                                    #Screen variable assigned to TK
    screen.geometry("300x250")                                                                      #This sets the screen size for the main screen
    screen.title("Notes Application")                                                               #This is the title of the main screen for notes app
    Label(text= "Notes", bg = "grey" ,width = "300", height = "2", font = ("Times New Roman", 13)).pack()                       #This is the header,background is set to grey font was set to Times New Roman with a font size of 13, Header size is also increased to
    Label(text= "Login or Regiester").pack() 
    Button(text = "Login", height = "2", width = "30", command= login).pack()                                                   #This is the login button, assigned command of login
    Label(text = "").pack()                                                                                                     #Created empty label to create space
    Button(text= "Register", height = "2", width = "30", command = register).pack()                                             #This is the register button with the same dimensions as the Login button, its assigned the command of register

    screen.mainloop()

main_screen() #calls main screen function 