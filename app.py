import os
from logging import error
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


try:
    # CARREGAR INFO DO ALUNO COM O .ENV
    load_dotenv()
    user = os.getenv('USER-LOGIN')
    pswd = os.getenv('USER-PSWD')

    # SELECTORS NECESSÁRIOS
    user_input = '#vSIS_USUARIOID'
    pswd_input = '#vSIS_USUARIOSENHA'
    login_button = '.Button'
    span_notas = '#ygtvlabelel10Span'

    # CRIAR WEBDRIVER FIREFOX
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(2)

    # OBTER NOTAS
    driver.get('https://siga.cps.sp.gov.br/aluno/login.aspx')

    driver.find_element(By.CSS_SELECTOR, user_input).send_keys(user)
    driver.find_element(By.CSS_SELECTOR, pswd_input).send_keys(pswd)
    driver.find_element(By.CSS_SELECTOR, login_button).click()

    driver.find_element(By.CSS_SELECTOR, span_notas).click()

    for i in range(1, 8):
        nome = driver.find_element(
            By.ID,
            f'span_vACD_DISCIPLINANOME_000{i}'
        ).get_attribute('textContent')

        nota = driver.find_element(
            By.ID,
            f'span_vACD_ALUNOHISTORICOITEMMEDIAFINAL_000{i}'
        ).get_attribute('textContent')

        print(f'{nota} - {nome}')

    driver.quit()

except Exception as e:
    error(e)
