from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_main_page(self):
        assert self.is_element_present(*MainPageLocators.LOGO), \
            "No logo"
        assert self.is_element_present(*MainPageLocators.HIDE_LEFT_MENU_BUTTON), \
            "No hide left menu button"
        assert self.is_element_present(*MainPageLocators.SWITCH_LOCALIZATION_BUTTON), \
            "No switch localization button"
        assert self.is_element_present(*MainPageLocators.SWITCH_THEME_BUTTON), \
            "No switch theme button"
        assert self.is_element_present(*MainPageLocators.USER_ICON_BUTTON), \
            "No user icon"
        assert self.is_element_present(*MainPageLocators.LEFT_MENU), \
            "No left menu"
        assert self.get_attribute(*MainPageLocators.BODY, "class") == "dark-theme", \
            "Dark Theme is not default"
        assert self.get_attribute(*MainPageLocators.LOGO, "alt") == "Logo icon", \
            "Localization is not english"

    def switch_localization(self):
        default_value = self.get_attribute(*MainPageLocators.LOGO, "alt")
        self.click_button(*MainPageLocators.SWITCH_LOCALIZATION_BUTTON)
        switch_value = self.get_attribute(*MainPageLocators.LOGO, "alt")
        assert default_value != switch_value, "Localization is not changed"

    def switch_theme(self):
        default_theme = self.get_attribute(*MainPageLocators.BODY, "class")
        self.click_button(*MainPageLocators.SWITCH_THEME_BUTTON)
        switch_theme = self.get_attribute(*MainPageLocators.BODY, "class")
        assert default_theme != switch_theme, "Theme is not changed"

    def hide_left_menu(self):
        assert self.get_attribute(*MainPageLocators.HIDE_LEFT_MENU_BUTTON, "class") \
               == "panel-switcher rotated", "Left menu is hidden now"
        self.click_button(*MainPageLocators.HIDE_LEFT_MENU_BUTTON)
        assert self.get_attribute(*MainPageLocators.HIDE_LEFT_MENU_BUTTON, "class") \
               == "panel-switcher", "Left menu is not hidden now"

    def show_left_menu(self):
        assert self.get_attribute(*MainPageLocators.HIDE_LEFT_MENU_BUTTON, "class") \
               == "panel-switcher", "Left menu is not hidden now"
        self.click_button(*MainPageLocators.HIDE_LEFT_MENU_BUTTON)
        assert self.get_attribute(*MainPageLocators.HIDE_LEFT_MENU_BUTTON, "class") \
               == "panel-switcher rotated", "Left menu is hidden now"
