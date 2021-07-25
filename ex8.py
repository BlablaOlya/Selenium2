import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_stic(driver):
    driver.get("http://localhost/litecart/")
    products = driver.find_elements_by_css_selector(".image-wrapper")
    print(len(products), "товаров")

    count = 0
    while count < len(products):
        for i in products:
            sticker = i.find_elements_by_xpath(".//div[starts-with(@class,'sticker')]")
            count += len(sticker)
            # print(count)
    assert len(products) == count, f"{products} товаров и {count} стикеров должны совпадать"
