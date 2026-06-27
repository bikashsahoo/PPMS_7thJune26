# 1. Class Creation
# 2. Method / Test Scenario Creation
# 3. SetUp to open the URL and website
# 4. Login
# 5. Dashboard Popup Handling
# 6. Project Creation Navigation
# 7. Close popup if it appears again
# 8. Verification
# 9. Close

# 1. Class Creation
#       (i) URL(base_url) set from config.ini & readProperties.py
#      (ii) Username set from config.ini & readProperties.py
#     (iii) Password set from config.ini & readProperties.py
#      (iv) Creation of Method / Test Scenario carry parameter called from "testCases=>conftest.py" carry browser(chrome/edge/firefox) or The setup parameter is a pytest fixture.=>Pytest automatically looks for a fixture named setup in conftest.py and injects the browser object.
#       (v) create a driver object inside the test method for all method by help of parameter setup == browser == chrome/firefox/edge or Receive the WebDriver instance from the fixture and assign it to the current object.
#       (iv) create a logger object inside class variable from "Utilities=>customLogger" ==> class "LogGen" method "loggen"
#        (v) Class Variables=>base_url, username, password

# 2. Method / Test Scenario Creation(logger,login, self.driver, dashboard, project object)
#       (i) Receive Driver from testCases=>conftest.py i.e "self.driver = setup"
#      (ii) Set Logger from Utilities=>customLogger  ==> logger = LogGen.loggen()
#     (iii) Set URL open the website in browser and set the screensize by the help of "get" and "maximize" access the class variable base_url(1.[i])
#      (iv) Login functionality and maintain logger file from LoginPage object(pageObjects=>LoginPage) create login driver to control the login functionality
#       (v) Dashboard Popup Handling create a dashboard object variable to control the pop up from "pageObjects=>dashboardPage.py"
#      (vi) Project Creation Navigation for this we crt object "project" from "pageObjects=>ProjectCreation3lakhPage.py" to control the menu->subMenu->AddProjects
#     (vii) Close popup if it appears again same as point (v)
#    (viii) Close all browser windows using the driver instance. => self.driver.quit() => is using an instance variable.
#      (ix) @pytest.mark.sanity, @pytest.mark.regression => Test case belongs to: Sanity Suite and Regression Suite

import pytest
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.DashboardPage import DashboardPage
from pageObjects.LoginPage import Login
from pageObjects.ProjectCreation3lakhPage import ProjectCreationPage_3lakh

from Configurations.readProperties import readProperties
from Utilities.customLogger import LogGen


class Test_ProjectCreation3Lakh:

    base_url = readProperties.getURL()
    username = readProperties.getUsername()
    password = readProperties.getPassword()

    logger = LogGen.loggen()

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_add_project_page_title(self, setup):   # 1st execute

        self.driver = setup

        self.logger.info(
            "******** Test Project Creation Started ********"
        )

        self.driver.get(self.base_url)
        # self.driver.maximize_window()
        # self.driver.get(self.base_url)

        self.driver.set_window_size(1366, 768)

        self.driver.execute_script(
            "document.body.style.zoom='70%'"
        )

        # Login
        login = Login(self.driver)

        login.click_login_menu()
        login.select_password_login()
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login_button()

        self.logger.info("Login Successful")

        # Dashboard Popup Handling
        dashboard = DashboardPage(self.driver)

        dashboard.click_success_ok()
        dashboard.click_success_continue()

        assert dashboard.wait_for_dashboard()

        self.logger.info(
            "Dashboard Loaded Successfully"
        )
# -------------------------------Navigation section-----------------------------------------
#  project = ProjectCreationPage_3lakh(self.driver)
#  project.click_files_menu()
#  project.click_entry_of_new_work_menu()
#  project.click_add_work_button()

        # Project Creation Navigation
        project = ProjectCreationPage_3lakh(self.driver)

        print(self.driver.current_url)
        print(self.driver.title)

        project.click_files_menu()

        self.driver.save_screenshot(
            ".\\Screenshots\\entry_of_new_work_visible11.png"
        )

        project.click_entry_of_new_work_menu()

        self.logger.info(
            "Clicked Entry Of New Work"
        )

        project.click_add_work_button()
