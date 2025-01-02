**Selenium Automation Script - Search Functionality Validation**

**Prerequisites**

**Install Python and Pip:** Ensure Python and Pip are installed in your local environment.

**Download Python:** https://www.python.org/downloads/

**Verify installation:**

python --version
pip --version

**Install Dependencies:**

Navigate to Python Interpreter > Interpreter settings

Click Add Interpreter 

Search for Selenium ,Pytest and Web driver-manager individually.

Add these packages

**Project Setup**

Create a New Project:

Open PyCharm IDE.

Create a new Python project.

**Folder Structure:**

Create the following folders inside your project:

**Locators:** Store locator classes.

**Pages:** Store page object classes.

**Tests:** Store test scripts.

**Implementation Details**

**Locators:**
Define a class under the Locators folder to store web element locators.

**Pages:**

Create a Home Page class under the Pages folder.

**Test Script:**

Write the test script under the Tests folder to validate search functionality.

**Execution**

Run the script using the following pytest command:

pytest Tests/test_search_functionality.py

**Script Functionality**

Navigate to the Selenium Playground website.

Perform a search operation by filtering the keyword 'New York'.

Verify that 5 entries are displayed out of 24 total entries.

**Expected Output**

The script should validate that the filtering operation displays exactly 5 entries related to 'New York' and confirm the total count of 24 entries.

