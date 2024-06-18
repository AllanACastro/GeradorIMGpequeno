import pandas as pd
from tkinter import *
import customtkinter as ctk
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import os
import datetime
from PIL import Image, ImageDraw, ImageFont, ImageTk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

df= pd.read_excel('Aniversariantes - Automatico.xlsx', sheet_name = "Envios")
df['Data de Nascimento+'] = pd.to_datetime(df['Data de Nascimento+'], format='%d/%m/%Y', errors='coerce')
data_hoje = datetime.datetime.now().strftime('%d/%m')
aniversariantes_hoje = df[df['Data de Nascimento+'].dt.strftime('%d/%m') == data_hoje]


aniversario = aniversariantes_hoje['Nome Completo']
socio = aniversariantes_hoje['Sociedade']
sexo = aniversariantes_hoje['Sexo']
telefone = aniversariantes_hoje['Telefone']

def process(aniversario, socio, sexo, telefone):

    numerador = 0

    for x,y,z,a in zip(aniversario, socio, sexo, telefone):
        
        if y == "SÓCIO":
            img = "sociedade.jpg"
            posicao_y = 365
        else:
            img = "aniversario.jpg"
            posicao_y = 365

        
        
        if z != 'M':
            sexo = 'Dra.'
        else:
            sexo = 'Dr.'


        # Abrir a imagem
        imagem = Image.open(img)
        

        # Criar um objeto ImageDraw para adicionar texto à imagem
        desenho = ImageDraw.Draw(imagem)

        # Especificar a fonte e o tamanho do texto
        fonte = ImageFont.truetype("arial.TTF", 44)

        # Especificar a cor do texto (R, G, B)
        cor = (255, 255, 255)  # Cor preta

        # Especificar a posição do texto (x, y)
        

        texto = f"{sexo} {x}"

        tamanho_texto = desenho.textlength(texto, font=fonte)
        
        largura_imagem = imagem.width

        posicao_x = ((largura_imagem - tamanho_texto) / 2)+105

        


        # Texto que você deseja adicionar
        

        # Adicionar o texto à imagem
        desenho.text((posicao_x, posicao_y), texto, fill=cor, font=fonte)

        if not os.path.exists("Imagens"):
            os.makedirs("Imagens")

        caminho_salvar = os.path.join("Imagens", f"Aniversario - {x} - {numerador} .jpg")
        # Salvar a imagem com o texto adicionado
        imagem.save(caminho_salvar)
        numerador = numerador+1
        # imagem = Image.open(f"Certificado - {nome}.jpg")

        # Fechar a imagem original
    imagem.close() 
    




data_e_hora_atual = datetime.datetime.now()
data_e_hora_formatada = data_e_hora_atual.strftime("%d/%m/%Y")

janela = ctk.CTk()
janela.title('Aniversariantes')
janela.geometry("250x300")

janela.resizable(0, 0)
janela.iconbitmap("icon.ico")

bg_image = Image.open("bg.png")
bg_image = bg_image.resize((250 , 300), Image.ADAPTIVE)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = ctk.CTkLabel(janela, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)



FILE = '-'



texto_orientacao = ctk.CTkLabel(janela, text='Aniversariantes!\nGerador de imagem', bg_color='#FFFFFF' )
texto_orientacao.pack(pady = 40)
texto_orientacao.configure(font=("Courier", 17, "bold"))


# btn_arquivo = ctk.CTkButton(janela, text='Selecione sua lista', command=lambda: botao_enviararquivo() )
# btn_arquivo.pack(pady=10)

# def botao_enviararquivo():
#     global FILE
#     file = askopenfile(initialdir= os.getcwd(), mode='r')
#     FILE = file.name
#     texto_orientacao4 = Label(janela, text=f'Arquivo Selecionado!', font='Courier 11', background='#FFFFFF')
#     texto_orientacao4.pack()


resultado = pd.merge(aniversario ,telefone, how='right', on= aniversario)
del resultado['key_0']
resultado.set_index('Telefone', inplace = True)



def msg():
    msg1= f"{resultado}"
    messagebox.showinfo("Alerta!", msg1)



processar_arq = ctk.CTkButton(janela, text='Iniciar', command=lambda: [process(aniversario, socio, sexo, telefone), msg()])
processar_arq.pack(pady= 10)

label_hora = ctk.CTkLabel(janela, text=f"Aniversariantes\ndo dia:\n{data_e_hora_formatada}", bg_color='#FFFFFF',font = ("Courier", 17, "bold"))
label_hora.pack(pady = 10)


# verificabtn = ctk.CTkButton(janela, text='Verificar Cpf', command=lambda: [numeroFolha.get(), verificarCPF(FILE)])
# verificabtn.pack(pady=2)


janela.mainloop()