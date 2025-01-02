from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def CheckTableSearch():
  
    drm = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=drm)

    try:
        automation_url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
        driver.get(automation_url)

       
        driver.maximize_window()
           
        table_search = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, "//label[text()='Search:']//input"))
        )
        table_search.click()

      
        driver.find_element(By.XPATH, "//label[text()='Search:']//input").send_keys("New York");

        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(By.XPATH, "//tbody//tr")) > 0
        )
         
        row = driver.find_elements(By.XPATH, "//tbody//tr")
        total_row = len(row)

        if total_row == 5:
            print("Search results show 5 entries for 'New York'.")
        else:
            print(f"Expected just 5 entries, but found {total_row}.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
if __name__ == "__main__":
    CheckTableSearch()

