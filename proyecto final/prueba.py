from tkinter import *

def tra(*args):
    if txt.get() == "a":
        return entrada.set("0")
        
    elif txt.get()=="b":
        return entrada.set("1")
        

def change_image(*args):
    # Change image of label accordingly
    if entrada.get() == "0":
        label.config(image=photos[int(entrada.get())])
        
    elif entrada.get()=="1":
        label.config(image=photos[int(entrada.get())])
        
    
        
        
    

app = Tk()
app.title("Example")
app.geometry('500x200+200+200')
app.configure(background='black')
app.resizable(0,0)

studFiles = StringVar()
studFiles.set('Image')
txt=Entry(app)
txt.place(x=0,y=0)
entrada=StringVar()

btn=Button(app, text="traducir", command=tra).place(x=250,y=0)



entrada.trace("w", change_image)

# List of photoimages for each image
photos =[PhotoImage(file='letra a.png'), PhotoImage(file='letra b.png')]
label = Label(app,image=photos[0])
label.place(x=175,y=50)

app.mainloop()
