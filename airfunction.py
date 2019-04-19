from tkinter import *
from tkinter.font import Font


def default(t1, t2):
    text2 = t2
    label_font = Font(family="Bold", size=13)
    head_font = Font(family="Times New Roman", size=30)
    win_font = Font(family="Arial", size=20)
    text = Label(t1, text=" AirLine One ", width="300", height="1", font=head_font, bg="light blue1")
    text.pack()
    Label(t1, text="Air_Tickets At your fingertips", width="300", height="1", font=label_font,
          bg="light blue1").pack()
    t1.title("AIRLINE SEAT RESERVATION")
    t1.geometry("600x550+450+70")
    label = Label(t1, text=text2, font=win_font, bg="orange3")
    label.pack(fill=X)
