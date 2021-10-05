import os
from logging import error
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options

try:
    # CARREGAR .ENV DO ALUNO
    load_dotenv()

    # SELECTORS NECESSÁRIOS
    user_input = '#vSIS_USUARIOID'
    pswd_input = '#vSIS_USUARIOSENHA'
    login_button = '.Button'
    span_notas = '#ygtvlabelel10Span'

    # CRIAR WEBDRIVER
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(2)

    # OBTER NOTAS
    driver.get('https://siga.cps.sp.gov.br/aluno/login.aspx')

    driver.find_element_by_css_selector(user_input).send_keys(os.getenv('USER-LOGIN'))
    driver.find_element_by_css_selector(pswd_input).send_keys(os.getenv('USER-PSWD'))
    driver.find_element_by_css_selector(login_button).click()
    
    driver.find_element_by_css_selector(span_notas).click()

    for i in range(1, 9):
        nome = driver.find_element_by_id(f'span_vACD_DISCIPLINANOME_000{i}').get_attribute('textContent')

        nota = driver.find_element_by_id(f'span_vACD_ALUNOHISTORICOITEMMEDIAFINAL_000{i}').get_attribute('textContent')

        print(f'{nota} - {nome}')

    driver.quit()

except Exception as e:
    error(e)
    driver.quit()
