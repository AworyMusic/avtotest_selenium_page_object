from .locators import BasketLocators
from .base_page import BasePage
from .locators import ProductPageBasketLocators
from .locators import BasePageLocators
from .locators import LoginPage

class RegisterNewUser(LoginPage):
    def regnewuseryes(self):
        self.register_new_user()

class ProductPage(BasePage):


    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def add_to_basket(self):
        basket = self.browser.find_element(*BasketLocators.BASKET)
        basket.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_none_seccsess_message(self):
        assert self.is_not_element_present(*BasketLocators.SUCCESS_MESSAGE)

    def should_be_none_seccsess_message(self):
        assert self.is_element_present(*BasketLocators.NO_SUCCESS_MESSAGE_IN_BASKET)


class Product(ProductPageBasketLocators):
    def should_be_product_page(self):
        #self.should_be_login_url()
        self.should_be_name_product()
        self.should_be_price_product()
        self.should_be_sklad()
        self.click_basket_button()
        self.should_be_price_in_basket()
        self.should_be_price_book_in_basket()

class MainPage(BasePage):
    """def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)"""
    pass
