from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    def should_be_login_url(self):
        LOGIN_URL = self.browser.current_url
        assert "login" in LOGIN_URL, "Login URL is incorrect"

    def should_be_register_form(self):
        REGISTER_FORM = self.is_element_present(By.CSS_SELECTOR, "#register_form")
        assert True
 
 
    def should_be_login_form(self): 
        LOGIN_FORM = self.is_element_present(By.CSS_SELECTOR, "#login_form") 
        assert True