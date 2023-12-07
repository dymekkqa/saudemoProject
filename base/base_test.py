import pytest
from config.data import Data
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.personal_page import PersonalPage
from pages.checkout_page import CheckoutPage
from pages.complete_page import CompletePage


class BaseTest:
    data: Data

    login_page: LoginPage
    home_page: HomePage
    cart_page: CartPage
    personal_page: PersonalPage
    checkout_page: CheckoutPage
    complete_page: CompletePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.cart_page = CartPage(driver)
        request.cls.personal_page = PersonalPage(driver)
        request.cls.checkout_page = CheckoutPage(driver)
        request.cls.complete_page = CompletePage(driver)
