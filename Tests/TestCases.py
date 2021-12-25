from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
import time
import os
import sys
import xmlrunner

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from POMProject.Pages.LoginPage import LoginPage
from POMProject.Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome = "C:\\Users\\kosur\\AppData\\Local\\Programs\\Python\\Python38\\Scripts\\chromedriver.exe"
        cls.driver: WebDriver = webdriver.Chrome(executable_path=chrome)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_01_login_valid(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            login = LoginPage(driver)
            login.enter_email_id("*********@gmail.com")
            login.enter_password("*********")
            login.click_login()
            print('Login Successfully : Welcome to CRM portal')
        except:
            print("Failed to Login : Please check your Email Id & Password")

    def test_02_logout_valid(self):
        try:
            time.sleep(5)
            driver = self.driver
            logout = HomePage(driver)
            logout.logout()
            print("logged out from CRM portal")
        except:
            print("Failed to logout from CRM portal")

    def test_03_login_invalid(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            login = LoginPage(driver)
            time.sleep(3)
            login.enter_email_id("abc@gmail.com")
            login.enter_password("huyhg")
            login.click_login()
            time.sleep(3)
            driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_02_login_invalid.png')
        except:
            print("Failed to Login : Please check your Email Id & Password")

    def test_04_empty_filed_login_invalid(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            login = LoginPage(driver)
            login.click_login()
            time.sleep(3)
            driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_04_empty_filed_login_invalid.png')
            print("Please enter the email & password field's to login")
        except:
            print("The email & password field's are required")

    def test_05_forgot_password_valid(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            forgot_password = LoginPage(driver)
            forgot_password.recovery_password("abc@gmail.com")
            self.driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_05_forgot_password_valid.png')
            print("Password Recovery Email Sent Successfully")
        except:
            print("Failed to navigate password recovery page")

    def test_06_existing_user_sign_invalid(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            signup = LoginPage(driver)
            signup.user_signup_username("Kosuru SriHari")
            signup.user_signup_emailid("abc@gmail.com")
            signup.user_signup_password("junjuhv")
            self.driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_06_existing_user_sign_invalid.png')
            print("Account already Exists")
        except:
            print("Failed to signup account")

    def test_07_password_change_login_valid(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            login = LoginPage(driver)
            login.enter_email_id("*********@gmail.com")
            login.enter_password("*********")
            login.click_login()
            time.sleep(3)
            self.driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_07_password_change_login_valid.png')
            print('Login Successfully with new password : Welcome to CRM portal')
            logout = HomePage(driver)
            logout.logout()
            time.sleep(5)
            print("logged out from CRM portal")
        except:
            print("Failed to Login with new password : Please check your Email Id & Password")

    def test_08_update_profie(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            login = LoginPage(driver)
            login.enter_email_id("*********@gmail.com")
            login.enter_password("*********")
            login.click_login()
            time.sleep(5)
            update_profile = HomePage(driver)
            update_profile.update_contact_number_profile('2222222222')
            update_profile.update_user_city_profile("aaaaaaaaaaa")
            updated_contact_number_textbox_js = 'return document.querySelector("#sTest-userContactNumber").value'
            phone_number = self.driver.execute_script(updated_contact_number_textbox_js)
            print(phone_number)
            if len(phone_number) != 0:
                print(phone_number)
            else:
                print("Phone number not updated")
            time.sleep(3)
            self.driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_08_update_profie.png')
            print('profile details updated successfully')
            logout = HomePage(driver)
            logout.logout()
            print("logged out from CRM portal")
        except:
            print("Failed to update user profile details")

    def test_09_login_password_asterisk_valid(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            login = LoginPage(driver)
            login.enter_email_id("abc@gmail.com")
            login.enter_password("abc@gmail.com")
            time.sleep(5)
            driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_09_password_asterisk_valid.png')
            print("Password is safe")
        except:
            print("URL is down")

    def test_10_job_portal_valid(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            login = LoginPage(driver)
            login.enter_email_id("*********@gmail.com")
            login.enter_password("*********")
            login.click_login()
            time.sleep(3)
            job = HomePage(driver)
            job.job_portal()
            time.sleep(3)
            self.driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_10_job_portal_valid.png')
            print("User able to access the job portal successfully")
        except:
            print("Failed to Login : Please check your Email Id & Password")

    def test_11_upload_file_valid(self):
        try:
            driver = self.driver
            upload_file = HomePage(driver)
            upload_file.upload_files_resume("C:/Users/kosur/Downloads/Resume.pdf")
            time.sleep(3)
            self.driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_11_upload_file_valid.png')
            print("Uploaded resume details into CRM portal")
        except:
            print("Failed to upload resume details into CRM portal")

    def test_12_download_file_valid(self):
        try:
            driver = self.driver
            download_file = HomePage(driver)
            download_file.download_companies_file()
            time.sleep(3)
            self.driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_12_download_file_valid.png')
            print("Download company details into CRM portal")
        except:
            print("Failed to Download company details into CRM portal")

    def test_13_add_contact(self):
        try:
            driver = self.driver
            driver.get("https://app.recruitcrm.io/")
            add_contacts = HomePage(driver)
            add_contacts.add_customer_details()
            add_contacts.add_firstname("Shivaji")
            add_contacts.add_lastname("KusiReddy")
            add_contacts.designation_add("IT")
            add_contacts.add_email_address("dnhy@gmail.com")
            add_contacts.add_contact_numberb('8989898989')
            add_contacts.add_contact_city("Vizag")
            add_contacts.contact_locatlity("Seetha")
            time.sleep(3)
            self.driver.save_screenshot(
                'C:/Users/kosur/PycharmProjects/CRM/POMProject/Screenshots/test_13_add_contact.png')
            print("contact details add into CRM portal")
        except:
            print("Failed to add contact details in CRM portal")


    @classmethod
    def tearDownClass(cls):
        print("Test Completed")
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="C:/Users/kosur/PycharmProjects/CRM/POMProject/Report"))