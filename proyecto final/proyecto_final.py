from tkinter import*
import winsound
import time

def senales():
    
    
    def tra():
        trad=txt.get()
        palabra=trad
        palabra=palabra.lower()
        list(palabra)
        mostrar="a"

        if trad=="a":
            ima1=PhotoImage(file="letra a.png")

       
        
##        for i in palabra:
##            mostrar.append(i)
        print(mostrar)
        return entrada.set(ima1)
        
##        xe=0
##        ye=420
##        for j in mostrar:
##            
##            if j=='a':
##                ima1=PhotoImage(file="letra a.png")
##                lblRes2=Label(venS,image=ima1).place(x=xe, y=ye)
##            elif j=='b':
##               
##                ima2=PhotoImage(file="letra b.png")
##                lblRes3=Label(venS,image=ima2).place(x=xe, y=ye)
##                
##            elif i=='c':
##                pass
##            elif i=='d':
##                ima=PhotoImage(file="letra d.png")
##             
##            elif i=='e':
##                mostar[i]=PhotoImage(file="letra e.png")
##                
##            elif i=='f':
##                mostar[i]=PhotoImage(file="letra f.png")
##            elif i=='g':
##                mostar[i]=PhotoImage(file="letra g.png")
##            elif i=='h':
##                mostar[i]=PhotoImage(file="letra h.png")
##            elif i=='i':
##                mostar[i]=PhotoImage(file="letra i.png")
##              
##            elif i=='j':
##                mostar[i]=PhotoImage(file="letra j.png")
##            elif i=='k':
##                mostar[i]=PhotoImage(file="letra k.png")
##             
##            elif i=='l':
##                mostar[i]=PhotoImage(file="letra l.png")
##                
##            elif i=='m':
##                mostar[i]=PhotoImage(file="letra m.png")
##                
##            elif i=='n':
##                mostar[i]=PhotoImage(file="letra n.png")
##                
##            elif i=='ñ':
##                mostar[i]=PhotoImage(file="letra ñ.png")
##               
##            elif i=='o':
##                mostar[i]=PhotoImage(file="letra o.png")
##                
##            elif i=='p':
##                mostar[i]=PhotoImage(file="letra p.png")
##                
##            elif i=='q':
##                mostar[i]=PhotoImage(file="letra q.png")
##              
##            elif i=='r':
##                mostar[i]=PhotoImage(file="letra r.png")
##                
##            elif i=='s':
##                mostar[i]=PhotoImage(file="letra s.png")
##                
##            elif i=='t':
##                mostar[i]=PhotoImage(file="letra t.png")      
##               
##            elif i=='u':
##                mostar[i]=PhotoImage(file="letra u.png")
##                
##            elif i=='v':
##                mostar[i]=PhotoImage(file="letra v.png")
##                
##            elif i=='w':
##                mostar[i]=PhotoImage(file="letra w.png")
##                
##                
##            elif i=='x':
##                mostar[i]=PhotoImage(file="letra x.png")
##               
##                
##            elif i=='y':
##                mostar[i]=PhotoImage(file="letra y.png")
##            
##                
##            elif i=='z':
##                mostar[i]=PhotoImage(file="letra z.png")
##        
##            elif i==' ':
##                mostar[i]=PhotoImage(file="letra a.png")
##                lblRes6=Label(venS,image=ima).place(x=300, y=420)
##            xe=xe+100
##
##
##            
##            
##        return entrada.set(mostrar)
        
        
    
        
            
        
    ven.destroy()
    venS=Tk()
    imagenf=PhotoImage(file="senas.png")
    labelFondo=Label(venS,image=imagenf)
    labelFondo.place(x=0,y=0,relwidth=1.0,relheight=1.0)
    venS.title("Traductor")
    venS.geometry("700x600+350+120")
    venS.resizable(0,0)
    venS.iconbitmap("icono.ico")
    labelTitulo=Label(venS, text="senales",fg="white", bg="#3498DB", font="arial 25 italic bold").place(x=450,y=50)
    imagenc=PhotoImage(file="codigo-senas.png")
    imagenc=imagenc.zoom(40)
    imagenc=imagenc.subsample(80)
    labelFoto=Label(venS,image=imagenc)
    labelFoto.place(x=200,y=120)
    lblpalabra=Label(text="digite lo que quiere traducir: ", font="arial 14 italic bold ").place(x=20,y=370)
    entrada=StringVar()
    txt=Entry(venS)
    txt.place(x=310,y=370)
    btn=Button(venS, text="traducir", command=tra).place(x=450,y=370)
    lblRes2=Label(venS,image=entrada).place(x=0, y=420)
  
    
    venS.mainloop()
