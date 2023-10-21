from tkinter import *
#Janela do programa
root = Tk()
root.title('Calculadora')
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)

numero1 = ''
div = FALSE
mul = FALSE
ad = FALSE
sub = FALSE

root.configure(background='#000')
#Tela da calculadora
e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#000', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
#Operadores
def botao_click(num):
    e.insert(END, num)

def botao_div():
    global numero1
    global div
    div = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_mul():
    global numero1
    global mul
    mul = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_sub():
    global numero1
    global sub
    sub = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_ad():
    global numero1
    global ad
    ad = TRUE
    numero1 = e.get()
    e.delete(0, END)

def botao_clear():
    e.delete(0, END)

def botao_igual():
    global ad
    global sub
    global mul
    global div
    numero2 = e.get()
    e.delete(0, END)
    #Lógica das operações
    if ad == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        ad = FALSE
    if sub == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        sub = FALSE
    if mul == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        mul = FALSE
    if div == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        div = FALSE    
#Botões do programa
div = Button(
    root, 
    text='÷', 
    padx=40, 
    pady=20, 
    command=botao_div, 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
div.grid(row=0, column=4)

#Primeira fileira
um = Button(
    root, 
    text='1', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(1), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
um.grid(row=1, column=1)

dois = Button(
    root, 
    text='2', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(2), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
dois.grid(row=1, column=2)

tres = Button(
    root, 
    text='3', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(3), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
tres.grid(row=1, column=3)

mul = Button(
    root, 
    text='x', 
    padx=40, 
    pady=20, 
    command=botao_mul,
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
mul.grid(row=1, column=4)

#Segunda fileira
quatro = Button(
    root, 
    text='4', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(4), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)

cinco = Button(
    root, 
    text='5', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(5), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)

seis = Button(
    root, 
    text='6', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(6), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
seis.grid(row=2, column=3)

sub = Button(
    root, 
    text='-', 
    padx=41.5, 
    pady=20, 
    command=botao_sub,
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
sub.grid(row=2, column=4)

#Terceira fileira
sete = Button(
    root, 
    text='7', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(7), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
sete.grid(row=3, column=1)

oito = Button(
    root, 
    text='8', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(8), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
oito.grid(row=3, column=2)

nove = Button(
    root, 
    text='9', 
    padx=40, 
    pady=20, 
    command=lambda: botao_click(9), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
nove.grid(row=3, column=3)

ad = Button(
    root, 
    text='+', 
    padx=40, 
    pady=20, 
    command=botao_ad,
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
ad.grid(row=3, column=4)

#Quarta fileira
zero = Button(
    root, 
    text='0', 
    padx=91, 
    pady=20, 
    command=lambda: botao_click(0), 
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
zero.grid(row=4, column=1, columnspan=2)

clear = Button(
    root, 
    text='c', 
    padx=40, 
    pady=20, 
    command=botao_clear,
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
clear.grid(row=4, column=3)

igual = Button(
    root, 
    text='=', 
    padx=40, 
    pady=20, 
    command=botao_igual,
    fg='#000', 
    activeforeground='#000',
    bg='#Ffcbdb', 
    activebackground='#FE48AA',
    relief=FLAT,
    font=('futura', 12, 'bold')
)
igual.grid(row=4, column=4)


root.mainloop()