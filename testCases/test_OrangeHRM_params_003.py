import time
import allure
import pytest

from Utilities.logger import Logger_class
from Utilities.readConfig import ReadConfig
from testCases.conftest import orangeHRM_login_data
from pageObjects.Login_Page import Login_Page_Class

@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Params_004:
    driver = None
    login_url = ReadConfig.get_login_url()
    log = Logger_class.get_logger()

    def test_OrangeHRM_Login_Param_005(self, orangeHRM_login_data):
        self.log.info("Starting Test: Verify OrangeHRM Login Functionality")
        self.log.info("Navigating to OrangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page Loaded")


        username = orangeHRM_login_data[0]
        password = orangeHRM_login_data[1]
        expected_result = orangeHRM_login_data[2]

        print(f"username: {username}")
        print(f"password: {password}")
        print(f"expected_result: {expected_result}")
        time.sleep(5)
        lp = Login_Page_Class(self.driver)

        self.log.info("Entering Username and Password")

        lp.Enter_Username(username)
        lp.Enter_Password(password)
        self.log.info("Clicking Login Button")

        lp.Click_Login()
        time.sleep(5)
        if lp.verify_login() == "Login Successful":
            self.log.info(f"Login Successful for Username={username}")

            self.driver.save_screenshot("Screenshots\\test_OrangeHRM_Login_Param_005_pass.png")
            self.log.info("Screenshot of Passed Test Saved")
            allure.attach.file(".\\Screenshots\\test_OrangeHRM_Login_Param_005_pass.png", name="test_OrangeHRM_Login_Param_005_pass",
                               attachment_type=allure.attachment_type.PNG)
            self.log.info("Clicking Menu Button")
            time.sleep(5)
            lp.Click_Menu()
            self.log.info("Clicking Logout Button")
            time.sleep(5)
            lp.Click_Logout()
            self.log.info("Logout Successful")
            actual_result = 'Login Pass'
            assert True
        else:
            self.log.info("Login Failed")
            actual_result = 'Login Fail'
            self.log.info("Screenshot of Failed Test Saved")
            self.driver.save_screenshot("Screenshots\\test_OrangeHRM_Login_Param_005_fail.png")
            allure.attach.file(".\\Screenshots\\test_OrangeHRM_Login_Param_005_fail.png", name="test_OrangeHRM_Login_Param_005_fail",
                               attachment_type=allure.attachment_type.PNG)
            assert False

        self.log.info("Actual Result: " + actual_result)
        self.log.info("Expected Result: " + expected_result)
        if actual_result == expected_result :

            print("Testcase Pass")
            assert True
        else:

            print("Testcase Fail")
            assert False

