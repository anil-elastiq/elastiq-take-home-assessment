from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    Search_Box_xpath = "//input[@type='search']"
    Result_xpath = "//div[@id='example_info']"
    Office_tables_xpath = "//td[3]"

    def __init__(self, driver):
        self.driver = driver

    def enter_office_Name(self, office_name):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Search_Box_xpath)))
        element.send_keys(office_name)

    def verify_Office_Name(self):
        Office_Name_List = self.driver.find_elements(By.XPATH, self.Office_tables_xpath)
        Office_Count = len(Office_Name_List)
        print("Office Count =" ,Office_Count)
        if Office_Count == 5:
            assert True
        else:
            assert False

    def verify_Result(self, Result_text):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Result_xpath)))
        Result_text_UI = element.text
        print("Result text UI =" + Result_text_UI)
        if Result_text_UI == Result_text:
            assert True
        else:
            assert False
