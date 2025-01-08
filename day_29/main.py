from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list=password_letters+password_symbols+password_numbers

    shuffle(password_list)
    password= "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_user_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok= messagebox.askokcancel(title=website,message=f'These are the details entered: \nEmail: {email} \nPassword: {password}\n Is it ok to save?')
        if is_ok:
            with open("day_29/passwords.txt",'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

#Window
window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


#Logo
canvas=Canvas(width=200,height=200,highlightthickness=0)
logo_img=PhotoImage(file="day_29/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)


#labels

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)


#Imput
website_entry=Entry(width=51)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_user_entry=Entry(width=51)
email_user_entry.grid(column=1,row=2,columnspan=2)
email_user_entry.insert(0,"georgelucascr@hotmail.com")
#email_user_entry.focus()

password_entry=Entry(width=32)
password_entry.grid(column=1,row=3)
#password_entry.focus()



#Button

generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button=Button(text="Add",width=43,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()