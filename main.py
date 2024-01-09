from tkinter import *
import random
import string



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_pressed():
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for i in range(16))
    password_entry.insert(0,random_password)
    print("Random password is:", random_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_pressed():
    if website_entry.get() == "" or creds_entry.get() == "" or password_entry.get() == "":
        print("dont leave blank")
        win = Tk()
        win.geometry("400x150")
        Label(win,text="Don't leave any fields blank!", font=("Times New Roman", 20, "bold")).pack()
        win.attributes("-topmost",True)
        win.mainloop()


    else:
        saved_password = website_entry.get() + "  |  " + creds_entry.get() + "  |  " + password_entry.get()
        with open("not_passwords.txt", 'a') as f:
            f.write(saved_password)
            f.write("\n")
            f.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=80)

canvas = Canvas(width=200, height=190)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,84, image=lock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:",font=("Times New Roman", 12, "bold"))
website_label.grid(column=0, row=1)

creds_label = Label(text="Email/Username: ",font=("Times New Roman", 12, "bold"))
creds_label.grid(column=0 ,row=2)

password_label = Label(text="Password:",font=("Times New Roman", 12, "bold"))
password_label.grid(column=0, row=3)

website_entry = Entry(width=54)
website_entry.grid(column=1, row=1,columnspan=2)

creds_entry = Entry(width=54)
creds_entry.grid(column=1, row=2,columnspan=2)


password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password_pressed)
generate_button.grid(column=2, row=3)


add_button = Button(text="Add", command=add_button_pressed)
add_button.config(width=45)
add_button.grid(column=1, row=4,columnspan=2)



window.mainloop()