import logging
from selenium.webdriver.common.by import By


def enter_text_into_search_box(driver, input_text):   # search action
    search_box = driver.find_element(By.XPATH, "//input[@type='search']")
    search_box.clear()
    search_box.send_keys(input_text)


search_text = "New York"    # search string


# Test Cases
def test_search_result_text(setup_and_teardown):
    driver = setup_and_teardown
    logging.info("test_search_result_text started...")
    
    # Perform search
    enter_text_into_search_box(driver, search_text)

    # Validate the search result text
    actual_text = driver.find_element(By.XPATH, "//div[@role='status']").text
    expected_text = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"
    assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
    logging.info("test_search_result_text completed...")


def test_search_result_table(setup_and_teardown):
    driver = setup_and_teardown
    logging.info("test_search_result_table started...")
    
    # Perform search
    enter_text_into_search_box(driver, search_text)

    # validate rows having searched text in table
    actual_count = len(driver.find_elements(By.XPATH,
                                            f"//thead/following-sibling::tbody/tr/td[text()='{search_text}']"))
    expected_count = 5
    assert actual_count == expected_count, f"Expected rows '{expected_count}', but got '{actual_count}'"
    logging.info("test_search_result_table completed...")
    