from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Add_Employee_Page_Class:

    btn_pim_xpath ="/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]/*[name()='svg'][1]"
    btn_add_xpath = "//button[normalize-space()='Add']"
    text_firstname_xpath = "//input[@placeholder='First Name']"
    # text_middlename_xpath = "//input[@placeholder='Middle Name']"
    text_lastname_xpath = "//input[@placeholder='Last Name']"
    text_employee_id_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]"
    btn_save_search_xpath = "//button[@type='submit']"
    text_employee_name_xpath = "//h6[@class='oxd-text oxd-text--h6 --strong']"
    text_employee_record_found_xpath = "//span[normalize-space()='(1) Record Found']"
    text_search_employee_name_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def Click_PIM_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.btn_pim_xpath)))
        self.driver.find_element(By.XPATH, self.btn_pim_xpath).click()

    def Click_Add_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.btn_add_xpath)))
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

    def Enter_Firstname(self,firstname):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_firstname_xpath)))
        self.driver.find_element(By.XPATH, self.text_firstname_xpath).send_keys(firstname)

    # def Enter_Middlename(self,middlename):
    #     self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_middlename_xpath)))
    #     self.driver.find_element(By.XPATH, self.text_middlename_xpath).send_keys(middlename)

    def Enter_Lastname(self,lastname):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_lastname_xpath)))
        self.driver.find_element(By.XPATH, self.text_lastname_xpath).send_keys(lastname)

    def Enter_EmployeeID(self,employeeid):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_employee_id_xpath)))
        emp_id=self.driver.find_element(By.XPATH, self.text_employee_id_xpath).send_keys(employeeid)

    def Click_Save_Search_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.btn_save_search_xpath)))
        self.driver.find_element(By.XPATH, self.btn_save_search_xpath).click()

    def verify_employee_details(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_employee_name_xpath)))
            self.driver.find_element(By.XPATH, self.text_employee_name_xpath)
            return "Employee Details Added Successfully"
        except:
            return "Employee Details Addition Failed"

    def Enter_EmployeeName(self,employeename):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_search_employee_name_xpath)))
        self.driver.find_element(By.XPATH, self.text_search_employee_name_xpath).send_keys(employeename)


    def verify_employee_record_found(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_employee_record_found_xpath)))
            self.driver.find_element(By.XPATH, self.text_employee_record_found_xpath)
            return "Employee Record Found"
        except:
            return "Employee Record Not Found"







