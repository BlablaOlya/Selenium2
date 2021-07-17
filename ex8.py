import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_stic(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/")
    products = len(driver.find_elements_by_css_selector(".image-wrapper"))
    print(products, "товаров")
    stickers = len(driver.find_elements_by_class_name("sticker"))
    print(stickers, "стикеров")
    count = 0
    while count < products:
        for i in range(products):
            driver.find_elements_by_css_selector('.sticker')[i]
            print(f"на товаре {i} - один стикер")
            count += 1
    assert products == stickers, f"{products} товаров и {stickers} стикеров должны совпадать"
