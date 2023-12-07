import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    PAGE_URL = Links.CART_PAGE
    CART_ITEM = ("class name", "cart_item")
    ITEM_PRICE_ON_CART = ("class name", 'inventory_item_price')
    CHECKOUT_BUTTON = ("id", "checkout")

    def items_value_on_cart(self, value):
        with allure.step(f"Verify items value on Cart {value}"):
            cart_items = self.driver.find_elements(*self.CART_ITEM)
            count = len(cart_items)
            assert count == value

    def item_price(self):
        with allure.step("Verify item price value on Cart"):
            item_price = self.wait.until(EC.element_to_be_clickable(self.ITEM_PRICE_ON_CART)).text.replace('$', '')
            return float(item_price)

    def checkout_button_action(self):
        with allure.step("Click on Checkout button"):
            self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

