import random
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_INPUT = ("id", "first-name")
    LAST_NAME_INPUT = ("id", "last-name")
    POSTAL_CODE_INPUT = ("id", "postal-code")
    CONTINUE_BUTTON = ("id", "continue")

    @allure.step("Enter first name")
    def input_first_name(self, first_name):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT)).send_keys(first_name)

    @allure.step("Enter last name")
    def input_last_name(self, last_name):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_INPUT)).send_keys(last_name)

    @allure.step("Enter postal code")
    def input_postal_code(self, postal_code):
        self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE_INPUT)).send_keys(postal_code)

    def action_continue_button(self):
        with allure.step("Click on continue button"):
            self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    @allure.step("User adds personal data")
    def input_personal_date(self):
        self.input_first_name(f"Test {random.randint(1, 100)}")
        self.input_last_name(f"Testowicz {random.randint(1, 100)}")
        self.input_postal_code(f"12345{random.randint(1, 100)}")
        self.action_continue_button()
