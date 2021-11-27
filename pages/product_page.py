from .locator import ProductPageLocators,BasePageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def should_be_add_to_cart_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "Add to cart button is not presented"
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN).click()
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    def check_info(self, link):
        name_in_basket = self.browser.find_elements(*ProductPageLocators.ALERT_PRODUCT_NAME)[0].text
        price_in_basket = self.browser.find_elements(*ProductPageLocators.ALERT_PRICE_IN_CART)[2].text
        try:
            assert self.get_product_name() == name_in_basket, "name mismatch"
            assert self.get_product_price() == price_in_basket, "price mismatch"
        except AssertionError:
            print(f"{link} FAILED")
        else:
            print("--OK--")
    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
    def should_not_be_success_message_is_disappeared(self):
        assert not self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_be_logged_in(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented"


#Hello
