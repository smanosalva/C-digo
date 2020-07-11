import winsound
import time


def morse():
    palabra=input('Ponga su palabra: ')
    palabra=palabra.lower()
    list(palabra)
    mostrar=[]
    for i in palabra:
        if i=='a':
            winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            a='.-'
            mostrar.append(a)
        if i=='b':
            winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            b='-...'
            mostrar.append(b)
        if i=='c':
            winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            c='-.-.'
            mostrar.append(c)
        if i=='d':
            winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            d='-..'
            mostrar.append(d)
        if i=='e':
            winsound.Beep(500,500),time.sleep(1.5)
            e='.'
            mostrar.append(e)
        if i=='f':
            winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            f='..-.'
            mostrar.append(f)
        if i=='g':
            winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            g='--.'
            mostrar.append(g)
        if i=='h':
            winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            h='....'
            mostrar.append(h)
        if i=='i':
            winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            i='..'
            mostrar.append(i)
        if i=='j':
            winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            j='.---'
            mostrar.append(j)
        if i=='k':
            winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            k='-.-'
            mostrar.append(k)
        if i=='l':
            winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            l='.-..'
            mostrar.append(l)
        if i=='m':
            winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            m='--'
            mostrar.append(m)
        if i=='n':
            winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            n='-.'
            mostrar.append(n)
        if i=='ñ':
            winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            ñ='--.--'
            mostrar.append(ñ)
        if i=='o':
            winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            o='---'
            mostrar.append(o)
        if i=='p':
            winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            p='.--.'
            mostrar.append(p)
        if i=='q':
            winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            q='--.-'
            mostrar.append(q)
        if i=='r':
            winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,500),time.sleep(1.5)
            r='.-.'
            mostrar.append(r)
        if i=='s':
            winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            s='...'
            mostrar.append(s)
        if i=='t':
            winsound.Beep(500,1500),time.sleep(1.5)
            t='-'
            mostrar.append(t)
        if i=='u':
            winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            u='..-'
            mostrar.append(u)
        if i=='v':
            winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            v='...-'
            mostrar.append(v)
        if i=='w':
            winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            w='.--'
            mostrar.append(w)
        if i=='x':
            winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),winsound.Beep(500,1500),time.sleep(1.5)
            x='-..-'
            mostrar.append(x)
        if i=='y':
            winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,1500),winsound.Beep(500,1500),time.sleep(1.5)
            y='-.--'
            mostrar.append(y)
        if i=='z':
            winsound.Beep(500,1500),winsound.Beep(500,1500),winsound.Beep(500,500),winsound.Beep(500,500),time.sleep(1.5)
            z='--..'
            mostrar.append(z)
        if i==' ':
            time.sleep(2.5)
            esp=' '
            mostrar.append(esp)
        
        cadena = " ".join(mostrar)
        print(cadena)
                

morse()
