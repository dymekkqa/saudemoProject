import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Buy products by cart")
class TestShopping(BaseTest):

    @allure.title("User Login")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_perform_login(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.home_page.is_opened()

    @allure.title("User add item to cart")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_item_to_cart(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.add_item_to_cart()
        self.home_page.items_value_on_cart(1)

    @allure.title("User add item to cart from item page")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_item_to_cart_from_item_page(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.open_item_page()
        self.home_page.add_item_to_cart()
        self.home_page.items_value_on_cart(1)

    @allure.title("User open Cart Page")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_open_cart_page(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.cart_button()
        self.cart_page.is_opened()

    @allure.title("Verify item price on Cart Page")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_items_data_on_cart(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.add_item_to_cart()
        item_price = self.home_page.item_price()
        self.home_page.cart_button()
        item_price_on_cart = self.cart_page.item_price()
        assert item_price == item_price_on_cart

    @allure.title("Verify item values on Cart Page")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_item_values_on_cart(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.add_item_to_cart()
        self.home_page.cart_button()
        self.cart_page.items_value_on_cart(1)

    @allure.title("Open Personal page")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_open_personal_page(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.add_item_to_cart()
        self.home_page.cart_button()
        self.cart_page.checkout_button_action()
        self.personal_page.is_opened()

    @allure.title("User input personal date")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_input_personal_date(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.add_item_to_cart()
        self.home_page.cart_button()
        self.cart_page.checkout_button_action()
        self.personal_page.input_personal_date()
        self.checkout_page.is_opened()

    @allure.title("User finish ordering item")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_input_personal_date(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.add_item_to_cart()
        self.home_page.cart_button()
        self.cart_page.checkout_button_action()
        self.personal_page.input_personal_date()
        self.checkout_page.finish_button()
        self.complete_page.is_opened()

    @allure.title("User back to Product page")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_input_personal_date(self):
        self.login_page.open()
        self.login_page.user_login(self.data.LOGIN, self.data.PASSWORD)
        self.home_page.add_item_to_cart()
        self.home_page.cart_button()
        self.cart_page.checkout_button_action()
        self.personal_page.input_personal_date()
        self.checkout_page.finish_button()
        self.complete_page.back_to_products_button()
        self.home_page.is_opened()




