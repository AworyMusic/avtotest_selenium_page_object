from .pages.product_page import ProductPage
from .pages.locators import ProductPageBasketLocators
import time
from .pages.product_page import Product
import pytest
from .pages.product_page import RegisterNewUser

@pytest.mark.parametrize('url', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, url):
        url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        basket = ProductPage(browser,url)
        basket.open()
        basket.add_to_basket()
        basket.solve_quiz_and_get_code()
        basket = Product(browser,browser.current_url)
        basket.should_be_product_page()
        time.sleep(1)

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    basket = ProductPageBasketLocators(browser, url)
    basket.click_basket_button()
    basket = ProductPage(browser, url)
    basket.should_be_none_seccsess_message()

@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()

@pytest.mark.login_guest
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
    loginpage = RegisterNewUser(browser, url)
    loginpage.regnewuseryes()
    
@pytest.mark.need_review
@pytest.mark.xfail(reason="wait fo fix bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    basket = ProductPage(browser,url)
    basket.open() 
    basket.add_to_basket() 
    basket.should_be_none_seccsess_message()

@pytest.mark.need_review 
@pytest.mark.xfail(reason="wait fo fix bug")
def test_guest_cant_see_success_message(browser): 
    url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    basket = ProductPage(browser,url)
    basket.open() 
    basket.should_be_none_seccsess_message()
 
@pytest.mark.xfail(reason="wait fo fix bug")
def test_message_disappeared_after_adding_product_to_basket(browser): 
    url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    basket = ProductPage(browser,url)
    basket.open() 
    basket.add_to_basket()
    basket.should_be_none_seccsess_message()

@pytest.mark.xfail(reason="wait fo fix bug")        
class TestUserAddToBasketFromProductPage():

    def test_user_cant_see_success_message(browser): 
        url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        basket = ProductPage(browser,url)
        basket.open() 
        basket.should_be_none_seccsess_message()

    def test_user_can_add_product_to_basket(browser):
        url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        basket = ProductPage(browser,url)
        basket.open()
        basket.should_be_none_seccsess_message()
        basket.add_to_basket()
        basket.solve_quiz_and_get_code()
        basket = Product(browser,browser.current_url)
        basket.should_be_product_page()
