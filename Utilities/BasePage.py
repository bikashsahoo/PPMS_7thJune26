# This way, all find_element(), waits, clicks, and text entry remain inside BasePage, and
# your Page Objects contain only business actions
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, by, locator):
        self. wait.until(EC.element_to_be_clickable((by, locator))).click()

    def enter_text(self, by, locator, value):
        self.driver.find_element(by, locator).clear()
        self.wait.until(EC.visibility_of_element_located((by, locator))).send_keys(value)

    def get_text(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator))).text


    def click_visible_element(self, by, locator):

        elements = self.driver.find_elements(by, locator)

        for element in elements:
            if element.is_displayed() and element.is_enabled():
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    element
                )

                return

        raise Exception(
            f"No visible element found for locator: {locator}"
        )



    def scroll_to_element(self, by, locator):
        element = self.wait.until(
            EC.presence_of_element_located((by, locator))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        return element



    def is_element_visible(self, by, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

