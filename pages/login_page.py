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
        pass
