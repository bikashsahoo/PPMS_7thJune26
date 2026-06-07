# ref img_002

import pytest
from Configurations.readProperties import readProperties
from pageObjects.LoginPage import Login
from pageObjects.DashboardPage import DashboardPage

"""Configurations // readProperties // readProperties"""
class Test_Login:
    base_url = readProperties.getURL()
    username = readProperties.getUsername()
    password = readProperties.getPassword()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self, setup):
        self.driver = setup

        self.driver.get(self.base_url)
        self.driver.maximize_window()

        login = Login(self.driver)

        login.click_login_menu()
        login.select_password_login()

        login.enter_username(self.username)
        login.enter_password(self.password)

        login.click_login_button()

        dashboard = DashboardPage(self.driver)

        dashboard.click_success_ok()
        self.driver.save_screenshot(".\\screenshots\\"+"continue_page.png")
        dashboard.click_success_continue()

        assert dashboard.is_dashboard_loaded()



