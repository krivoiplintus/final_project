import allure
import requests


class CompanyApi:

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    @allure.step("Получить список книг в корзине")
    def get_book_in_cart(self) -> dict:
        response = requests.get(self.base_url + "cart", headers={"Authorization": "Bearer " + self.token})
        return response.json()

    @allure.step("Добавить книгу в корзину")
    def add_book_in_cart(self, id: int) -> requests.Response:
        body = {"id": id,
                "adData": {
                    "item_list_name": "search",
                    "product_shelf": ""
                }}
        responses = requests.post(self.base_url + "cart/product", json=body, headers={"Authorization": "Bearer " + self.token})
        return responses

    @allure.step("Удалить книгу из корзины")
    def delete_book_in_cart(self) -> requests.Response:
        self.id_to_del = str(self.get_book_in_cart()["products"][0]["id"])
        responses = requests.delete(self.base_url + "cart/product/" + self.id_to_del, headers={"Authorization": "Bearer " + self.token})
        return responses

    @allure.step("Изменить количество книг в корзине")
    def change_book_in_cart(self, qwery: int) -> requests.Response:
        id_to_change = int(self.get_book_in_cart()["products"][0]["id"])
        body = [{
            "id": id_to_change,
            "quantity": qwery
        }]
        responses = requests.put(self.base_url + "cart", json=body, headers={"Authorization": "Bearer " + self.token})
        return responses

    @allure.step("Удалить книгу из корзины используя метод POST")
    def delete_book_in_cart_post(self) -> requests.Response:
        self.id_to_del = str(self.get_book_in_cart()["products"][0]["id"])
        responses = requests.post(
            self.base_url + "cart/product/" + self.id_to_del, headers={"Authorization": "Bearer " + self.token})
        return responses
