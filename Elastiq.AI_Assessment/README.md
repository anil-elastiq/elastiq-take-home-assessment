Pre-Requisite:
1. Install Pycharm(IDE)
2. Install python
3. Install the following packages:
   1) pytest
   2) pytest-selenium
   3) openpyxl(For reading test data from excel file)

I have used pytest framework and used POM to create my project.
The Structure of my project is like:-

Logs => Pages => Reports => testData => tests => utilities
1. Pages contain the xpath of the elements used in the page and also the functions where those xpaths are used
2. testData contains my excel sheet from where i am reading the testdata.
3. tests contains my main test which will run.
4. utilities contains the code to read the data from excel which is done with the help of openpyxl package.

To run the test, use the following command:-
pytest -v -s Elastiq.AI_Assessment/tests/qa_selenium_test.py