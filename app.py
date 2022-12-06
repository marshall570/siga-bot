import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

try:
    load_dotenv()
    user = os.getenv('USER-LOGIN')
    pswd = os.getenv('USER-PSWD')
    
    user_input = '#vSIS_USUARIOID'
    pswd_input = '#vSIS_USUARIOSENHA'
    login_button = '.Button'
    span_notas = '#ygtvlabelel10Span'

    firefox_options = Options()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(2)

    driver.get('https://siga.cps.sp.gov.br/aluno/login.aspx')
    driver.find_element(By.CSS_SELECTOR, user_input).send_keys(user)
    driver.find_element(By.CSS_SELECTOR, pswd_input).send_keys(pswd)
    driver.find_element(By.CSS_SELECTOR, login_button).click()
    driver.find_element(By.CSS_SELECTOR, span_notas).click()
    
    for i in range(1, 11):
        if i < 10:
            nome = driver.find_element(
                By.ID,
                f'span_vACD_DISCIPLINANOME_000{i}'
            ).get_attribute('textContent')

            nota = driver.find_element(
                By.ID,
                f'span_vACD_ALUNOHISTORICOITEMMEDIAFINAL_000{i}'
            ).get_attribute('textContent')
        else:
            nome = driver.find_element(
                By.ID,
                f'span_vACD_DISCIPLINANOME_00{i}'
            ).get_attribute('textContent')

            nota = driver.find_element(
                By.ID,
                f'span_vACD_ALUNOHISTORICOITEMMEDIAFINAL_00{i}'
            ).get_attribute('textContent')

        print(f'{nota} - {nome}')

    driver.quit()

except Exception as e:
    print(e)
