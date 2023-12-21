from selenium import  webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option(name="detach",value=True)
driver=webdriver.Chrome(options)
driver.maximize_window()
driver.get("https://www.amazon.in")
mobile=driver.find_element(By.XPATH,"//a[@href='/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles']")
print(mobile.is_displayed())
print(mobile.text)
mobile.click()

driver.find_element(By.XPATH,"(//span[text()='Samsung'])[2]").click()
allProduct=driver.find_elements(By.XPATH,"//span[@class='a-size-base-plus a-color-base a-text-normal']")
pro="Samsung Galaxy M13 (Aqua Green, 6GB, 128GB Storage) | 6000mAh Battery | Upto 12GB RAM with RAM Plus"
for i in allProduct:
    allText=i.text
    if allText.__eq__(pro):
        i.click()
# driver.quit()