def morse():
    def tra():
        trad=txt.get()
        palabra=trad
        palabra=palabra.lower()
        list(palabra)
        mostrar=[]
        for i in palabra:
            if i=='a':
                a=('.-')
                mostrar.append(a)
                winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='b':
                b='-...'
                mostrar.append(b)
                winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='c':
                c='-.-.'
                mostrar.append(c)
                winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='d':
                d='-..'
                mostrar.append(d)
                winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='e':
                e='.'
                mostrar.append(e)
                winsound.Beep(500,500),time.sleep(1.5)
            if i=='f':
                f='..-.'
                mostrar.append(f)
                winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='g':
                g='--.'
                mostrar.append(g)
                winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='h':
                h='....'
                mostrar.append(h)
                winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='i':
                i='..'
                mostrar.append(i)
                winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='j':
                j='.---'
                mostrar.append(j)
                winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='k':
                k='-.-'
                mostrar.append(k)
                winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='l':
                l='.-..'
                mostrar.append(l)
                winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='m':
                m='--'
                mostrar.append(m)
                winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='n':
                n='-.'
                mostrar.append(n)
                winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='ñ':
                ñ='--.--'
                mostrar.append(ñ)
                winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='o':
                o='---'
                mostrar.append(o)
                winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='p':
                p='.--.'
                mostrar.append(p)
                winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='q':
                q='--.-'
                mostrar.append(q)
                winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='r':
                r='.-.'
                mostrar.append(r)
                winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='s':
                s='...'
                mostrar.append(s)
                winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            if i=='t':
                t='-'
                mostrar.append(t)
                winsound.Beep(500,1500),time.sleep(1.5)
            if i=='u':
                u='..-'
                mostrar.append(u)
                winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='v':
                v='...-'
                mostrar.append(v)
                winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='w':
                w='.--'
                mostrar.append(w)
                winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='x':
                x='-..-'
                mostrar.append(x)
                winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='y':
                y='-.--'
                mostrar.append(y)
                winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            if i=='z':
                z='--..'
                mostrar.append(z)
                winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            if i==' ':
                esp=' '
                mostrar.append(esp)
                time.sleep(2.5)
            cadena = " ".join(mostrar)
            
        return entrada.set(cadena)
    
    ven.destroy()
    venM=Tk()
    imagenf=PhotoImage(file="morse.png")
    labelFondo=Label(venM,image=imagenf)
    labelFondo.place(x=0,y=0,relwidth=1.0,relheight=1.0)
    venM.title("Traductor")
    venM.geometry("700x600+350+120")
    venM.resizable(0,0)
    venM.iconbitmap("icono.ico")
    labelTitulo=Label(venM, text="morse",fg="white", bg="#3498DB", font="arial 25 italic bold").place(x=450,y=50)
    imagenc=PhotoImage(file="codigo-Morse.png")
    imagenc=imagenc.zoom(40)
    imagenc=imagenc.subsample(80)
    labelFoto=Label(venM,image=imagenc)
    labelFoto.place(x=200,y=120)
    lblpalabra=Label(text="digite lo que quiere traducir: ", font="arial 14 italic bold ").place(x=20,y=370)
    entrada=StringVar()
    txt=Entry(venM)
    txt.place(x=310,y=370)
    btn=Button(venM, text="traducir", command=tra).place(x=450,y=370)
    lblRes=Label(venM,textvariable=entrada, font="arial 14 italic bold ").place(x=300, y=420)
    
    venM.mainloop()
    

    
