import pyautogui
from tkinter import *


root=Tk()
root.title("screenshot")
root.geometry("100x100")

e=Entry(root)
l=Label(root,text="save as")



def ss():
    img1=pyautogui.screenshot()
    img1.save(f"{e.get()}.png")




btn=Button(root,text="Screenshot",background="black",foreground="red",command=ss)

btn.pack()
l.pack()
e.pack()


root.mainloop()