import time

import allure
from faker import Faker
import pytest
from Utilities.logger import Logger_class
from Utilities.readConfig import ReadConfig
from pageObjects.Add_Employee_Page import Add_Employee_Page_Class
from pageObjects.Login_Page import Login_Page_Class

@pytest.mark.usefixtures("driver_setup")
class Test_Add_Employee:
    driver = None
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    login_url = ReadConfig.get_login_url()
    log = Logger_class.get_logger()

    def test_add_employee_006(self):
        self.log.info("Starting Test: Verify Add Employee Functionality")
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page Loaded")
        lp = Login_Page_Class(self.driver)
        self.log.info("Entering Username and Password")
        lp.Enter_Username(self.username)
        lp.Enter_Password(self.password)
        self.log.info("Clicking Login Button")
        lp.Click_Login()
        self.log.info("Login Attempt Completed")
        ae = Add_Employee_Page_Class(self.driver)
        self.log.info("Clicking PIM Button")
        time.sleep(10)
        ae.Click_PIM_Button()
        self.log.info("Clicking Add Button")
        time.sleep(5)
        ae.Click_Add_Button()
        time.sleep(5)
        self.log.info("Entering Employee Details")
        fake_firstname = Faker().first_name()
        fake_lastname = Faker().last_name()
        fake_employee_id = Faker().random_int(min=1000, max=9999)

        ae.Enter_Firstname(fake_firstname)
        ae.Enter_Lastname(fake_lastname)
        time.sleep(5)
        ae.Enter_EmployeeID(fake_employee_id)

        self.log.info("Clicking Save Button")
        ae.Click_Save_Search_Button()
        self.log.info("Employee Added Successfully")
        time.sleep(5)
        if ae.verify_employee_details() == "Employee Details Added Successfully":
            self.log.info("Employee Details Verified")
            self.driver.save_screenshot("Screenshots\\test_add_employee_pass.png")
            self.log.info("Screenshot saved")
            allure.attach.file(".\\Screenshots\\test_add_employee_pass.png", name="test_add_employee_pass",
                               attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.error("Employee Details Verification Failed")
            self.driver.save_screenshot("Screenshots\\test_add_employee_fail.png")
            self.log.info("Screenshot saved")
            allure.attach.file(".\\Screenshots\\test_add_employee_fail.png", name="test_add_employee_fail",
                               attachment_type=allure.attachment_type.PNG)
            assert False

        time.sleep(5)
        self.log.info("Clicking PIM Button")
        ae.Click_PIM_Button()
        time.sleep(5)
        self.log.info("Entering Employee name")
        ae.Enter_EmployeeName(fake_firstname+" "+fake_lastname)
        time.sleep(5)
        self.log.info("Clicking Search Button")
        ae.Click_Save_Search_Button()
        self.log.info("Employee Record Found")
        time.sleep(5)
        if ae.verify_employee_record_found() == "Employee Record Found":
            self.log.info("Employee Record Verified")
            self.driver.save_screenshot("Screenshots\\test_add_employee_record_found_pass.png")
            allure.attach.file(".\\Screenshots\\test_add_employee_record_found_pass.png", name="test_add_employee_record_found_pass",
                               attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.error("Employee Record Verification Failed")
            self.driver.save_screenshot("Screenshots\\test_add_employee_record_found_fail.png")
            allure.attach.file(".\\Screenshots\\test_add_employee_record_found_fail.png", name="test_add_employee_record_found_fail",
                               attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("test_add_employee_006 test Completed")
        self.log.info("=============================================================")

















