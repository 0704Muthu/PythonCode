from selenium import  webdriver
from selenium.webdriver.common.by import By
import  time

class webTable:

    def table(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        driver = webdriver.Chrome(options)
        driver.maximize_window()
        driver.get("https://www.worldometers.info/coronavirus/")
        # getHeader=driver.find_element(By.XPATH,"(//table)[1]//thead").text
        # print(getHeader)
        getRow = driver.find_element(By.XPATH, "(//div[@class='maincounter-number'])[1]").text
        print(getRow)

webTable().table()


