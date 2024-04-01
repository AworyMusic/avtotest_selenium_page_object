from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        
        LOGIN_LINK = self.browser.current_url.text
        assert LOGIN_LINK == "login", "login in url"

    def should_be_login_form(self):
        self.browser.find_element(By.CSS_SELECTOR,"#login_form"), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        self.browser.find_element(By.CSS_SELECTOR,"#register_form"), "Register form is not presented"
        assert True