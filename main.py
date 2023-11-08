from tkinter import*
from tkinter.ttk import *
from move import *
window=Tk()
window.geometry("665x373")
img= PhotoImage(file="D:/nam nhat/term1/Programming/lab3/background.png")
background= Label(window, image=img)
background.place(x=0,y=0)
intro= Label(window, text="input your first block of the key",font=("Arial",15))
intro.pack(pady=10)
my_frame=Frame(window)
my_frame.pack(pady=15)
info=Entry(my_frame, width=30)
info.grid(column=0,row=0)
output=Label(my_frame, text="your key will be showed here!")
output.grid(column=0,row=3)

def click():
    input=info.get()
    if len(input)>5 or len(input)<5:
        output["text"]="your block is not valid"
    else:
        block_2=move_right(3,input)
        block_3=move_left(5,input)
        output["text"]=f"your key is: {input}-{block_2}-{block_3} "
button=Button( my_frame, 
              text="click",
              command= click )
button.grid(column=0, row=5)
window.mainloop()