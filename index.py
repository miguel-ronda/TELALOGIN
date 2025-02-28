#importar as blibliotecas
from tkinter import*# IMPORTA TODODS OS MODULOS DO TKINTER
from tkinter import messagebox #importa o modulo de caixas de menasgem do tkinter 
from tkinter import ttk #importa o modulo de widgets tematicos do tkinter
from DataBase import database # importa a classe database do modulo DataBase

#criar janela
jan = Tk() #cria uma instancia da janela principal 
jan.title ("SL Systens - painel de acesso")#define o titulo da janela
jan.geometry ("600X300") #define o tamanho da janela 
jan.configure(background="white")#configura a cor da janela
jan.resizable(witdh=False,heigh=False)#impede que a janela seja redeimensionada 

#comando para deixar a tela transparente 
jan.atributes("-alpha",0.9)#define a transparencia da janela (0.0 a 1.0)

#definir icone da janela 
#jan.iconbitmap(default="icons/1logoicon.ico")#define o icone da janela 

#carregar imagem 
logo=PhotoImage(file="ICONS/miguelronda.png")#carrega a imagem do logo 

#criar frame 
leftFrame = Frame(jan,width=395,height=300,bg="MIDNIGHTBLUE",relief="raise")#criar um frame a esquerda 
leftFrame.pack(side=LEFT)#posiciona na esquerda

rightFrame = Frame(jan,width=395,height=300,bg="MIDNIGHTBLUE",relief='raise')#criar um frame a direita
rightFrame.pack(side=RIGHT)#posiciona na direita 

#ADICIONAR LOGO 
LogoLabel = Label(leftFrame,image=logo,bg="MIDNIGTHBLUE") #CRIAR UM LABEL PARA A IMAGEM DO LOGO 
LogoLabel.place(x=50,y=100)# posiciona o label no frame esquerdo 

#adicionar campos de ususario e senha 
usuarioLabel = Label(rightFrame,text="usuario",font=("century gothic",20),bg="MIDNIGTHBLUE",fg="white")
#cria um label para o usuario 
usuarioLabel.place(x=5,y=100)#posiciona o label no frame direito 
usuarioEntry = ttk.Entry(rightFrame,width=30) #cria um campo de entrada para o usuario 
usuarioEntry.place(x=)
