import pytest
from selenium.webdriver.common.by import By

def test_add_to_cart_button_exists(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена на странице"
