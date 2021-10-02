#####################################
#       Code by SochnoeAnime        #
#      github.com/SochnoeAnime      #
#       2021, Nizhny Novgorod       #
#####################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Browser():

    def open_browser():

        opts = Options()
        opts.headless = True
        assert opts.headless
        dweb = webdriver.Chrome(executable_path='chromedriver.exe', options=opts)
        dweb.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131'})
        dweb.get('https://2ch.hk/b/')
        time.sleep(10)

        for i in range(0, 20):
            dweb.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.250)

        print('Browser open')

        return dweb

    def load_threads():

        driver = Browser.open_browser()
        divselements = driver.find_elements_by_xpath('//div[@class="thread"]')
        print(len(divselements))

        return divselements
