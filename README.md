# Selenium Automation Assessment
**Submitted by:** Ashithosh K S
## Objective
This project involves creating a Selenium automation script in Python to validate the search functionality on the Selenium Playground website.

---

## Project Structure
The project contains the following files:
- **`qa_selenium_test.py`**: Main Python script containing test cases.
- **`conftest.py`**: pytest setup file having setup & teardown, logs features
- **`requirements.txt`**: Dependencies for the project.
- **`README.md`**: Documentation (this file).

---

## Approach

### Test Cases
1. **Test Case 1: Validate Search Result Text**
   - Navigates to the Selenium Playground Table Search Demo.
   - Searches for the term "New York."
   - Validates that the result text is: `Showing 1 to 5 of 5 entries (filtered from 24 total entries).`

2. **Test Case 2: Validate Rows in the Table**
   - Searches for the term "New York."
   - Validates that exactly **5 rows** in the table contain "New York."

### Code Highlights
- The `setup_and_teardown` fixture dynamically supports different browsers (`Chrome`, `Firefox`, `Edge`) and modes (`headless` and `non_headless`).
- The tests are written using the `pytest` framework for modularity and scalability.

---

## Prerequisites
Ensure the following are installed:
1. **Python 3.10+**
2. **pip** (Python package manager)

---

## Installation and Setup

### Step 1: Download the Code
You can download the files directly from the pull request or the provided repository branch.

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Tests
Run the tests using `pytest`:
```bash
pytest -v qa_selenium_test.py
```

To run in **headless mode** or with a different browser, modify the `setup_and_teardown` fixture in `qa_selenium_test.py`.

Check generated log file in logs folder.


---

## Best Practices Followed
1. **PEP8 Compliance**: The script adheres to Python coding standards.
2. **Reusable Functions**: Key interactions (e.g., search box input) are modularized.
3. **Robust Assertions**:
   - Validates both the result text and the table row count.
4. **Browser Compatibility**: Supports Chrome, Firefox, and Edge browsers.
5. **Headless Mode**: Allows tests to run without GUI for CI/CD environments.
6. **Logs**: logs setup is done using conftest.py for debugging process.

---

## Notes
- Tested on the latest versions of Chrome, Firefox, and Edge.
- Ensure internet access for downloading browser drivers via `webdriver-manager.`

---

## Dependencies
The project uses the following libraries:

- `selenium==4.27.1`
- `pytest==8.3.4`
- `webdriver-manager==4.0.2`

These are listed in the `requirements.txt` file.

---

## Contact
For any issues or queries, feel free to reach out.

Thank you for reviewing my submission!
