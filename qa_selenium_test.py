from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def SearchTableValidation():
    """
    This is a method to the Selenium
    """
    #have setup the chromedriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # URL search
        playground_url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
        driver.get(playground_url)

        # Maximize browser window
        driver.maximize_window()

        # Wait for the Table Search  is visible 
        table_search_link = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((By.XPATH, "//label[text()='Search:']//input"))
        )
        table_search_link.click()

        # Locating the search box and enter "New York"
        driver.find_element(By.XPATH, "//label[text()='Search:']//input").send_keys("New York");
        
        # Wait for the results to load 
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(By.XPATH, "//tbody//tr")) > 0
        )

        # Validate the search results
        rows = driver.find_elements(By.XPATH, "//tbody//tr")
        total_rows = len(rows)

        if total_rows == 5:
            print("Search results show 5 entries for 'New York'.")
        else:
            print(f"Expected just 5 entries, but found {total_rows}.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Closing the browser
        driver.quit()

if __name__ == "__main__":
    SearchTableValidation()
