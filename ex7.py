import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    menu = len(driver.find_elements_by_css_selector("#box-apps-menu a"))
    count = 0
    while count < menu:
        for i in range(menu):
            driver.find_elements_by_css_selector("#box-apps-menu a")[i].click()
            count += 1
