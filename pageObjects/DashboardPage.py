from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.BasePage import BasePage


class DashboardPage(BasePage):

    btn_success_ok_xpath = "//button[normalize-space()='ok']"

    btn_success_continue_xpath = (
        "//button[@onclick='closeModernPopup()']"
    )

    dashboard_header_xpath = "//h2[contains(text(),'Dashboard')]"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_success_ok(self):

        try:

            self.click(
                By.XPATH,
                self.btn_success_ok_xpath
            )

            print("OK popup closed")

        except:

            print("OK popup not displayed")

    def click_success_continue(self):

        try:

            popup_btn = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        self.btn_success_continue_xpath
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                popup_btn
            )

            print("Continue popup closed")

        except:

            print("Continue popup not displayed")

    def is_dashboard_loaded(self):

        return self.is_element_visible(
            By.XPATH,
            self.dashboard_header_xpath
        )

    def wait_for_dashboard(self):

        return self.is_dashboard_loaded()