from tkinter import Tk, PhotoImage
from tkinter.ttk import Label, Frame, Entry, Button

window=Tk()

window.geometry("665x373") # Лимит размер окно

img= PhotoImage(file="D:/nam nhat/term1/Programming/lab3/background.png")
background= Label(window, image=img) 
background.place(x=0,y=0)

intro= Label(window, text="input your first block of the key",font=("Arial",15))
intro.pack(pady=10)

my_frame=Frame(window)
my_frame.pack(pady=15)

input=Entry(my_frame, width=20)
input.grid(column=0,row=0)

output=Label(my_frame, text="your key will be showed here!")
output.grid(column=0, row=3)

def move_right(n, key):  # n это число шагов перемещения, key это блок, который мы передаём
    
    original_key=[i for i in key]
    new_key=''
    for i in range (n):
        change=original_key.pop(-1)
        original_key.insert(0,change)    
    for i in range (len(original_key)):
        new_key+=original_key[i]
    return new_key


def move_left(n,key):   # n это число шагов перемещения, key это блок, который мы передаём
    
    original_key=[i for i in key]
    new_key=''
    for i in range (n):
        change=original_key.pop(0)
        original_key.append(change)
    for i in range(len(original_key)):
        new_key+=original_key[i]
    return new_key


def click():
    
    block_1=input.get()
    if len(block_1)>5 or len(block_1)<5:
        output["text"]="your block is not valid"
    else:
        block_2=move_right(3, block_1)
        block_3=move_left(5, block_1)
        output["text"]=f"your key is: {block_1}-{block_2}-{block_3}"


button=Button( my_frame, 
              text="click",
              command=click )

button.grid(column=0, row=5)
window.mainloop()
