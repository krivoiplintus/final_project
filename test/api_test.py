import allure
from page.company_api import CompanyApi
from configyration.config_provider import ConfigProvider
from test_data.data_provider import DataProvider


base_url = ConfigProvider().get_api_base_url()
token = ConfigProvider().get_api_token()
id_book = DataProvider().get_id_book()


@allure.title("Получение списка книг в корзине")
def test_get_book_in_cart():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url, token)
    result = api.get_book_in_cart()
    with allure.step("Проверить, что корзина пуста"):
        assert result["cost"] == 0


@allure.title("Добавление книги в корзину")
def test_add_book_in_cart():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url, token)
    resp = api.add_book_in_cart(id_book)
    result = api.get_book_in_cart()
    with allure.step("Проверить, что id книги в корзине соответствует id добавленной книги"):
        assert result["products"][0]["goodsId"] == id_book
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 200
    api.delete_book_in_cart()


@allure.title("Удаление книги из корзины")
def test_delete_book_in_cart():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url, token)
    api.add_book_in_cart(id_book)
    resp = api.delete_book_in_cart()
    result = api.get_book_in_cart()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 204
    with allure.step("Проверить, что корзина пуста"):
        assert result["cost"] == 0


@allure.title("Изменение количества книг в корзине")
def test_increasing_books_in_cart():
    number_of_books = DataProvider().get_number_of_books()
    new_number_of_books = DataProvider().get_new_number_of_books()
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url, token)
    api.add_book_in_cart(id_book)
    resp1 = api.change_book_in_cart(number_of_books)
    result1 = api.get_book_in_cart()
    resp2 = api.change_book_in_cart(new_number_of_books)
    result2 = api.get_book_in_cart()
    with allure.step("Проверить, что id книги в корзине соответствует id добавленной книги"):
        assert result1["products"][0]["goodsId"] == id_book
        assert result2["products"][0]["goodsId"] == id_book
    with allure.step("Проверить, что количество книг в корзине соответствует количеству добавленных книг"):
        assert result1["products"][0]["quantity"] == number_of_books
        assert result2["products"][0]["quantity"] == new_number_of_books
    with allure.step("Проверить, что количество книг в корзине изменилось"):
        assert result1["products"][0]["quantity"] - result2["products"][0]["quantity"] == number_of_books - new_number_of_books
    with allure.step("Проверить код ответа"):
        assert resp1.status_code == 200
        assert resp2.status_code == 200


@allure.title("Добавление книги с несуществующим id в корзину")
def test_add_book_in_cart_neg():
    fake_id_book = DataProvider().get_fake_id_book()
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url, token)
    resp = api.add_book_in_cart(fake_id_book)
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 500


@allure.title("Удаление книги из корзины с использованием другова метода")
def test_delete_book_in_cart_neg():
    with allure.step("Подключится к API"):
        api = CompanyApi(base_url, token)
    api.add_book_in_cart(id_book)
    resp = api.delete_book_in_cart_post()
    result = api.get_book_in_cart()
    api.delete_book_in_cart()
    with allure.step("Проверить код ответа"):
        assert resp.status_code == 405
    with allure.step("Проверить, что книга в корзин"):
        assert result["products"][0]["goodsId"] == id_book
