#Passo passo do Projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

#Passo 2: Fazer login
#passo 3: Importar a base de dados de produtos
#passo 4: Cadastrar 1 produto
#passo 5 Repetir o cadastro para todos os produtos


# Bibliotecas importadas
import pyautogui # Para instalar - pip install pyautogui
import time
import pandas # para Instalar - pip install pandas numpy openpyxl

# pyautogui.click -> clicar com o  mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (combinação de teclas ex crtl + c)


#pausa entre cada comando do pyautogui
pyautogui.PAUSE = 1.0

#abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "shift", "n") #abrindo guia anonima
# time.sleep(3)

# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# Fazer login
pyautogui.click(x=2767, y=389)
pyautogui.write("niltonbarbosa.nb@gmail.com")
pyautogui.press("tab") #passando para o campo senha
pyautogui.write("123495")
pyautogui.press("tab") #passando para o campo de login
pyautogui.press("enter")

#Espera o site carregar
time.sleep(3)

# Importar a base de dados de produtos
tabela = pandas.read_csv("produtos.csv")


# condição de repetição
for linha in tabela.index:

    #codigo = tabela.loc[linha, 'codigo'] -> pode ser realizado dessa forma, adicioando dentro de uma varial. e depois passar a varial dentro do pyautogui.write(VARIAVEL)
    #pode ser passar o parametro tabela.loc[linha, 'codigo'] dentro pyautogui.write(tabela.loc[linha, 'codigo']).
    
    # Preenchendo a tabela.
    pyautogui.click(x=2762, y=282)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    #Verifica se a coluna OBS esta vazia (NaN), caso sim pula para o botão enviar.
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    #aperta o botão enviar
    pyautogui.press("tab") # passa para o botão de login
    pyautogui.press("enter")

    # subir o scrol para o topo
    pyautogui.scroll(50000)









