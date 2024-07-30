#Bibliotecas
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import webbrowser, os
import pyautogui

#Pede para fechar todas as janelas e manter somente o programa ativo,
#apos tudo fechado aperta enter, e digite a mensagem que o cliente irá receber em seu Whatsapp
conferindo = input("\n\nEnquanto esse programa estiver rodando, não mexa no computador!!\nAperte enter para continuar!\n\n")
msg_cliente = input("Digite a mensagem que o cliente irá receber: \n\n")

#Abre o diretório que está os cardapios, aguarda carregamento por 2 segundos, muda a tela para
#o cardapio usando alt + tab (por isso da conferencia de estar tudo fechado), aguarda 1 segundo por garantia,
#seleciona tudo e copia usando PYAUTOGUI
os.startfile(os.path.realpath(r".\cardapio"))
time.sleep(2)
pyautogui.hotkey('alt', 'tab') #Se estiver rodando em IDE, é necessário habilitar a linha 21 e 22, se não buga
time.sleep(1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')

#Carregando banco de dados onde contém os contatos usando Panda
contatos_df = pd.read_excel(r".\Contatos.xlsx")

#Usando Selenium, abre o navegador no Whastapp Web
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

#Aguardo o login com o QRCODE, quando pagina toda carregada, segue
while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

#faz a tentativa com Try, se conseguir perfeito, se não vai para excessão e pula o número
#Envio de mensagem usando o link, percorre o banco de dados, organiza os dados para poder usar em link
#abre o link e segue
for i, mensagem in enumerate(contatos_df['Número']):
    try:
        numero = contatos_df.loc[i, "Número"]
        link = f"https://web.whatsapp.com/send?phone={numero}&text={msg_cliente}"
        navegador.get(link)
    
        #Aguarda a pagina carregar, localizando o elemento "side" no HTML, após localizado aguarda
        #o carregamento completo da pagino por 5 segundos
        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(1) 
        time.sleep(5)   
    
        #Variavel "elem_xpath" contem o XPATH do elemento que precisa ser localizado,
        #localiza o elemento "caixa de texto" no HTML pelo XPATH, e aperta enter, aguarda 2 segundos
        #para continuar
        elem_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span'
        navegador.find_element(By.XPATH, f'{elem_xpath}').send_keys(Keys.ENTER)
        time.sleep(2)

        #enviando cardápios que estão na area de tranferencia, aguardando 10 segundos para carregar fotos
        #aperta enter e aguarda 5 segundos até enviar
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(5)
        pyautogui.hotkey('enter')
        time.sleep(5)

    #exceção caso o número de telefone estiver errado ou não localizar, então enviar mensagem dizendo qual número é
    except NoSuchElementException:
        print("\nO número ", numero, " não funcionou!\n")
