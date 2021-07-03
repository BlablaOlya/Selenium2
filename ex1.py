import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome('/Users/olgapo/chromedriver')
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://www.mvideo.ru/")
