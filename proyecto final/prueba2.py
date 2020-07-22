from tkinter import *

def change_image(*args):
    # Change image of label accordingly
    label.config(image=photos[int(studFiles.get())])

app = Tk()
app.title("Example")
app.geometry('500x200+200+200')
app.configure(background='black')
app.resizable(0,0)

studFiles = StringVar()
studFiles.set('imagenes')
files =['0', '1'] # Number is corresponding list index
studDropDown = OptionMenu(app, studFiles, *files)
studDropDown.config(font=("Times", 16, "italic"))
studDropDown["menu"].config(font=("Times", 16, "italic"))
studDropDown.pack()

studFiles.trace("w", change_image)

# List of photoimages for each image
photos =(PhotoImage(file='letra a.png'), PhotoImage(file='letra b.png'))
label = Label(app,image=photos[0])
label.pack()

app.mainloop()
