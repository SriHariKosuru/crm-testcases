class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_id = "sTestEmail"
        self.password_textbox_id = "sTestPassword"
        self.login_button_id = "sTestLoginBtn"
        self.forgot_password_link_xpath = '//*[@id="sTest-forgotPasswordLink"]/a'
        self.forgot_email_textbox_id = "sTest-emailIdForgotPassTxt"
        self.request_password_button_xpath = "sTest-requestPasswordBtn"
        self.signup_button_id = 'Sign Up'
        self.signup_user_name_textbox_id = "userFirstName"
        self.signup_user_email_textbox_id = "userEmail"
        self.signup_password_textbox_id = "userPassword"
        self.signup_account_button_id = "submitSignUp"


    def enter_email_id(self, email_id):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email_id)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def recovery_password(self, email):
        self.driver.find_element_by_xpath(self.forgot_password_link_xpath).click()
        self.driver.find_element_by_id(self.forgot_email_textbox_id).send_keys(email)
        self.driver.find_element_by_id(self.request_password_button_xpath).click()

    def user_signup_username(self, username):
        self.driver.find_element_by_link_text(self.signup_button_id).click()
        self.driver.find_element_by_id(self.signup_user_name_textbox_id).send_keys(username)

    def user_signup_emailid(self, emailid):
        self.driver.find_element_by_id(self.signup_user_email_textbox_id).send_keys(emailid)

    def user_signup_password(self, s_password):
        self.driver.find_element_by_id(self.signup_password_textbox_id).send_keys(s_password)
        self.driver.find_element_by_id(self.signup_account_button_id).click()
