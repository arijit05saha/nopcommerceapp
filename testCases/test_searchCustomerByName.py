from pageObjects.SearchCustomerPage import SearchCuctomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

class Test_004_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerbyName(self, setup):
        self.logger.info("************** Test_004_SearchCustomerByName **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************** Logging Successful **************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.logger.info("************** Nagivated to Search Customer Page Successful **************")

        self.searchCustomerByName = SearchCuctomer(self.driver)

        self.searchCustomerByName.setFirstName("Brenda")
        self.searchCustomerByName.setLastName("Lindgren")
        self.searchCustomerByName.clickSearch()
        status = self.searchCustomerByName.searchCustomerByName("Brenda Lindgren")
        assert True == status

        self.logger.info("************** Search Customer By Name is Successful **************")
        self.driver.close()

