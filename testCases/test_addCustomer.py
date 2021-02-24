from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
import pytest

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("************** Test_003_AddCustomer **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************** Logging Successful **************")

        self.logger.info("************** Starting Add Customer Test **************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()

        self.addCust.clickOnAddnew()

        self.logger.info("************** Providing Customer details **************")

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword('test123')
        self.addCust.setFirstName('Arijit')
        self.addCust.setLastName('Saha')
        self.addCust.setCustomerRoles('Guests')
        self.addCust.setManagerOfVendor('Vendor 2')
        self.addCust.setGender('Male')
        self.addCust.setDob('05/08/1987')
        self.addCust.setCompanyName("Arijit's Startup")
        self.addCust.setAdminContent('This is for testing .....')
        self.addCust.clickOnSave()
        self.logger.info("************** Saving Customer details **************")

        self.logger.info("************** Add Customer Validation **************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        if 'customer has been added successfully.' in self.msg:
            self.logger.info(" Customer has been added Successfully")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.driver.close()
            self.logger.error(">>> Add Customer Validation Failed !!!!!!!!!!!")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")




def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

