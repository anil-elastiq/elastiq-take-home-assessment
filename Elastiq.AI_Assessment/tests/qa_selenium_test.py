import os.path
import time

import pytest
from utilities import XLUtils
from Pages.Home_Page import HomePage


def processRowData(data):
    print("Processing Row Data:")
    for index, value in enumerate(data):
        print(f"Column {index + 1}: {value}")


class Test_002_Add_Employee:
    path = "Elastiq.AI_Assessment/testData/Selenium_Playground_testData.xlsx"

    def test_Verify_New_York_Size(self, setup, test_Login):
        self.driver = setup

        self.hp = HomePage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'HomePage')
        self.columns = XLUtils.getColumnCount(self.path, 'HomePage')

        for r in range(2, self.rows + 1):
            data = []
            for c in range(1, self.columns + 1):
                cell_data = XLUtils.readData(self.path, 'HomePage', r, c)
                data.append(cell_data)

            processRowData(data)
            self.hp.enter_office_Name(data[1])
            self.hp.verify_Office_Name()
            self.hp.verify_Result("Showing 1 to 5 of 5 entries (filtered from 24 total entries)")