def braille():
    def tra():
        trad=txt.get()
        palabra=trad
        palabra=palabra.lower()
        list(palabra)
        for i in palabra:
    
            if i == ' ':
                espacio = ([[" ", " "],[" ", " "],[" ", " "]]) 
                for ñ in range(3):
                    for ii in range(2):
                        print(espacio[ñ][ii], end = " ")
                    print()

            if i == "a":
                a = ([["·", " "],[" ", " "],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(a[ñ][ii], end = " ")
                    print()
      
            if i == "b":
                b = ([["·", " "],["·", " "],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(b[ñ][ii], end = " ")
                    print()

            if i == "c" : 
                c = ([["·", "·"],[" ", " "],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(c[ñ][ii], end = " ")
                    print()

            if i == "d": 
                d = ([["·", "·"],[" ", "·"],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(d[ñ][ii], end = " ")
                    print()

            if i == "e": 
                e = ([["·", " "],[" ", "·"],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(e[ñ][ii], end = " ")
                    print()

            if i == "f": 
                f = ([["·", "·"],[" ", "·"],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(f[ñ][ii], end = " ")
                    print()
    
            if i == "g": 
                g = ([["·", "·"],["·", "·"],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(g[ñ][ii], end = " ")
                    print()

            if i == "h": 
                h = ([["·", " "],["·", "·"],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(h[ñ][ii], end = " ")
                    print()

            if i == "i": 
                i = ([[" ", "·"],["·", " "],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(i[ñ][ii], end = " ")
                    print()

            if i == "j": 
                j = ([[" ", "·"],["·", "·"],[" ", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(j[ñ][ii], end = " ")
                    print()

            if i == "k": 
                k = ([["·", " "],[" ", " "],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(k[ñ][ii], end = " ")
                    print()

            if i == "l": 
                l = ([["·", " "],["·", " "],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(l[ñ][ii], end = " ")
                    print()

            if i == "m":
                m = ([["·", "·"],[" ", " "],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(m[ñ][ii], end = " ")
                    print()

            if i == "n": 
                n = ([["·", "·"],[" ", "·"],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(n[ñ][ii], end = " ")
                    print()

            if i == "ñ":
                ñ = ([["·", "·"],["·", "·"],[" ", "·"]])
                for ñ in range(3):
                    for ii in range(2):
                        print(n[ñ][ii], end = " ")
                    print()

            if i == "o": 
                o = ([["·", " "],[" ", "·"],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(o[ñ][ii], end = " ")
                    print()

            if i == "p": 
                p = ([["·", "·"],["·", " "],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(p[ñ][ii], end = " ")
                    print()

            if i == "q":
                q = ([["·", "·"],["·", "·"],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(q[ñ][ii], end = " ")
                    print()

            if i == "r": 
                r = ([["·", " "],["·", "·"],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(r[ñ][ii], end = " ")
                    print()
        
            if i == "s": 
                s = ([[" ", "·"],["·", " "],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(s[ñ][ii], end = " ")
                    print()

            if i == "t":
                t = ([[" ", "·"],["·", "·"],["·", " "]])
                for ñ in range(3):
                    for ii in range(2):
                        print(t[ñ][ii], end = " ")
                    print()

            if i == "u":
                u = ([["·", " "],[" ", " "],["·", "·"]])
                for ñ in range(3):
                    for ii in range(2):
                        print(u[ñ][ii], end = " ")
                    print()

            if i == "v":
                v = ([["·", " "],["·", " "],["·", "·"]])
                for ñ in range(3):
                    for ii in range(2):
                        print(v[ñ][ii], end = " ")
                    print()

            if i == "w":
                w = ([[" ", "·"],["·", "·"],[" ", "·"]])
                for ñ in range(3):
                    for ii in range(2):
                        print(w[ñ][ii], end = " ")
                    print()

            if i == "x":
                x = ([["·", "·"],[" ", " "],["·", "·"]])
                for ñ in range(3):
                    for ii in range(2):
                        print(x[ñ][ii], end = " ")
                    print()

            if i == "y":
                y = ([["·", "·"],[" ", "·"],["·", "·"]])
                for ñ in range(3):
                    for i in range(2):
                        print(y[ñ][ii], end = " ")
                    print()

            if i == "z":
                z = ([["·", " "],[" ", "·"],["·", "·"]])
                for ñ in range(3):
                    for i in range(2):
                        print(z[ñ][ii], end = " ")
                    print()

            if i == ".":
                punto = ([[" ", " "],[" ", " "],["·", " "]])
                for ñ in range(3):
                    for i in range(2):
                        print(punto[ñ][ii], end = " ")
                    print()

            if i == ",":
                coma = ([[" ", " "],["·", " "],[" ", " "]])
                for ñ in range(3):
                    for i in range(2):
                        print(coma[ñ][ii], end = " ")
                    print()
        return entrada.set(palabra)
                    
    ven.destroy()
    venB=Tk()
    imagenf=PhotoImage(file="braille.png")
    labelFondo=Label(venB,image=imagenf)
    labelFondo.place(x=0,y=0,relwidth=1.0,relheight=1.0)
    venB.title("Traductor") 
    venB.geometry("700x600+350+120")
    venB.resizable(0,0)
    venB.iconbitmap("icono.ico")
    labelTitulo=Label(venB, text="braille",fg="white", bg="#3498DB", font="arial 25 italic bold").place(x=450,y=50)
       

    
    
    imagenc=PhotoImage(file="codigo-braille.gif")
    imagenc=imagenc.zoom(60)
    imagenc=imagenc.subsample(80)
    labelFoto=Label(venB,image=imagenc)
    labelFoto.place(x=200,y=120)
    lblpalabra=Label(venB,text="digite lo que quiere traducir: ", font="arial 14 italic bold ").place(x=20,y=420)
    entrada=StringVar()
    txt=Entry(venB)
    txt.place(x=310,y=420)
    btn=Button(venB, text="traducir", command=tra).place(x=450,y=420)
    lblRes=Label(venB,textvariable=entrada).place(x=300, y=500)
    venB.mainloop()
ven=Tk()
imagenf=PhotoImage(file="fondo.png")
labelFondo=Label(ven,image=imagenf)
labelFondo.place(x=0,y=0,relwidth=1.0,relheight=1.0)
ven.title("Traductor")
ven.geometry("700x600+350+120")
ven.resizable(0,0)
ven.iconbitmap("icono.ico")
etiqueta=Label(ven, text="traductor",fg="white", bg="#3498DB", font="arial 25 italic bold").place(x=300,y=80)
imaBtn1=Button(ven, text="senales", command=senales).place(x=300,y=150)
imaBtn2=Button(ven, text="braille", command=braille).place(x=300,y=200)
imaBtn3=Button(ven, text="morse", command=morse).place(x=300,y=250)
ven.mainloop()
















