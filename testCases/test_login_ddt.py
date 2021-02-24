import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    dataPath = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************** Test_002_DDT_Login **************")
        self.logger.info("************** Verifying test_login **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.numOfTests = XLUtils.gerRowCount(self.dataPath, "Sheet1")

        test_status_lst = []
        for data in range(2,self.numOfTests+1):
            self.user = XLUtils.readData(self.dataPath, "Sheet1", data, 1)
            self.pwd = XLUtils.readData(self.dataPath, "Sheet1", data, 2)
            self.exp = XLUtils.readData(self.dataPath, "Sheet1", data, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            print("Data %: % %", data, self.user, self.pwd)

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** PASSED ***")
                    test_status_lst.append("Pass")
                    self.lp.clickLogout()
                elif self.exp == "Fail":
                    self.logger.info("*** FAILED ***")
                    test_status_lst.append("Fail")
                    self.lp.clickLogout()
            if act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** FAILED ***")
                    test_status_lst.append("Fail")
                elif self.exp == "Pass":
                    self.logger.info("*** PASSED ***")
                    test_status_lst.append("Pass")


        if "Fail" not in test_status_lst:
            self.logger.info("DDT Test is Pass")
            self.driver.close()
            assert True
        else:
            self.logger.info("DDT Test is Fail")
            self.driver.close()
            assert False

        self.logger.info(" ********** End of Login DDT Test **********")
        self.logger.info(" *************** Completed TC_LoginDDT_002 **************")