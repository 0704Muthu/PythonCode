from selenium import  webdriver
from selenium.webdriver.common.by import By
import  time

class MouseAction:

    def rightClick(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        driver = webdriver.Chrome(options)
        driver.maximize_window()
        driver.get("https://www.bigbasket.com/")
        time.sleep(20)
        drop = driver.find_element(By.CSS_SELECTOR, "[href='https://www.bigbasket.com/pc/fruits-vegetables/fresh-vegetables/']")
        drop.click()
        time.sleep(20)
        veg = driver.find_element(By.XPATH, "//h3[text()='Onion (Loose)']")
        veg.click()
MouseAction().rightClick()