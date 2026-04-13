from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def solve_quiz(self):
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_success_message_with_product_name(self, product_name):
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)
        assert message.text == product_name, \
            f"Product name in message '{message.text}' does not match '{product_name}'"

    def should_be_basket_total_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_price, \
            f"Basket total '{basket_price}' does not match product price '{product_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message has not disappeared"
