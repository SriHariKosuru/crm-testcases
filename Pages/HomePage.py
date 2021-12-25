import time


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.user_click_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/nav[1]/div[2]/div[4]/div[5]/div[" \
                                "1]/a[1]/img[1] "
        self.logout_click_id = "sTest-signOutInAppBtn"
        self.user_button_xpath = '//*[@id="sTest-dpLinkInAppBtn"]/img'
        self.user_profile_button_xpath = '//*[@id="sTest-profileInAppBtn"]'
        self.contact_number_textbox_xpath = '//*[@id="sTest-userContactNumber"]'
        self.city_textbox_xpath = '//*[@id="sTest-userCity"]'
        self.save_profile_button_xpath = '//*[@id="sTest-btnSaveProfile"]'
        self.job_portal_button_xpath = '//*[@id="sidebar"]/nav/ul[1]/li[5]/a'
        self.portal_sidebar_button_xpath = '//*[@id="sidebar"]/nav/ul[1]/li[2]/a'
        self.portal_resume_button_css = "#sTest-resumeParserBtn"
        self.portal_file_upload_button_id = "sTest-uploadFilesForResumeParser"
        self.assign_to_candidate = 'sTest-candidateDAssignJobsBtn'
        self.resume_checkbox_xpath = '//body/div[108]/div[2]/form[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/label[1]/span[1]'
        self.final_assign_button_id = 'sTest-assignJobsBtn'
        self.companies_icon_button_xpath = '//*[@id="sTest-companiesIcon"]'
        self.companies_download_dropdown_button_xpath = "//thead/tr[1]/th[1]/label[1]/span[1]"
        self.companies_download_button_xpath = '//*[@id="sTest-exportToCSVButton"]'
        self.companies_checkbox_xpath = '//body/div[34]/div[2]/div[1]/div[1]/section[1]/label[1]/span[1]'
        self.companies_export_button_id = "sTest-exportToCsvPopUpBtn"

        self.add_contacts_textbox_xpath = '//*[@id="sTest-contactsIcon"]'
        self.text_expand_xpath = "//i[@id='sTest-expandIcon']"
        self.contact_add_textbox_id = 'sTest-addContactBtn'
        self.first_name_textbox_id = 'sTest-contactFirstnameTxt'
        self.last_name_textbox_id = 'sTest-contactLastnameTxt'
        self.designation_textbox_id = 'sTest-contactDesignationTxt'
        self.email_textbox_id = 'sTest-contactEmailTxt'
        self.contact_number_tbox_id = 'sTest-contactContactnumberTxt'
        self.contact_city_textbox_id = 'sTest-contactCityTxt'
        self.contact_locality_textbox_id = 'sTest-contactLocalityTxt'
        self.contact_add_button_id = 'sTest-contactAddBtn'

    def logout(self):
        self.driver.find_element_by_xpath(self.user_click_xpath).click()
        self.driver.find_element_by_id(self.logout_click_id).click()

    def update_contact_number_profile(self, contact):
        self.driver.find_element_by_xpath(self.user_button_xpath).click()
        self.driver.find_element_by_xpath(self.user_profile_button_xpath).click()
        self.driver.find_element_by_xpath(self.contact_number_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.contact_number_textbox_xpath).send_keys(contact)

    def update_user_city_profile(self, city):
        self.driver.find_element_by_xpath(self.city_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.city_textbox_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.save_profile_button_xpath).click()

    def job_portal(self):
        self.driver.find_element_by_xpath(self.job_portal_button_xpath).click()

    def upload_files_resume(self, path):
        self.driver.find_element_by_xpath(self.portal_sidebar_button_xpath).click()
        self.driver.find_element_by_css_selector(self.portal_resume_button_css).click()
        self.driver.find_element_by_id(self.portal_file_upload_button_id).send_keys(path)
        time.sleep(8)
        self.driver.find_element_by_id(self.assign_to_candidate).click()
        self.driver.find_element_by_xpath(self.resume_checkbox_xpath).click()
        self.driver.find_element_by_id(self.final_assign_button_id).click()

    def download_companies_file(self):
        self.driver.find_element_by_xpath(self.companies_icon_button_xpath).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.companies_download_dropdown_button_xpath).click()
        self.driver.find_element_by_xpath(self.companies_download_button_xpath).click()
        self.driver.find_element_by_xpath(self.companies_checkbox_xpath).click()
        self.driver.find_element_by_id(self.companies_export_button_id).click()

    def add_customer_details(self):
        self.driver.find_element_by_xpath(self.add_contacts_textbox_xpath).click()
        self.driver.find_element_by_xpath(self.text_expand_xpath).click()
        self.driver.find_element_by_id(self.contact_add_textbox_id).click()

    def add_firstname(self, name):
        self.driver.find_element_by_id(self.first_name_textbox_id).send_keys(name)

    def add_lastname(self, last_name):
        self.driver.find_element_by_id(self.last_name_textbox_id).send_keys(last_name)

    def designation_add(self, designation):
        self.driver.find_element_by_id(self.designation_textbox_id).send_keys(designation)

    def add_email_address(self, email_add):
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email_add)

    def add_contact_numberb(self, con):
        self.driver.find_element_by_id(self.contact_number_tbox_id).send_keys(con)

    def add_contact_city(self, place):
        self.driver.find_element_by_id(self.contact_city_textbox_id).send_keys(place)

    def contact_locatlity(self, locality):
        self.driver.find_element_by_id(self.contact_locality_textbox_id).send_keys(locality)
        self.driver.find_element_by_id(self.contact_add_button_id).click()
