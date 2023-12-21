
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
        faceWash=driver.find_element(By.XPATH, "(// a[contains(text(), 'Face Wash')])[2]")
        faceWash.click()
        chWind=driver.window_handles[1]
        driver.switch_to.window(chWind)
        print(driver.title)
        lakme = driver.find_element(By.XPATH, "// div[text() = 'Lakme Micellar Pure Facewash For Deep Pore Cleanse']")
        lakme.click()
        thirdWind = driver.window_handles[2]
        driver.switch_to.window(thirdWind)
        bag = driver.find_element(By.XPATH, "(//span[text()='Add to Bag'])[1]")
        bag.click()