from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_TITLE), \
            "No title"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_INPUT), \
            "No username input"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), \
            "No password input"
        assert  self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), \
            "No login button"

    def login_to_system(self, username, password):
        self.should_be_login_page()
        self.input_text(*LoginPageLocators.LOGIN_USERNAME_INPUT, username)
        self.input_text(*LoginPageLocators.LOGIN_PASSWORD_INPUT, password)
        self.click_button(*LoginPageLocators.LOGIN_BUTTON)

