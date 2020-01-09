from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def switch_to_frame(self, how, what):
        frame = self.browser.find_element(how, what)
        self.browser.switch_to.frame(frame)

    def switch_to_default_frame(self):
        self.browser.swtich_to.default_content()

    def element_text(self, how, what):
        element = self.browser.find_element(how, what)
        text = element.text
        return text

    def input_text(self, how, what, text):
        element = self.browser.find_element(how, what)
        element.send_keys(text)

    def click_button(self, how, what):
        button = self.browser.find_element(how, what)
        button.click()

    def hover_to_element(self, how, what):
        element = self.browser.find_element(how, what)
        element.hover()

    def get_attribute(self, how, what, attribute):
        element = self.browser.find_element(how, what)
        value = element.get_attribute(attribute)
        return value
