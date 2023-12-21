from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDown:

    def singleDropDown(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        driver = webdriver.Chrome(options)
        driver.maximize_window()
        driver.get("https://www.amazon.in")
        drop = Select(driver.find_element(By.ID, "searchDropdownBox"))
        # drop.select_by_index(5)
        # drop.select_by_visible_text("Baby")

        #  Find All options length in dropdown
        # listOptions=drop.options
        # print(len(listOptions))

        # Print all  DropDown options using text function
        # for i in listOptions:
        #     print(i.text)

        drop.select_by_index(2)
        myOption = drop.first_selected_option
        print(myOption.text)
    def multipleDropDown(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        driver = webdriver.Chrome(options)
        driver.maximize_window()
        driver.get("https://demoqa.com/select-menu")
        multipleDrop=Select(driver.find_element(By.ID,"cars"))
        multipleDrop.select_by_value("volvo")
        multipleDrop.select_by_visible_text("Saab")

        allOptions = multipleDrop.all_selected_options

        for i in allOptions:
            print(i.text)

        multipleDrop.deselect_all()

        allOptions = multipleDrop.all_selected_options

        for i in allOptions:
            print(i.text)



DropDown().multipleDropDown()
