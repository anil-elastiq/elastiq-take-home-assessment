# AssessmentSubmission
Elastiq.AI Take Home Assessment - Solution submission

### APPROACH

This script validates the search functionality of the "Table Sort Search Demo" on the Selenium Playground. It performs the following:
1.	Opens the demo webpage using the Chrome browser.
2.	Locates the search box element.
3.	Enters the search term "New York" into the search box.
4.	Counts the visible rows that match the search term dynamically.
5.	Confirms that the search results display exactly 5 rows.
6.	Ensures that the total number of entries remains 24.
The test is implemented using the pytest framework to ensure modularity and robust test execution.



### HOW TO RUN THE SCRIPT

1.	Clone or download this repository.
2.	Ensure Python (3.8 or higher) is installed on your system.
3.	Install dependencies using:
    pip install -r requirements.txt
4.	Save the script as qa_selenium_test.py in the same directory.
5.	Run the test using pytest:
    pytest qa_selenium_test.py
