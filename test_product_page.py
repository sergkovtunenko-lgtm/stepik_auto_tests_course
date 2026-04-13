import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
PRODUCT_LINK_WITHOUT_PROMO = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        product_name = page.get_product_name()
        page.add_to_basket()
        page.solve_quiz()
        page.should_be_success_message_with_product_name(product_name)
        page.should_be_basket_total_equal_to_product_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_LINK_WITHOUT_PROMO)
        page.open()
        page.should_not_be_success_message()


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_LINK)
        page.open()
        product_name = page.get_product_name()
        page.add_to_basket()
        page.solve_quiz()
        page.should_be_success_message_with_product_name(product_name)
        page.should_be_basket_total_equal_to_product_price()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_LINK_WITHOUT_PROMO)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_LINK_WITHOUT_PROMO)
        page.open()
        page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_LINK_WITHOUT_PROMO)
        page.open()
        page.add_to_basket()
        page.should_disappear_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, PRODUCT_LINK_WITHOUT_PROMO)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_empty_basket_message()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, PRODUCT_LINK_WITHOUT_PROMO)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
