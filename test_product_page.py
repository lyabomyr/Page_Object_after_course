import pytest
from pages.product_page import ProductPage
import logging
from pages.basket_page import BasketPage
import time
from pages.login_page import LoginPage

logging.basicConfig(level=logging.DEBUG)
mylogger = logging.getLogger()

@pytest.mark.parametrize('site', ["promo=offer0","promo=offer1","promo=offer2","promo=offer3","promo=offer4","promo=offer5","promo=offer6",pytest.param("promo=offer7", marks=pytest.mark.xfail),"promo=offer8","promo=offer9"])

@pytest.mark.skip(reason="no way of currently testing this")
def test_user_can_add_product_to_cart(browser,site):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?"+site
    page = ProductPage(browser, link)
    page.open(link)
    page.should_be_add_to_cart_link()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.check_info(link)

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open(link)
    page.should_be_add_to_cart_link()
    page.add_product_to_cart()
    page.check_info(link)
@pytest.mark.other
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link= "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page= ProductPage(browser,link)
    page.open(link)
    page.add_product_to_cart()
    page.should_not_be_success_message()
@pytest.mark.other
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page= ProductPage(browser,link)
    page.open(link)
    page.should_not_be_success_message()
@pytest.mark.other
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page=ProductPage(browser,link)
    page.open(link)
    page.add_product_to_cart()
    time.sleep(1)
    page.should_not_be_success_message_is_disappeared()
    
@pytest.mark.other
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open(link)
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link= "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open(link)
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open(link)
    page.go_to_cart_page()
    cart_page = BasketPage(browser, browser.current_url)
    cart_page.should_not_be_items_in_cart()
    cart_page.should_be_text_cart_is_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open(link)
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "new_pass_8"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.other
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open(link)
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open(link)
        page.should_be_logged_in()
        page.should_be_add_to_cart_link()
        page.add_product_to_cart()
        page.check_info(link)

#Thanks for rewiev