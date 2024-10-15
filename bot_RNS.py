from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import os
import csv
from unidecode import unidecode
from pathlib import Path


erros=[]
count_erros = 0



def verificar_extensao(arquivo, extensao):
    # Cria um objeto Path
    p = Path(arquivo)
    return p.suffix.lower() == extensao.lower()


def nome_cidades():
    with open('cidades.csv','r', newline='\n') as file:
        csvfile = csv.reader(file, delimiter=';')
        linhas=[]
        for n, line in enumerate(csvfile):
            linhas.append( unidecode(line[0]).lower())
            print(n,line)
    return linhas

def renomear_arquivo(number):
    downloads_folder = "C:\\Users\\User\\Downloads"
    list_of_files = os.listdir(downloads_folder)
    list_of_files.sort(key=lambda x: os.path.getmtime(os.path.join(downloads_folder, x)))
    last_downloaded_file = list_of_files[-1]
    last_downloaded_file_path = os.path.join(downloads_folder, last_downloaded_file)
    if not verificar_extensao(last_downloaded_file,'.xlsx'): 
        time.sleep(3)


    if verificar_extensao(last_downloaded_file,'.xlsx') and last_downloaded_file != str(number-1)+'.xlsx': 
        print("Último arquivo baixado:", last_downloaded_file)
        new_file_name = str(number)+'.xlsx' 
        new_file_path = os.path.join(downloads_folder, new_file_name)

        # Renomeia o arquivo
        if os.path.isfile(new_file_path):
            print("Arquivoja existe!")
            print("erro arquivo:")
            erros.append(number)
            print(number)


        else:
            os.rename(last_downloaded_file_path, new_file_path)
            print("Arquivo renomeado para:", new_file_name)

    else:
        print("erro arquivo:")
        erros.append(number)
        print(number)
        global count_erros
        count_erros+=1



# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Open browser in maximized mode

service = Service('chromedriver.exe')
# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=options)


def reiniciar_chrome():
    driver.quit()

    driver2 = webdriver.Chrome(service=service, options=options)
    driver2.get('https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/docs/renaest')
    #Espera modulo carregar
    print("Esperando carregar módulo RNS...")
    for i in range(0,11):
        print(str(i)+'s')
        time.sleep(1) 

    #Move o mouse para o botão "MUNICIPIOS"
    pyautogui.moveTo(897, 696, duration=0.5)
    #CLICK para ATIVAR a SCREEN
    pyautogui.click(x=897, y=696, button='left')
    time.sleep(0.5) 

    #Reduz a tela do CHROME
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    time.sleep(0.5)
    print("E lá vamos nós!")

try:
    # Open a webpage
    driver.get('https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/docs/renaest')


    #Espera modulo carregar
    print("Esperando carregar módulo RNS...")
    for i in range(0,11):
        print(str(i)+'s')
        time.sleep(1) 

    #Move o mouse para o botão "MUNICIPIOS"
    pyautogui.moveTo(897, 696, duration=0.5)
    #CLICK para ATIVAR a SCREEN
    pyautogui.click(x=897, y=696, button='left')
    time.sleep(0.5) 

    #Reduz a tela do CHROME
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    time.sleep(0.5)

    cidades = []
    cidades = nome_cidades()
    print("LET's GOOOO")
    count_reiniciar=0
    faltantes=[79, 152, 361, 893, 926, 1135, 1177, 1200, 1202, 1229, 1231, 1260, 1288, 1291, 1437, 1482, 1484, 1547, 1549, 1551, 1553, 1769, 1908, 1910, 2130, 2132, 2153, 2775, 2777, 2779, 2927, 2929, 3108, 3382, 3384, 3943, 4143, 4387, 4401, 5222]
    for index,cidade in enumerate(cidades):

        if(index in faltantes):
            #########ROTINA###########
            #contador para reinciar serviço
            count_reiniciar+=1

            print(str(index)+'.'+cidade)
            #CLICK para botão "MUNICIPIOS"
            pyautogui.click(x=897, y=696, button='left')
            time.sleep(0.3)
            #LIMPA QLQR COISA
            pyautogui.moveTo(930, 722, duration=0.5)
            pyautogui.click(x=930, y=722, button='left') 
            time.sleep(0.3)
            pyautogui.press('tab')#download
            time.sleep(0.3)   

            #SEARCH pelo nome da cidade
            pyautogui.typewrite(cidade, interval=0.2)
            time.sleep(0.3) 

            #HOVER a primeira cidade
            pyautogui.press('tab')#hover o primeiro
            time.sleep(0.2) 

            #SELECIONA a primeira cidade
            pyautogui.press('space')
            time.sleep(0.2)     

            #FECHA BOTAO MUNICIPIOS
            pyautogui.click(x=897, y=696, button='left')
            time.sleep(1) 

            pyautogui.press('esc')
            time.sleep(0.5) 


            pyautogui.moveTo(897, 540, duration=0.5) 
            time.sleep(0.3) 
            pyautogui.drag(3, 0, 0.5, button='right')
            #dados
            pyautogui.moveTo(964, 570, duration=0.3)
            pyautogui.click(x=964, y=570, button='left')
            time.sleep(0.3) 
            pyautogui.moveTo(951, 584, duration=0.5)
            pyautogui.click(x=951, y=584, button='left')


            time.sleep(0.5) 
            pyautogui.press('tab')#download
            time.sleep(0.5)   
            pyautogui.press('enter')#salvar
            time.sleep(0.5)
            pyautogui.press('esc')#escape qlqr coisa
            time.sleep(0.5)        

            #RENOMEIA ARQUIVO
            renomear_arquivo(index)

            #CLICK para botão "MUNICIPIOS"
            # pyautogui.moveTo(897, 696, duration=0.5)
            # pyautogui.click(x=897, y=696, button='left')
            # time.sleep(0.5) 

            # #HOVER o PRIMEIRO
            # pyautogui.press('tab')#hover o primeiro
            # time.sleep(0.5) 

            # #DESELECIONA O MUNICIPIO
            # pyautogui.press('space')
            # time.sleep(0.5)
            #DESELECIONA TODOS OS MUNICIPIOS
            # pyautogui.moveTo(930, 722, duration=0.5)
            # pyautogui.click(x=930, y=722, button='left')
            # time.sleep(1) 


            # pyautogui.click(x=897, y=696, button='left')
            # time.sleep(1.5) 
            print("ERROS: ",erros)
            if count_reiniciar==100:
                count_reiniciar=0
                reiniciar_chrome()

            if count_erros==3:
                count_erros=0
                reiniciar_chrome()


        else:
            pass

    time.sleep(60)

finally:
    # Close the driver
    driver.quit()
