from selenium import webdriver
from selenium.webdriver.common.keys import keys

#IMPORTANTE - Referencias podem mudar conforme ocorrem atualizações no dominio do instagram, então é sempre bom verificar se as referências continuam as mesmas

import time

class InstagramBot:
    def_init_(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.chrome(execute_path=r'#caminho do arquivo geckodriver no computador'

    def login(self):
        driver = self.driver
        driver.get('https://www.intagram.com')

        time.sleep(2)

        login_button = driver.find_elemente_by_xpath("//a[@href='/accounts/login/?source-auth_switcher']") #referência html do botão de login
        login_button.click() #depois de referenciado ele vai clicar nesse botão

        user_element = driver.find_elemente_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password.element.send_keys(keys.RETURN)

        time.sleep(2)

        self.curtir_fotos('conteúdo da hashtag que você escolher')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

        time.sleep(2)
        
        for i in range (1, 5): #numero de descidas de pagina
            driver.excute_script("window.scrollTo(0, document.body.scrollHeight):")

        hrefs = driver.find_element_bu_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hastag in href]
        print(hashtag + ' fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.getpic(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight):")
            try:
                driver.find_element_by_class_name('//button[@class="dCJp8 afkep _omzm-]"').click()
                time.sleep(19) #não pode ser menor que esse tempo
            except Exception as e:
                time sleep(5)
        
GabrielBot = InstagramBot('seu_username', 'sua_senha')
GabrielBot.login()
