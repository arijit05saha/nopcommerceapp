from pageObjects.SearchCustomerPage import SearchCuctomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerbyEmail(self, setup):
        self.logger.info("************** Test_004_SearchCustomerByEmail **************")
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

        self.searchCustomerByEmail = SearchCuctomer(self.driver)

        self.searchCustomerByEmail.setEmail("victoria_victoria@nopCommerce.com")
        self.searchCustomerByEmail.clickSearch()
        status = self.searchCustomerByEmail.serachCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status

        self.logger.info("************** Search Customer By Email is Successful **************")
        self.driver.close()

