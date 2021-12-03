from loginn import senha, login
def google(texto,senha):
    """Digite o texto que será traduzido"""
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    
    from selenium.webdriver.chrome.options import Options
    
    import time
    from random import random
    
    opt = Options()
    opt.headless = True
    
    chrome = webdriver.Chrome(executable_path=r'chromedriver.exe')
    chrome.get("https://educacional.fieg.com.br/")

    rand = lambda:f"{random():.1f}"
    chrome.maximize_window()
    teste = chrome.find_element_by_xpath(r'//*[@id="username"]')
    time.sleep(3)
    for c in texto:
        teste.send_keys(c)
        time.sleep(float(rand()))
    
    tsl = lambda x: time.sleep(x)
    
    sen = chrome.find_element_by_xpath(r'//*[@id="password"]').send_keys(senha)
    time.sleep(1)
    chrome.find_element_by_xpath(r'//*[@id="boxForm"]/div/form/div[3]/button').click()
    time.sleep(5)
    chrome.find_element_by_link_text('Planejamento e Controle da Manutenção').click() #click por link tag <a>
    tsl(2)
    chrome.find_element_by_xpath('//*[@id="onetopictabs"]/ul[1]/li[3]/a/div').click()
    
    time.sleep(10)
    chrome.find_element_by_xpath('//*[@id="dropdown-1"]').click()
    time.sleep(2)
    chrome.find_element_by_xpath('//*[@id="action-menu-1-menu"]/a[7]').click()
    while True:
        time.sleep(10)
        chrome.close()


google(login,senha) #login e senha
