from tkinter import*
from tkinter import ttk

import random
def password_generator():
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
           'o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'Q','R','S','T','U','V','W','X','Y','Z']
  numbers = ['0','1','2','3','4','5','6','7','8','9']
  symbols = ['!','#','$','%','&','(',')','*','+']
  password_list = []
  for i in range(int(letter.get())):
    char = random.choice(letters)
    password_list += char
  for i in range(int(number.get())):
    char = random.choice(numbers)
    password_list += char
  for i in range(int(symbol.get())):
    char = random.choice(symbols)
    password_list += char
  random.shuffle(password_list)
  password = ""
  for i in password_list:
    password += i
  result = Label(win,text=f"Your Password is {password}",font=("Time New Roman",20))
  result.place(x=50,y=400,height=50,width=400)


win = Tk()
win.title("Password Generator")
win.config(bg="lightpink")
win.geometry("500x570")
name_label = Label(win,text="Password Generator",font=("Time New Roman",34,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

l_label = Label(win,text="Enter number of letters",font=("Time New Roman",20))
l_label.place(x=25,y=120,height=50,width=300)

letter = Entry(win,font=("Time New Roman",20))
letter.place(x=350,y=120,height=50,width=125)

n_label = Label(win,text="Enter number of digits",font=("Time New Roman",20))
n_label.place(x=25,y=190,height=50,width=300)

number = Entry(win,font=("Time New Roman",20))
number.place(x=350,y=190,height=50,width=125)

n_label = Label(win,text="Enter number of symbols",font=("Time New Roman",20))
n_label.place(x=25,y=260,height=50,width=300)

symbol = Entry(win,font=("Time New Roman",19))
symbol.place(x=350,y=260,height=50,width=125)

done_button = Button(win,text="Submit",font=("Time New Roman",20,"bold"),command=password_generator)
done_button.place(x=160,y=330,height=50,width=180)
win.mainloop()