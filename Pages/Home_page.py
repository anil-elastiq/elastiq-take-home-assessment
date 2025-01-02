from Locators.Locators import Locator


class Homepage:

    def __init__(self,driver):
        self.driver=driver


    def open_page(self, url):
        self.driver.get(url)

    def search_value(self, value):
        self.driver.find_element(*Locator.search_box).send_keys(value)

    def filter_rows(self):
        rows=self.driver.find_elements(*Locator.rows)
        visible_rows = [row for row in rows if row.is_displayed()]
        return visible_rows

    def result_words(self):
        words=self.driver.find_element(*Locator.words)
        return words