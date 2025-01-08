from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
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
    new_data={
        website:{
            "Email":email,    
            "Password":password,    
        }
    }
    if len(website)==0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("day_30/passwords.json",'r') as data_file:

                #Reading old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("day_30/passwords.json",'w') as data_file:   
                json.dump(new_data,data_file,indent=4)
        else:
            #Updatind old data with new data
            data.update(new_data)
            with open("day_30/passwords.json",'w') as data_file:
                #Saving update data
                json.dump(data,data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    
# ---------------------------- SEARCH --------------------------------- #
def find_password():
    website=website_entry.get()
    try:
        with open("day_30/passwords.json","r") as data_file:
            data=json.load(data_file)
    except FileExistsError:
        messagebox.showinfo(title="Erro", message="No data file found.")
    else:    
        if website in data:
            email= data[website]["Email"]
            password= data[website]["Password"]
            messagebox.askokcancel(title=website,message=f'Email: {email} \nPassword: {password}')
        else:
            messagebox.showinfo(title="Erro",message=f"No details for {website} exists.")

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
website_entry=Entry(width=32)
website_entry.grid(column=1,row=1)
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

search_button=Button(text="Generate Password",command=find_password)
search_button.grid(column=2,row=1)
window.mainloop()