from tkinter import*
from tkinter import ttk
import requests


def data_get():
  city = city_name.get()
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0ffef7045720177f84f529dfbfada947").json()
  w_label_1.config(text=data["weather"][0]["main"])
  wb_label_1.config(text=data["weather"][0]["description"])
  temp_label_1.config(text=str(int(data["main"]["temp"]-273.15)))
  pre_label_1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather App")
win.config(bg="lightblue")
win.geometry("500x570")
name_label = Label(win,text="Weather App",font=("Time New Roman",40,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city_name = StringVar()
com = ttk.Combobox(win,text="Weather App",font=("Time New Roman",20,"bold"),values=list_name,textvariable=city_name)
com.place(x=40,y=120,height=50,width=420)

w_label = Label(win,text="Weather Climate",font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)

w_label_1 = Label(win,text="",font=("Time New Roman",20))
w_label_1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win,text="Weather Description",font=("Time New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label_1 = Label(win,text="",font=("Time New Roman",17))
wb_label_1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Temperature",font=("Time New Roman",17))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label_1 = Label(win,text="",font=("Time New Roman",17))
temp_label_1.place(x=250,y=400,height=50,width=210)

pre_label = Label(win,text="Pressure",font=("Time New Roman",17))
pre_label.place(x=25,y=470,height=50,width=210)

pre_label_1 = Label(win,text="",font=("Time New Roman",17))
pre_label_1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Submit",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(x=160,y=190,height=50,width=180)

win.mainloop()