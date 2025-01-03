Approach

1. 	Imports: 	
		The script imports some modules from pytest and selenium

2.	Locators Class:	
		This class contains locators for elements on the webpage. 

3.	Fixture setup_and_teardown:	
	3.1	 Initializes a Chrome WebDriver
	3.2	 Maximizes the browser
	3.3	 Yields the driver to the test function and quits the driver after the test is complete.	

4.	Test Function test_search_functionality:
	4.1	It navigates to a specified URL.
	4.2	Finds the search box element and inputs the search text "New York".
	4.3	Uses an explicit wait to ensure that the expected text appears in the INFO_TEXT element.
	4.4	Asserts that the search results show "Showing 1 to 5 of 5 entries", validating the search functionality.


How to Run the Code

1.	Install Dependencies
		1.1 	Install python
		1.2	Install pip
		1.3	Install pytest selenium using command "pip install pytest selenium"

2.	Download ChromeDriver:
		2.1 Check the version of Chrome in you system and install the compatible ChromeDriver from url : https://googlechromelabs.github.io/chrome-for-testing/#stable
		2.2 After Downloading the ChromeDriver Extract the file and Then move the "chromedriver.exe" to project file "../../elastiq-take-home-assessment".


3.	Execution:
		3.1 For Execution of script open "CMD" 
		3.2 navigate to project folder by using command
			cd 'C:\Users\..\..\elastiq-take-home-assessment\' (Please change as per you folder structure)
		3.3 Run the below command to execute the testcase.
			pytest qa_selenium_test.py