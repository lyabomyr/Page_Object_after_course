from .base_page import BasePage
from .locator import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "in url not present world \'login\'" # проверкa на корректный url адрес


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "E-mail input is not presented on login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PW),"Password input is not presented on login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Submit button is not presented on login form"
        # check, что есть форма логина


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), "submit button is not present on registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PW1), "Password input is not presented on registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Email is not present on registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PW2), "Confirm password input is not presented on registration form"

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        user_email.send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.REGISTER_PW1)
        user_password.send_keys(password)
        user_password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PW2)
        user_password2.send_keys(password)
        login_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        login_btn.click()

    def should_be_logged_in(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented"