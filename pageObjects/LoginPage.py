from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage

# Because class Login(BasePage): means Login inherits all methods and properties from BasePage.
class Login(BasePage):
    login_menu_link = "Login"
    using_password_tab_xpath = "//a[normalize-space()='Using Password']"
    using_otp_tab_xpath = "//a[normalize-space()='Using OTP']"
    textbox_username_id = "username"
    textbox_password_xpath = "//input[@placeholder='Password']"
    textbox_otp_xpath = "//input[@placeholder='Enter OTP']"
    login_button_xpath = "//button[normalize-space()='Login']"
    getotp_button_xpath = "//button[normalize-space()='Get OTP']"



# Refer image on system : img_001 (harry_python/selenium/ppms_automation/img_001)
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

# Because Login inherited the click() method from BasePage. i.e self.click()
    def click_login_menu(self):
        self.click(By.LINK_TEXT, self.login_menu_link)
        # here i pass 2 parameter to click method by & locator

    def select_password_login(self):
        self.click(By.XPATH, self.using_password_tab_xpath)

    def enter_username(self, username):
        self.enter_text(By.ID, self.textbox_username_id, username)
        # how can i fetch these username and password and otp from ini file

    def enter_password(self, password):
        self.enter_text(By.XPATH, self.textbox_password_xpath, password)

    def enter_otp(self, otp):
        self.enter_text(By.XPATH, self.textbox_otp_xpath, otp)

    def select_otp_login(self):
        self.click(By.XPATH, self.using_otp_tab_xpath)

    def click_get_otp(self):
        self.click(By.XPATH, self.getotp_button_xpath)

    def click_login_button(self):
        self.click(By.XPATH, self.login_button_xpath)