# ---------------------------------------------------------------------
        # Close popup if it appears again
        dashboard.click_success_continue()

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("/new-work/add")
        )

        print(
            "URL After Add Click =",
            self.driver.current_url
        )

        self.driver.save_screenshot(
            ".\\Screenshots\\after_add_click1.png"
        )

        self.logger.info(
            "Clicked Add Work"
        )

        assert project.verify_add_project_page()

        self.logger.info(
            "Add Project Page Opened Successfully"
        )

        print(
            "Current URL =",
            self.driver.current_url
        )

        assert "/new-work/add" in self.driver.current_url

        self.driver.save_screenshot(
            ".\\Screenshots\\add_project_page.png"
        )

        self.driver.quit()


    # 2nd Test Method i.e. add project test case, for 2nd test we need to crt object once again "project = ...."
    @pytest.mark.sanity
    @pytest.mark.regression
    def navigate_to_add_project_page(self):
        self.driver.get(self.base_url)
        login = Login(self.driver)

        self.driver.set_window_size(1366, 768)
        self.driver.execute_script(
            "document.body.style.zoom='70%'"
        )


        login.click_login_menu()
        login.select_password_login()
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login_button()
        dashboard = DashboardPage(self.driver)
        dashboard.click_success_ok()
        dashboard.click_success_continue()

        project = ProjectCreationPage_3lakh(self.driver)

        self.driver.set_window_size(1366, 768)
        self.driver.execute_script(
            "document.body.style.zoom='70%'"
        )

        project.click_files_menu()
        project.click_entry_of_new_work_menu()
        project.click_add_work_button()
        dashboard.click_success_continue()

        self.driver.set_window_size(1366, 768)
        self.driver.execute_script(
            "document.body.style.zoom='60%'"
        )

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("/new-work/add")
        )

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_create_project(self, setup):   #2nd execute
        self.driver = setup
        self.navigate_to_add_project_page()
        project = ProjectCreationPage_3lakh(self.driver)

        self.driver.set_window_size(1366, 768)
        self.driver.execute_script(
            "document.body.style.zoom='60%'"
        )

        self.logger.info(
            "************************Project Creation Test Started******************************"
        )

        self.logger.info(
            "***********************************Entering Project Details************************"
        )


        project_name = f"Improvement of road from A house to B house {int(time.time())}"

        project.select_financial_year("2025-26")
        project.enter_project_name(project_name)
        project.select_department("Panchayati Raj and Drinking Water Department")
        project.enter_project_description("Panchayati Raj and Drinking Water Department PPMS from PR&DW Deptt")
        project.select_project_type("New Work")
        project.select_scheme_name("5th SFC Grant in Aid")
        project.select_scheme_component("103 - Maintenance and improvement of Road infrastructure")
        project.select_project_category("Road")
        project.select_project_subcategory("CC Road")
        project.select_execution_level("Gram Panchayat (GP)")
        project.select_project_period("New")

        # Proposal Details
        project.enter_proposal_ltr_no("3784")
        project.enter_proposal_ltr_date("06/23/2026")
        project.enter_estimate_cost("300000")

        # Approval Details
        project.enter_approval_ltr_no("8529")
        project.enter_approval_ltr_date("06/23/2026")

        # Sanction Details
        project.enter_sanction_ltr_no("SL001")
        project.enter_sanction_ltr_date("06/23/2026")
        project.enter_sanction_amount("300000")

        # Location Details
        project.select_location_type("Rural")
        project.select_district("Khordha")
        project.select_block("Bhubaneswar")
        project.select_gram_panchayat("Andhrua")
        project.select_village("Andharua")

        # Submit
        # Submit and validate success message
        try:

            actual_success_message = project.click_submit_add_project()

            assert "Project successfully created" in actual_success_message

            self.driver.save_screenshot(
                ".\\Screenshots\\project_creation_success.png"
            )

            self.logger.info(
                "Project created successfully and success message displayed"
            )

        except Exception as e:

            self.driver.save_screenshot(
                ".\\Screenshots\\project_creation_failed.png"
            )

            self.logger.error(str(e))

            raise

        # self.driver.quit()



    # Add Project method call

    # project_page.navigate_to_add_project_page()
    #
    # project_page.create_new_project(
    #     financial_year="2025-26",
    #     project_name="Road Construction",
    #     department="PR&DW",
    #     project_description="Village Road",
    #     project_type="Civil",
    #     scheme_name="MGNREGS",
    #     scheme_component="Road",
    #     category="Infrastructure",
    #     subcategory="Road",
    #     execution_level="GP",
    #     project_period="1 Year",
    #     proposal_letter_no="PL001",
    #     proposal_date="01/06/2026",
    #     estimated_cost="250000",
    #     approval_letter_no="AL001",
    #     approval_date="05/06/2026",
    #     sanction_letter_no="SL001",
    #     sanction_date="10/06/2026",
    #     sanction_amount="250000",
    #     location_type="Rural",
    #     district="Puri",
    #     block="Pipili",
    #     gram_panchayat="Rupadeipur",
    #     village="Nuagaon"
    # )
