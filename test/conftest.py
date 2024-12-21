import allure
import pytest
from selenium import webdriver
from configyration.config_provider import ConfigProvider


@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicitly_wait(ConfigProvider().get_ui_timeout())
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()
