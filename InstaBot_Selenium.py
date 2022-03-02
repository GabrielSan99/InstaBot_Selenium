#https://github.com/bjcarlson42/youtube

from time import sleep
from selenium import webdriver

class Bot():
    
    links = []

    comments = [
        'You are great!', 'Awesome!'
    ]

    def __init__(self):
        
        username = input("Type your username: ")
        password = input("Type your password: ")

        self.login(username, password)

        self.like_comment_by_hashtag('bodybuilding')     #choose the theme for your likes

    def login(self, username, password):
    
    #to work on linux:
    #sudo apt-get install chromium-chromedriver
    #move chromedriver to /usr/lib/chromium-browser/ and execute self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    #to work on windows:
    #self.driver = webdriver.chrome(execute_path=r'/path/to/chromedriver.exe')
        
        self.driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
        self.driver.get('https://instagram.com/')
        sleep(3)

        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)

        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(2)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(3)
        
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        except:
            pass
        
        sleep(3)

        try:
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        except:
            pass

        sleep(2)

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        sleep(1)
        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')

        valid_links = list(filter(condition, links))

        imgs_to_like = 5

        for i in range(imgs_to_like):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            
            # like
            sleep(5)
            self.driver.find_element_by_class_name('fr66n').click()
            sleep(19)


            # # comment
            # self.driver.find_element_by_class_name('RxpZH').click() 
            # sleep(1)
            # self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
            # sleep(1)
            # self.driver.find_element_by_xpath("//button[@type='submit']").click()


    

def main():
    while True:
        my_bot = Bot()
        sleep(60)       #wait 1 minute to run the bot again

if __name__ == '__main__':
    main()
