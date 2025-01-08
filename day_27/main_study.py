from tkinter import *

def button_clicked():
    print('I got clicked')
    new_text=input.get()
    my_label.config(text=new_text)

window=Tk()
window.title("MY first gui program")
window.minsize(width=500, height=500)
window.config(padx=100,pady=100)

#Label

my_label=Label(text="I'm a label",font=("Arial",24,"bold"))
my_label.config(text="Next text")
my_label.grid(column=0,row=0)
my_label.config(padx=20,pady=20)
# my_label.place(x=0,y=0)
# my_label.pack()


#buttons



button1= Button(text="Click me", command=button_clicked)
button2= Button(text="Click me,again", command=button_clicked)
# button.pack()
button1.grid(column=1,row=1)
button2.grid(column=2,row=0)

#entry components

input= Entry(width=10)
input.grid(column=3,row=3)
print(input.get())
# input.pack()






window.mainloop()