# Waits
#1.implicit wait
# 2.Explicit wait

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MouseAction:

    def implicitWaitConcept(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        driver = webdriver.Chrome(options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        driver.find_element(By.XPATH,value="(//a[@role='button'])[2]").click()
        driver.find_element(By.NAME,"firstname").send_keys('TestCase')

MouseAction().implicitWaitConcept()