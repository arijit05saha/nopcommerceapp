class SearchCuctomer:

    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstName_xpath = "//input[@id='SearchFirstName']"
    txtLastName_xpath = "//input[@id='SearchLastName']"
    drpDOBMonth_xpath = "//select[@id='SearchMonthOfBirth']"
    drpDOBDay_xpath = "//select[@id='SearchDayOfBirth']"
    txtCompany = "//input[@id='SearchCompany']"
    txtIP_xpath = "//input[@id='SearchIpAddress']"
    txtCustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    btnSearch_xpath = "//button[@id='search-customers']"

    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastName)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def serachCustomerByEmail(self, email):
        found_flg = False
        for row in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            table_email = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr[" + str(row)+"]/td[2]").text
            if table_email == email :
                found_flg = True
                break
        return found_flg

    def searchCustomerByName(self, name):
        found_flag = False
        for row in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            table_name = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr[" + str(row)+"]/td[3]").text
            if table_name == name :
                found_flg = True
                break
        return found_flg

