from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("GUI")
root.geometry("900x600")
list1 = ["Label","Button","Dropdown"]
d1 = ttk.Combobox(root, state = "readonly", values = list1)
d1.pack()

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
    
    def createButton(self):
        b1 = Button(root, text = "Click Here!", command = self.message)
        b1.pack()
    def createDropdown(self):
        list2 = ["Apples","Banana","Oranges","Mango"]
        d2 = ttk.Combobox(root, state = "readonly", values = list2)
        d2.pack()
    def createLabel(self):
        l1= Label(root, text = "very cool new label")
        l1.pack()
    def message(self):
        messagebox.showinfo("showinfo","you clicked the button")
    def choose(self):
        global d1
        element = d1.get()
        if(element == "Label"):
            self.createLabel()
        elif(element == "Button"):
            self.createButton()
        elif(element == "Dropdown"):
            self.createDropdown()
            
obj_of_CreateElements = CreateElements()

btn = Button(root, text = "Select Options", command = obj_of_CreateElements.choose)
btn.pack(padx = 20, pady = 10)

root.mainloop()