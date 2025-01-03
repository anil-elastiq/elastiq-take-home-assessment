# Selenium Search Functionality Validation

## Objective
This project automates the validation of search functionality on the Selenium Playground website.

## Deliverables
1. A Python script (`qa_selenium_test.py`) that:
   - Navigates to the Selenium Playground "Table Sort and Search Demo" page.
   - Searches for "New York" in the search box.
   - Validates that the search results display 5 entries out of 24 total entries.

---

## Prerequisites
Ensure you have the following installed on your system:

1. Python (version 3.8 or higher)
2. Google Chrome (latest version)
3. pip (Python package manager)

---

## Setup Instructions

1. **Clone or Download the Repository**
   Download the script (`qa_selenium_test.py`) and save it in a desired directory.

2. **Install Dependencies**
   Install the required Python libraries by running the following command:
   ```bash
   pip install pytest selenium webdriver-manager
   ```

3. **Execute the Script**
   Navigate to the directory containing the script and run the following command:
   ```bash
   pytest -v qa_selenium_test.py
   ```

---

## Approach

1. **Setup WebDriver**:
   - The script uses the `webdriver-manager` package to manage the ChromeDriver installation, ensuring compatibility with the latest Chrome browser version.

2. **Navigation**:
   - The script navigates to the "Table Sort and Search Demo" page on the Selenium Playground.

3. **Search Operation**:
   - The search term "New York" is entered in the search box.

4. **Validation**:
   - Asserts that exactly 5 rows are displayed in the search results.
   - Asserts that the total number of entries remains 24.

5. **Browser Compatibility**:
   - Default configuration is for Chrome, but other browsers (e.g., Firefox) can be configured by modifying the script.

---

## Code Quality
The script adheres to the following principles:

- Follows PEP8 coding standards.
- Uses Python's `pytest` framework for structured and modular testing.
- Includes assertion statements to validate functionality.

---

## Troubleshooting

1. **Environment Issues**:
   - Ensure Python and Chrome are correctly installed and added to the system PATH.

2. **Driver Compatibility**:
   - Use `webdriver-manager` to avoid manual driver updates.

3. **Test Failures**:
   - Check for potential UI changes on the Selenium Playground website that might affect element locators.

---

## Support
For any issues, please contact navedmd700@gmail.com
