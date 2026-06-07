from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage

class DashboardPage(BasePage):
    btn_success_ok_xpath = "//button[normalize-space()='ok']"
    btn_success_continue_xpath = (
        "//div[contains(@class,'modern-popup')]"
        "//button[@onclick='closeModernPopup()']"
    )
    dashboard_header_xpath = "//h2[contains(text(),'Dashboard')]"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_success_ok(self):
        self.click(By.XPATH, self.btn_success_ok_xpath)


    # def handle_post_login_popups(self):

    def click_success_continue(self):

        elements = self.driver.find_elements(
            By.XPATH,
            "//button[normalize-space()='Continue']"
        )

        for element in elements:
            if element.is_displayed():
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )
                break

    def is_dashboard_loaded(self):
        return self.is_element_visible(
            By.XPATH,
            self.dashboard_header_xpath
        )
