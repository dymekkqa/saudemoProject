import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.HOST

    USERNAME_FIELD = ("id", "user-name")
    PASSWORD_FIELD = ("id", "password")
    SUBMIT_BUTTON = ("id", "login-button")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)
        self.wait.until(EC.text_to_be_present_in_element_value(self.USERNAME_FIELD, login))

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
        self.wait.until(EC.text_to_be_present_in_element_value(self.PASSWORD_FIELD, password))

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("User login with credentials")
    def user_login(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_submit_button()
