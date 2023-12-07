import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    PAGE_URL = Links.HOME_PAGE

    ADD_TO_CART_BUTTON = ("id", "add-to-cart-sauce-labs-backpack")
    ITEM_NAME_LINK = ("id", "item_4_img_link")
    VALUE_ON_CART_ITEM = ("class name", "shopping_cart_badge")
    CART_BUTTON = ("class name", "shopping_cart_link")
    ITEM_PRICE = ("class name", "inventory_item_price")
    MENU_BUTTON = ("id", "react-burger-menu-btn")

    def add_item_to_cart(self):
        with allure.step("Add item to cart by click Add button"):
            self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()

    def open_item_page(self):
        with allure.step("Open item page by click on Item Name"):
            self.wait.until(EC.element_to_be_clickable(self.ITEM_NAME_LINK)).click()

    def items_value_on_cart(self, exp_value):
        with allure.step("Verify items value on cart"):
            value = self.wait.until(EC.element_to_be_clickable(self.VALUE_ON_CART_ITEM)).text
            assert int(value) == exp_value

    def cart_button(self):
        with allure.step("Open cart by click on Cart button"):
            self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()

    def item_price(self):
        with allure.step("Verify item price"):
            cost = self.wait.until(EC.element_to_be_clickable(self.ITEM_PRICE)).text.replace('$', '')
            return float(cost)

    def open_menu(self):
        with allure.step("Open Menu by click on Menu button"):
            self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()
