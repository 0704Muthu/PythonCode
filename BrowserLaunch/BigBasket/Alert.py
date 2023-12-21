from selenium import  webdriver
from selenium.webdriver.common.by import By
import  time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, value="alertButton").click()
time.sleep(1)
driver.switch_to.alert.accept()

driver.find_element(By.ID, value="timerAlertButton").click()
# time.sleep(10)
# driver.switch_to.alert.accept()

# Explicit wait
try:
    WebDriverWait(driver,100).until(cond.alert_is_present())
    driver.switch_to.alert.accept()
except (NoAlertPresentException):
    print('No alert present')


