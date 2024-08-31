from tkinter import*
from tkinter import ttk

def calculate_bmi():
  bmi =float(weight.get()) / float(height.get())**2
  int_bmi = round(bmi,4)
  print("BMI is:",bmi)
  result = Label(win,text=f"Your BMI is {int_bmi}",font=("Time New Roman",20))
  result.place(x=50,y=330,height=50,width=400)
  if(bmi>0):
    if(bmi<18.5):
      des = Label(win,font=("Time New Roman",20),text="You are Underweight")
      des.place(x=50,y=400,height=50,width=400)
    elif(18.5<=bmi<=24.9):
      des = Label(win,font=("Time New Roman",20),text="You are Normalweight")
      des.place(x=50,y=400,height=50,width=400)
    elif(25<=bmi<=29.9):
      des = Label(win,font=("Time New Roman",20),text="You are Overweight")
      des.place(x=50,y=400,height=50,width=400)
    elif(30<=bmi<=34.9):
      des = Label(win,font=("Time New Roman",20),text="You are Obese")
      des.place(x=50,y=400,height=50,width=400)
    elif(35<=bmi<=39.9):
      des = Label(win,font=("Time New Roman",20),text="You are Severely obese")
      des.place(x=50,y=400,height=50,width=400)
    else:
      des = Label(win,font=("Time New Roman",20),text="You are Morbidly obese")
      des.place(x=50,y=400,height=50,width=400)
  else:
    des = Label(win,font=("Time New Roman",20),text="Enter valid inputs")
    des.place(x=50,y=400,height=50,width=400)
   
win = Tk()
win.title("BMI Calculator")
win.config(bg="lightgreen")
win.geometry("500x570")
name_label = Label(win,text="BMI Calculator",font=("Time New Roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

w_label = Label(win,text="Enter your weight in kg",font=("Time New Roman",20))
w_label.place(x=25,y=120,height=50,width=300)

weight = Entry(win,font=("Time New Roman",20))
weight.place(x=350,y=120,height=50,width=125)

h_label = Label(win,text="Enter your height in m",font=("Time New Roman",20))
h_label.place(x=25,y=190,height=50,width=300)

height = Entry(win,font=("Time New Roman",20))
height.place(x=350,y=190,height=50,width=125)

done_button = Button(win,text="Submit",font=("Time New Roman",20,"bold"),command=calculate_bmi)
done_button.place(x=160,y=260,height=50,width=180)

win.mainloop()
