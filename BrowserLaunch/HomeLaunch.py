
from selenium import  webdriver
options=webdriver.ChromeOptions()
options.add_experimental_option(name="detach",value=True)
driver=webdriver.Chrome(options)
driver.get("https://www.amazon.in")
driver.maximize_window()
getTitle=driver.title
print(getTitle)
getCurrentUrl=driver.current_url
print(getCurrentUrl)




