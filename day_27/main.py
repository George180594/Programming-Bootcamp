from tkinter import *

def converting():
    miles=input_miles.get()
    km=float(miles)*1.609
    kilometer_result_label.config(text=f'{km}')



#window

window= Tk()
window.title('Mile to Km converter')
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

my_label1=Label(text="is equal to",font=("Arial",12,"normal"))
my_label1.grid(column=0,row=1)
my_label1.config(padx=10,pady=10)

my_label_2=Label(text="Miles",font=("Arial",12,"normal"))
my_label_2.grid(column=2,row=0)
my_label_2.config(padx=0,pady=10)

my_label_3=Label(text="Km",font=("Arial",12,"normal"))
my_label_3.grid(column=2,row=1)
my_label_3.config(padx=0,pady=10)

kilometer_result_label= Label(text='0')
kilometer_result_label.grid(column=1,row=1)

#Input

input_miles=Entry()
input_miles.grid(column=1,row=0)

convert=Button(text="Convert",command=converting)
convert.grid(column=1,row=2)


window.mainloop()