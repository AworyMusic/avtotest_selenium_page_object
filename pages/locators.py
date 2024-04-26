from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import faker

class LoginPageLocator():
    LOGIN_INPUT = (By.CSS_SELECTOR,"#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR,"#id_registration-password1")
    PASSWORD_INPUT_REPEAT = (By.CSS_SELECTOR,"#id_registration-password2")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BUTTON_REG = (By.CSS_SELECTOR,"#register_form > button")
    SUCCESS_MESEGE_REG = (By.CSS_SELECTOR,"#messages > div > div")

class BasketLocators():

    BASKET = (By.CSS_SELECTOR,"#add_to_basket_form > button")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    NAME_PRODUCT_FROM_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    PRICE_FROM_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SKLAD_BASE = (By.CSS_SELECTOR,"div.col-sm-6.product_main > p.instock.availability")
    SKLAD_BASE_FOOTER = (By.CSS_SELECTOR,"tbody > tr:nth-child(6) > td")
    NAME_PRODUCT_IN_NAVIGATOR = (By.CSS_SELECTOR,"#default > div.container-fluid.page > div > ul > li.active")
    BASKET_BUTTON = (By.CSS_SELECTOR,".pull-right.hidden-xs > span > a")
    PRICE_IN_BASKET_BASE = (By.CSS_SELECTOR,"tr:nth-child(10) > td > h3")
    PRICE_IN_BASKET_PRODUCT = (By.CSS_SELECTOR,"tr:nth-child(2) > th.total.align-right")
    PRICE_BOOK_IN_BASKET = (By.CSS_SELECTOR,"div.col-sm-1 > p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div")
    NO_SUCCESS_MESSAGE_IN_BASKET = (By.CSS_SELECTOR,"#content_inner > p")


class LoginPage(BasePage):
    def register_new_user(self):
        f = faker.Faker(self.browser)
        helper_find = HelperFind(self.browser)
        LOGIN_INPUT = helper_find.find_element(locators=BasePageLocators.LOGIN_LINK)
        LOGIN_INPUT.send_keys("Danil@mail.ru")
        PASSWORD_INPUT = helper_find.find_element(locators=LoginPageLocator.PASSWORD_INPUT)
        PASSWORD_INPUT_REPEAT = helper_find.find_element(locators=LoginPageLocator.PASSWORD_INPUT_REPEAT)
        PASSWORD_INPUT_REPEAT and PASSWORD_INPUT.send_keys("danik1289")
        BUTTON_REG = helper_find.find_element(locators=BasePageLocators.BUTTON_REG)
        BUTTON_REG.click()
        SUCCESS_MESEGE_REG = helper_find.find_element(locators=BasePageLocators.SUCCESS_MESEGE_REG).text
        assert SUCCESS_MESEGE_REG == "Спасибо за регистрацию!"
        


class AuthorizedUser(BasePage):
        def should_be_authorized_user(self):
            assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
    

class ProductPageBasketLocators(BasePage):


    """def should_be_login_url(self):
        LOGIN_URL = self.browser.current_url
        assert "?promo=newYear" in LOGIN_URL, "Login URL is incorrect"""

    def should_be_name_product(self):
        helper_find = HelperFind(self.browser)
        NAME_PRODUCT = helper_find.find_element(locators=BasketLocators.NAME_PRODUCT).text
        NAME_PRODUCT_FROM_BASKET = helper_find.find_element(locators=BasketLocators.NAME_PRODUCT_FROM_BASKET).text
        assert NAME_PRODUCT == NAME_PRODUCT_FROM_BASKET
 
 
    def should_be_price_product(self):
        helper_find = HelperFind(self.browser) 
        PRICE_PRODUCT = helper_find.find_element(locators=BasketLocators.PRICE_PRODUCT).text 
        PRICE_FROM_BASKET = helper_find.find_element(locators=BasketLocators.PRICE_FROM_BASKET).text
        assert PRICE_PRODUCT == PRICE_FROM_BASKET


    def should_be_sklad(self):
        helper_find = HelperFind(self.browser) 
        SKLAD_BASE = helper_find.find_element(locators=BasketLocators.SKLAD_BASE).text 
        SKLAD_BASE_FOOTER = helper_find.find_element(locators=BasketLocators.SKLAD_BASE_FOOTER).text
        assert SKLAD_BASE == SKLAD_BASE_FOOTER

    def click_basket_button(self):
        helper_find = HelperFind(self.browser)
        BASKET_BUTTON = helper_find.find_element(locators=BasketLocators.BASKET_BUTTON)
        BASKET_BUTTON.click()

    

    def should_be_price_in_basket(self):
        helper_find = HelperFind(self.browser) 
        PRICE_IN_BASKET_BASE = helper_find.find_element(locators=BasketLocators.PRICE_IN_BASKET_BASE).text 
        PRICE_IN_BASKET_PRODUCT = helper_find.find_element(locators=BasketLocators.PRICE_IN_BASKET_PRODUCT).text
        assert PRICE_IN_BASKET_BASE == PRICE_IN_BASKET_PRODUCT

    def should_be_price_book_in_basket(self):
        helper_find = HelperFind(self.browser) 
        PRICE_IN_BASKET_BASE = helper_find.find_element(locators=BasketLocators.PRICE_IN_BASKET_BASE).text 
        PRICE_BOOK_IN_BASKET = helper_find.find_element(locators=BasketLocators.PRICE_BOOK_IN_BASKET).text
        assert PRICE_IN_BASKET_BASE == PRICE_BOOK_IN_BASKET

    

    """def should_not_be_success_message(self):                                        #проверяет, что элемент не появляется на странице в течение заданного времени
    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"""
    



class HelperFind():
    def __init__(self, browser):
        self.browser = browser
        
    def find_element(self, locators, time=5):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locators), message=f"Can't find element by locator {locators}")
        