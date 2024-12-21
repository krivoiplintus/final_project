import json


my_data = open('test_data.json')
global_data = json.load(my_data)


class DataProvider:

    def __init__(self) -> None:
        self.data = global_data

    def get(self, property: str) -> str:
        return self.data.get(property)

    def getint(self, property: str) -> int:
        return int(self.data.get(property))

    def get_id_book(self) -> int:
        return self.data.get("id_book")

    def get_fake_id_book(self) -> int:
        return self.data.get("fake_id_book")

    def get_number_of_books(self) -> int:
        return self.data.get("number_of_books")

    def get_new_number_of_books(self) -> int:
        return self.data.get("new_number_of_books")

    def get_number(self) -> str:
        return self.data.get("number")

    def get_fake_number(self) -> str:
        return self.data.get("fake_number")

    def get_search_data(self) -> str:
        return self.data.get("search_data")

    def get_fake_search_data(self) -> str:
        return self.data.get("fake_search_data")
