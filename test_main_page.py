from .pages.product_page import ProductPage
from .pages.locators import ProductPageBasketLocators
import pytest

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    basket = ProductPageBasketLocators(browser, url)
    basket.click_basket_button()
    basket = ProductPage(browser, url)
    basket.should_be_none_seccsess_message()

@pytest.mark.need_review
@pytest.mark.login_guest
class TestLoginFromMainPage():                     
    def test_guest_can_go_to_login_page(self, browser): 
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, url)
        self.page.open()
        self.page.go_to_login_page()    
        

    def test_guest_should_see_login_link(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, url)
        self.page.open()
        self.page.should_be_login_link()