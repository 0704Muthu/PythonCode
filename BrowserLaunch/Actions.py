import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MouseAction:

    def rightClick(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        driver = webdriver.Chrome(options)
        driver.maximize_window()
        driver.get("https://www.nykaa.com/")
        action=ActionChains(driver)
        drop = driver.find_element(By.XPATH, "(//a[text()='skin'])[2]")
        action.move_to_element(drop).perform()




MouseAction().rightClick()







