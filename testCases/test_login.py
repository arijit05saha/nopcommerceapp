import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("************** Test_001_Login **************")

        self.logger.info("************** Verifying test_homePageTitle **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("************** Verifying test_homePageTitle Passed **************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Verifying test_homePageTitle Failed **************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************** Verifying test_login **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************** Login test passed **************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("************** Verifying test_login Failed **************")
            self.driver.close()
            assert False



