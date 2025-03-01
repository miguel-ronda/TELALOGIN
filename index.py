#importar as blibliotecas
from tkinter import*# IMPORTA TODODS OS MODULOS DO TKINTER
from tkinter import messagebox #importa o modulo de caixas de menasgem do tkinter 
from tkinter import ttk #importa o modulo de widgets tematicos do tkinter
from Database import database   # importa a classe database do modulo DataBase

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
usuarioEntry.place(x=120,y=110)#posicione o campo de entrada

senhaLabel=Label(rightFrame,text="senha:",font=("century gothic",20),bg="MIDNIGTHBLUE",fg="white")
#cria um label para senha 
senhaLabel.place(x=5,y=150)#posicione o label mo frame direito

senhaEntry= ttk.Entry(rightFrame,width=30,show="*")
#cria um campo de entrada para senha 
senhaEntry.place(x=120,y=165)#posicione o campo de entrada

#funcao de login 
def Login():
    usuario = usuarioEntry.get()#obtem o valor do campo de entrada do usuario
    senha = senhaEntry.get()#obtem o valor do campo de entrada da senha 

    #conectar ao banco de dados 
    db= Database()#cria uma instacia da classe database =
    db.cursor.execute("""SELECT * FROM usuario WHERE usuario = %s and senha = %s""",(usuario,senha))#execute a consulta SQL para verificar o usuario e a senha 
    verifyLogin = db.cursor.fetchone() #obtem o resultado da consulta
    #verufucar se o usuario foi encontrado 
    if verifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="acesso confirmado. bem vindo!")# exibe mensagem de sucesso 
    else:
        messagebox.showinfo(title="INFO LOGIN", message="acesso negado .verifique se esta cadastrado no sistema")#exibe o erro
#criando botoes
LoginButton = ttk.Button(rightFrame,text="login",width=15,command=Login)#cria um botao login 
LoginButton.place(x=150,y=225)#cria um botao login 
#funcao para regidtrar novo usuario 
def registrar():
    #removendo botoes de login
    LoginButton.place(x=5000)#move o botao de login para fora da tela 
    registerButton.place(x=5000)#move o botao de registro para fora da tela 

#inserindo widgets de cadastro 
NomeLabel = Label(rightFrame,text="nome:",font=("century gothic",20),bg="MIDNIGHTBLUE",fg="white") #cria im label para email
NomeLabel.place(x=5,y=5) #posiciona o label mo frame direito 
NomeEntry = ttk.Entry(rightFrame,width=30)#cria imum campo de entrada

emailLabel=Label(rightFrame,text="email:",font=("century gothic",20,),bg= "MIDNIGHTBLUE",fg='white')#cria um label  oara o email
emailLabel.place(x=5,y=40)#posione o label no frame direito 
emailEntry=ttk.entry(rightFrame,width=30)
emailEntry.place(x=120,y=55)

#funcao para reigistrar no banco de dados 
def registrarnobanco():
    nome= NomeEntry.get() #obtem o valor do campo de entrada di nome 
    email= emailEntry.get() #obtem o valor do campo de entrada di email
    senha= senhaEntry.get() #obtem o valor do campo de entrada di senha 
    usuario= usuarioEntry.get() #obtem o valor do campo de entrada di usuario 
    if nome == "" or email == "" or usuario == "" or senha == "":
        messagebox.showerror(title="erro de registro",message="PRENCHA TODOS OS CAMPOS")# exibe mensagem de erro
    else:
        db = Database()# cria uma instancia da classe database
        db.registrarnobanco(nome,email,usuario,senha)
        # chama o metodo para registrar no bsnvo de dados
        messagebox.showinfo("sucesso","usuario registrado com sucesso!")#exibe a mensagem de sucesso 


        #limpar os campos apos o registro
        NomeEntry.delete(0,END)#LIMPA O CAMPO DE ENTRADA do nome
        emailEntry.delete(0,END)#LIMPA O CAMPO DE ENTRADA do email 
        usuarioEntry.delete(0,END)#LIMPA O CAMPO DE ENTRADA do usuario 
        senhaEntry.delete(0,END)#LIMPA O CAMPO DE ENTRADA da senha

register= ttk.Button(rightFrame,text="REGISTRAR",width=15,command=registrarnobanco)#cria um botao de registro
register.place(x=150,y=225)

#funcao para voltar para a tela de login 
def voltarlogin():
    NomeLabel.place(x=5000)#move o label do nome para fora da tela
    NomeEntry.place(x=5000)#move o campo de entrada do nome para fora da tela
    emailLabel.place(x=5000)#move o label do email para fora da tela
    registerButton.place(x=5000)#move o botao do registro para fora da tela
    voltar.place(x=5000)#move o botao do registro para fora da tela

    # trazendo de volta os widgets 
    LoginButton.place(x=150)# traz o botao de login de volta para a tela 
    registerButton.place(x=150)# traz o botao de registro de volta para a tela 
    
    voltar= ttk.Button(rightFrame,text="voltar",width=15,command=voltarlogin)#cria o botao fr voltar 
    voltar.place(x=150,y=255)#posiciona o botao de voltar 
registerButton=ttk.Button(rightFrame,text="REGISTRAR",witdh=15,command=registrar)#cria um botao de registro 
registerButton.place(X=150,y=255)#posiciona o botao de registro 

#iniciar o loop principal 
jan.mainloop()





