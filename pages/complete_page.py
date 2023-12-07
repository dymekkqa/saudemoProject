import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CompletePage(BasePage):
    PAGE_URL = Links.COMPLETE_PAGE

    BACK_TO_PRODUCTS_PAGE_BUTTON = ("id", "back-to-products")

    def back_to_products_button(self):
        with allure.step("Verify user open Products page by click on Back to products button"):
            self.wait.until(EC.element_to_be_clickable(self.BACK_TO_PRODUCTS_PAGE_BUTTON)).click()
