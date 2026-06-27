# Class            → Represents Page
# Locator          → Address of Element
# __init__()       → Constructor
# self.driver      → Browser Controller
# find_element()   → Locate Element
# WebDriverWait    → Dynamic Wait
# EC               → Expected Condition
# scrollIntoView() → Bring Element Into View
# execute_script() → Run JavaScript
# click()          → Click Element
# return True      → Verification Success
# try/except       → Handle Unexpected Popup




#   1. Class Declaration
#   2. Keep all Locators => Class Variables.
#   3. create constructor
#   4. create methods for different actions. like navigate, click, verifying the page and handel the pop up


#      1. Class Declaration Create a class which inherits "BasePage" Because common methods may already exist in "BasePage"
#      2. Constructor Creations => Runs automatically whenever object is created. & Call parent class constructor => super().__init__(driver) <==> BasePage.__init__(driver) we use this because "Initialize parent class variables."
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.BasePage import BasePage
import time


class ProjectCreationPage_3lakh(BasePage):

    lnkfile_menu_xpath = "//a[contains(.,'File')]"

    lnkentry_of_new_work_menu_xpath = (
        "//a[contains(.,'Entry of New Work')]"
    )

    lnkaddwork_submenuitem_xpath = (
        "//a[contains(@href,'new-work/add')]"
    )

    page_title_xpath = "//*[contains(text(),'Add Project')]"

    # Add Projects at BDO login

    ddl_financial_year_xpath = "//select[@name='financial_year']"
    txt_project_name_xpath = "//input[@name='project_name']"
    ddl_department_xpath = "//select[@name='department_id']"

    txt_project_description_xpath = "//textarea[@name='project_description']"

    ddl_project_type_xpath = "//select[@name='project_type_id']"
    ddl_scheme_name_xpath = "//select[@id='scheme_id']"
    ddl_scheme_component_xpath = "//select[@id='scheme_component_id']"

    ddl_project_category_xpath = "//select[@id='project_category_id']"
    ddl_project_subcategory_xpath = "//select[@id='project_subcategory_id']"
    ddl_execution_level_xpath = "//select[@id='execution_level']"

    ddl_project_period_xpath = "//select[@id='project_period']"

    txt_district_proposal_letter_no_xpath = "//input[@name='proposal_letter']"
    dt_district_proposal_letter_date_xpath = "//input[@id='proposal_date']"

    txt_proposed_estimated_cost_xpath = "//input[@id='proposed_estimated_cost']"

    txt_project_approval_letter_no_xpath = "//input[@name='project_approval_letter']"
    dt_project_approval_date_xpath = "//input[@id='approval_date']"

    txt_fund_sanction_letter_no_xpath = "//input[@name='fund_sanction_letter_no']"
    dt_fund_sanction_letter_date_xpath = "//input[@id='sanction_letter_date']"

    txt_sanction_amount_xpath = "//input[@id='sanction_amount']"

    # Location details add Project
    ddl_location_type_xpath = "//select[@id='location_type']"
    ddl_district_xpath = "//select[@id='project_district']"
    ddl_block_xpath = "//select[@id='project_block']"
    ddl_gram_panchayat_xpath = "//select[@id='project_panchayat']"
    ddl_village_xpath = "//select[@id='project_village']"

    # Submit Projects confirmation msg yes no btn
    btn_submit_xpath = "//button[normalize-space()='Submit']"
    confirm_yes_btn_xpath = "//button[normalize-space()='Yes']"
    success_project_created_msg_xpath = "//div[contains(@class,'jconfirm-content') and contains(normalize-space(),'Project successfully created')]"
    success_ok_btn_xpath = "//button[normalize-space()='OK']"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # Navigation Methods
    def click_files_menu(self):

        file_menu = self.driver.find_element(
            By.XPATH,
            self.lnkfile_menu_xpath
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", # Bring menu into visible area.
            file_menu
        )

        self.driver.execute_script(
            "arguments[0].click();",  #  Click Add Work.
            file_menu
        )

    def click_entry_of_new_work_menu(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    self.lnkentry_of_new_work_menu_xpath
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", #  Scroll page until File Menu comes into view.
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def click_add_work_button(self):

        add_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.lnkaddwork_submenuitem_xpath)
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_btn
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_btn
        )

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("/new-work/add")
        )

        print("URL After Add Click =", self.driver.current_url)

    def verify_add_project_page(self):

        WebDriverWait(self.driver, 20).until(
            EC.url_contains("/new-work/add")
        )

        return True

    def close_browser_popup(self):  # Close popup if popup appears.

        try:
            popup_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[@onclick='closeModernPopup()']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].click();",
                popup_btn
            )

            print("OK popup closed")

        except:
            print("OK popup not displayed")

    # Financial Year
    def select_financial_year(self, financial_year):
        Select(
            self.driver.find_element(
                By.XPATH,
                self.ddl_financial_year_xpath
            )
        ).select_by_visible_text(financial_year)

    # Project Name
    def enter_project_name(self, project_name):
        self.driver.find_element(
            By.XPATH,
            self.txt_project_name_xpath
        ).send_keys(project_name)

    # Department
    def select_department(self, department):
        Select(
            self.driver.find_element(
                By.XPATH,
                self.ddl_department_xpath
            )
        ).select_by_visible_text(department)

    # Project Description
    def enter_project_description(self, description):
        self.driver.find_element(
            By.XPATH,
            self.txt_project_description_xpath
        ).send_keys(description)

    # Project Type
    def select_project_type(self, project_type):
        Select(
            self.driver.find_element(By.XPATH,
                                     self.ddl_project_type_xpath)
        ).select_by_visible_text(project_type)

    # Scheme Name need wait timer
    def select_scheme_name(self, scheme_name):

        scheme_dropdown = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.ddl_scheme_name_xpath)
            )
        )

        Select(scheme_dropdown).select_by_visible_text(scheme_name)

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_scheme_component_xpath
                    )
                ).options
            ) > 1
        )

    # Scheme Component
    def select_scheme_component(self, scheme_component):

        component_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.ddl_scheme_component_xpath)
            )
        )

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_scheme_component_xpath
                    )
                ).options
            ) > 1
        )

        component_select = Select(component_dropdown)

        all_options = [
            option.text.strip()
            for option in component_select.options
        ]

        print("Available Scheme Components =", all_options)

        for option in component_select.options:
            if option.text.strip() == scheme_component.strip():
                option.click()
                return

        raise Exception(
            f"Scheme Component not found: {scheme_component}. "
            f"Available options are: {all_options}"
        )

    # Project Category
    def select_project_category(self, project_category):

        category_dropdown = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.ddl_project_category_xpath)
            )
        )

        Select(category_dropdown).select_by_visible_text(project_category)

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_project_subcategory_xpath
                    )
                ).options
            ) > 1
        )

    # Project Subcategory
    def select_project_subcategory(self, project_subcategory):

        subcategory_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.ddl_project_subcategory_xpath)
            )
        )

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_project_subcategory_xpath
                    )
                ).options
            ) > 1
        )

        subcategory_select = Select(subcategory_dropdown)

        all_options = [
            option.text.strip()
            for option in subcategory_select.options
        ]

        print("Available Project Subcategories =", all_options)

        for option in subcategory_select.options:
            if option.text.strip() == project_subcategory.strip():
                option.click()
                return

        raise Exception(
            f"Project Subcategory not found: {project_subcategory}. "
            f"Available options are: {all_options}"
        )

    # Execution Level
    def select_execution_level(self, execution_level):
        Select(
            self.driver.find_element(By.XPATH, self.ddl_execution_level_xpath)
        ).select_by_visible_text(execution_level)

    # Project Period
    def select_project_period(self, project_period):
        Select(
            self.driver.find_element(By.XPATH, self.ddl_project_period_xpath)
        ).select_by_visible_text(project_period)

    # District proposal Letter No
    def enter_proposal_ltr_no(self, ltr_no):
        self.driver.find_element(
            By.XPATH,
            self.txt_district_proposal_letter_no_xpath
        ).send_keys(ltr_no)

    # District proposal Letter Date
    def enter_proposal_ltr_date(self, ltr_date):
        self.driver.find_element(
            By.XPATH,
            self.dt_district_proposal_letter_date_xpath
        ).send_keys(ltr_date)

    # Proposed Estimated Cost
    def enter_estimate_cost(self, estimated_cost):
        self.driver.find_element(
            By.XPATH,
            self.txt_proposed_estimated_cost_xpath
        ).send_keys(estimated_cost)

    # Project Approval Letter No
    def enter_approval_ltr_no(self, approval_ltr_no):
        self.driver.find_element(
            By.XPATH,
            self.txt_project_approval_letter_no_xpath
        ).send_keys(approval_ltr_no)

    # Project Approval Date
    def enter_approval_ltr_date(self, approval_ltr_date):
        self.driver.find_element(
            By.XPATH,
            self.dt_project_approval_date_xpath
        ).send_keys(approval_ltr_date)


    # txt_fund_sanction_letter_no_xpath
    def enter_sanction_ltr_no(self, sanction_ltr_no):
        self.driver.find_element(
            By.XPATH,
            self.txt_fund_sanction_letter_no_xpath
        ).send_keys(sanction_ltr_no)

    # Fund Sanction Date
    def enter_sanction_ltr_date(self, sanction_ltr_date):
        self.driver.find_element(
            By.XPATH,
            self.dt_fund_sanction_letter_date_xpath
        ).send_keys(sanction_ltr_date)

    # Sanction Amount
    def enter_sanction_amount(self, sanction_amount):
        self.driver.find_element(
            By.XPATH,
            self.txt_sanction_amount_xpath
        ).send_keys(sanction_amount)


    # Project Location

    # Location Type
    def select_location_type(self, location_type):

        location_dropdown = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.ddl_location_type_xpath)
            )
        )

        Select(location_dropdown).select_by_visible_text(location_type)

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_district_xpath
                    )
                ).options
            ) > 1
        )

    # District
    def select_district(self, district):

        district_dropdown = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.ddl_district_xpath)
            )
        )

        Select(district_dropdown).select_by_visible_text(district)

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_block_xpath
                    )
                ).options
            ) > 1
        )

    # Block
    def select_block(self, block):

        block_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.ddl_block_xpath)
            )
        )

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_block_xpath
                    )
                ).options
            ) > 1
        )

        block_select = Select(block_dropdown)

        all_options = [
            option.text.strip()
            for option in block_select.options
        ]

        print("Available Blocks =", all_options)

        for option in block_select.options:
            if option.text.strip() == block.strip():
                option.click()
                return

        raise Exception(
            f"Block not found: {block}. "
            f"Available Blocks are: {all_options}"
        )
    # Gram Panchayat
    def select_gram_panchayat(self, gram_panchayat):

        gp_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.ddl_gram_panchayat_xpath)
            )
        )

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_gram_panchayat_xpath
                    )
                ).options
            ) > 1
        )

        gp_select = Select(gp_dropdown)

        all_options = [
            option.text.strip()
            for option in gp_select.options
        ]

        print("Available Gram Panchayats =", all_options)

        for option in gp_select.options:
            if option.text.strip() == gram_panchayat.strip():
                option.click()
                return

        raise Exception(
            f"Gram Panchayat not found: {gram_panchayat}. "
            f"Available Gram Panchayats are: {all_options}"
        )

    # Village
    def select_village(self, village):

        village_dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, self.ddl_village_xpath)
            )
        )

        WebDriverWait(self.driver, 20).until(
            lambda driver: len(
                Select(
                    driver.find_element(
                        By.XPATH,
                        self.ddl_village_xpath
                    )
                ).options
            ) > 1
        )

        village_select = Select(village_dropdown)

        all_options = [
            option.text.strip()
            for option in village_select.options
        ]

        print("Available Villages =", all_options)

        for option in village_select.options:
            if option.text.strip() == village.strip():
                option.click()
                return

        raise Exception(
            f"Village not found: {village}. "
            f"Available Villages are: {all_options}"
        )

    # Submit
    # Submit
    # Submit
    def click_submit_add_project(self):

        submit_btn = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, self.btn_submit_xpath)
            )
        )

        # Hide PHP debug bar because it is blocking Submit button
        self.driver.execute_script(
            """
            document.querySelectorAll('.phpdebugbar, .phpdebugbar-resize-handle')
            .forEach(function(element) {
                element.style.display = 'none';
            });
            """
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            submit_btn
        )

        self.driver.execute_script(
            "arguments[0].click();",
            submit_btn
        )

        print("Submit button clicked successfully")

        # Wait for confirmation popup and click Yes
        yes_btn = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.confirm_yes_btn_xpath)
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            yes_btn
        )

        print("Confirmation Yes button clicked successfully")

        # Wait for final success message after Yes click
        success_msg = WebDriverWait(self.driver, 120).until(
            EC.presence_of_element_located(
                (By.XPATH, self.success_project_created_msg_xpath)
            )
        )

        success_text = success_msg.text.strip()

        print("Success Message Displayed =", success_text)

        # Screenshot while success popup is visible
        self.driver.save_screenshot(".\\Screenshots\\project_creation_success_popup.png")

        # Optional: wait 3 seconds so you can see/capture the success message
        time.sleep(3)

        return success_text

