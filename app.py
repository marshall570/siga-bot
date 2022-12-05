import os
from plyer import notification
from logging import error
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

try:
    # CARREGAR INFO DO ALUNO COM O .ENV
    load_dotenv()
    user = os.getenv('USER-LOGIN')
    pswd = os.getenv('USER-PSWD')

    grades = ''
    
    # SELECTORS NECESSÁRIOS
    user_input = '#vSIS_USUARIOID'
    pswd_input = '#vSIS_USUARIOSENHA'
    login_button = '.Button'
    span_notas = '#ygtvlabelel10Span'

    # CRIAR WEBDRIVER FIREFOX
    firefox_options = FirefoxOptions()
    firefox_options.headless = True
    driver = webdriver.Firefox(options=firefox_options)
    
    # CRIAR WEBDRIVER CHROME
    # chrome_options = ChromeOptions()
    # chrome_options.headless = True
    # driver = webdriver.Chrome(options=chrome_options)
    
    driver.implicitly_wait(2)
    
    notification.notify(
        app_name = 'SIGA',
        title = 'EXECUTANDO',
        message =  'Logando no sistema...',
        timeout = 3
    )

    # OBTER NOTAS
    driver.get('https://siga.cps.sp.gov.br/aluno/login.aspx')

    driver.find_element(By.CSS_SELECTOR, user_input).send_keys(user)
    driver.find_element(By.CSS_SELECTOR, pswd_input).send_keys(pswd)
    driver.find_element(By.CSS_SELECTOR, login_button).click()

    driver.find_element(By.CSS_SELECTOR, span_notas).click()

    
    for i in range(1, 10):
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

        # print(f'{nota} - {nome}')
        grades += f'{nota} - {nome}\n'

    notification.notify(
        app_name = 'SIGA',
        title = 'NOTAS ATUAIS',
        message =  grades,
        timeout = 10
    )

    driver.quit()

except Exception as e:
    notification.notify(
        app_name = 'SIGA',
        title = 'ERRO',
        message = e,
        timeout = 10
    )
