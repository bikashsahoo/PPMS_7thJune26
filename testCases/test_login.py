# ref img_002
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configurations.readProperties import readProperties
from pageObjects.LoginPage import Login
from pageObjects.DashboardPage import DashboardPage
from Utilities.customLogger import LogGen # Utilities{Package}, customLogger{module}, LogGen {class name}
"""Configurations // readProperties // readProperties"""
class Test_Login:
    base_url = readProperties.getURL()
    username = readProperties.getUsername()
    password = readProperties.getPassword()
    logger = LogGen.loggen() # from utility file i call the log feature by class and method name it will return a logger object
    #as we crt the logger variable in class level so we can call by self keyword

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_HomePageTitle(self, setup):
        self.logger.info("******************* Test_Login **************************")
        self.logger.info("******************* Verifying HomePage Title **************************")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title
        if act_title == "PPMS || Home":
            assert True
            # self.driver.close()
            self.logger.info("************ Home Page Title Test is Passed ************")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "continue_page0.png")
            self.driver.close()
            self.logger.warning("************ Home Page Title Test is Failed ************")
            assert False

    def test_valid_login(self, setup):
        self.logger.info("************* Verifying the Login Test ***************")
        self.driver = setup
        self.driver.get(self.base_url)
        # self.driver.maximize_window()

        self.driver.set_window_size(1366, 768)
        self.driver.execute_script("document.body.style.zoom='70%'")

        login = Login(self.driver)
        login.click_login_menu()
        login.select_password_login()
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login_button()

        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.title != "PPMS || Sign In"
        )

        act_title_dashboard = self.driver.title
        print("Dashboard Title =", act_title_dashboard)
        if act_title_dashboard == "PPMS || Dashboard":
            self.logger.info("*************** Login Test is Passed ********************")
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\continue_page1.png")
            self.logger.error("Login Test is Failed")
            assert False

        dashboard = DashboardPage(self.driver)
        dashboard.click_success_ok()


        self.driver.save_screenshot(".\\screenshots\\"+"continue_page2.png")
        dashboard.click_success_continue()

        assert dashboard.is_dashboard_loaded()

        self.driver.quit()

