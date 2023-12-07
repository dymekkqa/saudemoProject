import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    PAGE_URL = Links.CHECKOUT_PAGE

    TAX_VALUE = ("class name", "summary_tax_label")
    TOTAL_PRICE_VALUE = ("css selector", '.summary_info_label.summary_total_label')
    CART_LIST_ITEMS = ("class name", 'cart_list')
    CART_ITEM_LOCATOR = ("class name", "cart_item")
    ITEM_PRICE_LOCATOR = ("class name", 'inventory_item_price')
    FINISH_BUTTON = ("id", "finish")

    def value_tax_price(self):
        with allure.step("Verify tax price value"):
            tax_price = self.wait.until(EC.element_to_be_clickable(self.TAX_VALUE)).text.replace('Tax: $', '')
            return float(tax_price)

    def value_total_price(self):
        with allure.step("Verify Total price"):
            total_price = self.wait.until(EC.element_to_be_clickable(self.TOTAL_PRICE_VALUE)).text.replace(
                'Total: $',
                '')
            return float(total_price)

    def subtotal_sum_items_price(self, result):
        with allure.step("Verify subtotal price"):
            cart_container = self.wait.until(EC.element_to_be_clickable(self.CART_LIST_ITEMS))
            cart_items = cart_container.find_elements(*self.CART_ITEM_LOCATOR)
            list_result = []
            for cart_item in cart_items:
                price_element = cart_item.find_element(self.ITEM_PRICE_LOCATOR)
                price_text = price_element.text
                price_value = float(price_text.replace('$', ''))
                list_result.append(price_value)
            total_price = sum(list_result)
            assert total_price == result

    def finish_button(self):
        with allure.step("Verify order by click on Finish button"):
            self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
