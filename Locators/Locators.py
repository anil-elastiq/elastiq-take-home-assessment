from selenium.webdriver.common.by import By


class Locator:

    #HomePage Object
    search_box = (By.XPATH, '//*[@id="example_filter"]/label/input')
    rows = (By.XPATH, "//table[@id='example']/tbody/tr")
    words = (By.XPATH, "//*[@id='example_info']")
