import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#----Xpath capital----
div_capital = "//*[@id='rso']/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]"

#----Leer el archivo de Excel----
excel_file_path = 'paises.xlsx'
read = pd.read_excel(excel_file_path)

#----Crear una nueva columna Capital----
read['Capital'] = ''

#----Abrir navegador----
chrome_options = Options()
driver = webdriver.Chrome()
driver.maximize_window()

#----Iterar y buscar las capitales----
for index, row in read.iterrows():
    country_name = row['País']
    
    #----Busqueda en Google----
    search_query = f'{country_name} capital'
    driver.get(f'https://www.google.com/search?q={search_query}')
    
    #----Conseguir la información de la capital----
    try:
        capital_element = driver.find_element(By.XPATH, div_capital)
        capital = capital_element.text
    except:
        capital = 'No encontrado'

    #----Almacenar en el DataFrame----
    read.at[index, 'Capital'] = capital

#----Cerrar el navegador----
driver.quit()

#----Guardar los resultados en un nuevo archivo de Excel----
output_excel_file_path = 'C:/Users/Diego/Downloads/resultados.xlsx'
read.to_excel(output_excel_file_path, index=False)

print(f'Los resultados se han guardado en: {output_excel_file_path}')
