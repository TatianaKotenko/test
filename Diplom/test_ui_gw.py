from selenium import webdriver
from ui_UserAuthorization import UserAuthorization
from ui_search import SearchBook
from put_basket import PutBasket
from basket_delite import DeliteBasket
from add_to_cart import AddToCart

driver = webdriver.Firefox()

def test_User_Authorization():
    autorization_user = UserAuthorization(driver)
    autorization_user.enter("https://www.chitai-gorod.ru/")
    autorization_user.autorization("div.header-controls__btn")
    autorization_user.data_number("+79493972575")
    autorization_user.get_code('chg-app-button.chg-app-button--primary.chg-app-button--xl.chg-app-button--breeze.chg-app-button--block.auth-modal-content__button.auth-modal-content__button')
    autorization_user.element()
    
    assert autorization_user.element() == "Код из СМС"

    driver.quit()

def test_search_book():
    book_search_engine = SearchBook(driver)
    book_search_engine.enter("https://www.chitai-gorod.ru/")
    book_search_engine.search_field("Макс Фрай")
    book_search_engine.author_search_button("chg-app-button.chg-app-button--primary.chg-app-button--l.chg-app-button--breeze.chg-app-button--iconic.search-form__button-search.search-form__button-search")
    book_search_engine.book_looking()

    assert book_search_engine.book_looking() == "324 товара"
    
    driver.quit()

def test_put_it_in_the_basket():
    put_it_in_the_basket = PutBasket(driver)
    put_it_in_the_basket.enter("https://www.chitai-gorod.ru/")
    put_it_in_the_basket.search_field("Макс Фрай")
    put_it_in_the_basket.author_search_button("chg-app-button.chg-app-button--primary.chg-app-button--l.chg-app-button--breeze.chg-app-button--iconic.search-form__button-search.search-form__button-search")
    put_it_in_the_basket.click_book_basket("chg-app-button.chg-app-button--primary.chg-app-button--s.chg-app-button--breeze.product-buttons__main-action.product-buttons__main-action")
    number = put_it_in_the_basket.basket_number()
    
    assert number == "1"
    
    driver.quit()

def test_delite_it_in_the_basket():
    delite_in_the_basket = DeliteBasket(driver)
    delite_in_the_basket.enter("https://www.chitai-gorod.ru/")
    delite_in_the_basket.search_field("Макс Фрай")
    delite_in_the_basket.author_search_button("chg-app-button.chg-app-button--primary.chg-app-button--l.chg-app-button--breeze.chg-app-button--iconic.search-form__button-search.search-form__button-search")
    delite_in_the_basket.click_book_basket("chg-app-button.chg-app-button--primary.chg-app-button--s.chg-app-button--breeze.product-buttons__main-action.product-buttons__main-action")
    delite_in_the_basket.enter_basket("https://www.chitai-gorod.ru/cart")
    delite_in_the_basket.delite_book_basket("chg-app-button.chg-app-button--secondary.chg-app-button--m.chg-app-button--gray-cherry.chg-app-button--iconic.cart-item__delete-button.cart-item__delete-button")
    number_0 = delite_in_the_basket.basket_number_0()

    assert number_0 == "0"

    driver.quit()

def test_add_in_the_basket():
    add_in_the_basket = AddToCart(driver)
    add_in_the_basket.enter("https://www.chitai-gorod.ru/")
    add_in_the_basket.search_field("Макс Фрай")
    add_in_the_basket.author_search_button("chg-app-button.chg-app-button--primary.chg-app-button--l.chg-app-button--breeze.chg-app-button--iconic.search-form__button-search.search-form__button-search")
    add_in_the_basket.click_book_basket("chg-app-button.chg-app-button--primary.chg-app-button--s.chg-app-button--breeze.product-buttons__main-action.product-buttons__main-action")
    add_in_the_basket.enter_basket("https://www.chitai-gorod.ru/cart")
    add_in_the_basket.delite_book_basket("chg-app-button.chg-app-button--secondary.chg-app-button--m.chg-app-button--gray-cherry.chg-app-button--iconic.cart-item__delete-button.cart-item__delete-button")
    add_in_the_basket.add_to_cart('chg-app-button.chg-app-button--secondary.chg-app-button--xs.chg-app-button--gray-cherry.cart-item-deleted__button.cart-item-deleted__button')
    number_2 = add_in_the_basket.basket_number_2()

    assert number_2 == "1"

    driver.quit()
