from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException

class MainPage(BasePage, MainPageLocators):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
        


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK)