from .locator import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_ITEM), "Cart item is presented, but should not be"
    def should_be_text_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_TEXT), "'Your basket is empty.' text is not presented on cart"