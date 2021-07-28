import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


emails = ["blabla11", "blabla22", "blabla33", "blabla44", "blabla55"]
domain = ["@mail.ru", "@gmail.com", "@hotmail.com", "@yandex.ru"]


def test_registration(driver):
    driver.get('http://localhost/litecart/en/')
    driver.find_element_by_link_text("New customers click here").click()
    driver.find_element_by_name("tax_id").send_keys("1")
    driver.find_element_by_name("company").send_keys("company#1")
    driver.find_element_by_name("firstname").send_keys("Blablaolya")
    driver.find_element_by_name("lastname").send_keys("Popova")
    driver.find_element_by_name("address1").send_keys("address#1")
    driver.find_element_by_name("address2").send_keys("address#2")
    driver.find_element_by_name("postcode").send_keys("11111")
    driver.find_element_by_name("city").send_keys("NY")
    driver.find_element_by_css_selector("[role='combobox']").click()
    driver.find_element_by_css_selector(".select2-results__option[id $= US]").click()
    zone_code = []
    zones = driver.find_elements_by_xpath("//select[@name='zone_code']/option")
    for z in zones:
        zone_code.append(z.get_attribute("value"))
    Select(driver.find_element_by_css_selector("select[name=zone_code]")).select_by_value(random.choice(zone_code))
    email = random.choice(emails) + random.choice(domain)
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("phone").send_keys("000000000")
    password = "01"
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("confirmed_password").send_keys(password)
    driver.find_element_by_name("create_account").click()
    driver.find_element_by_link_text("Logout").click()
    fill_element(driver, "email", email)
    fill_element(driver, "password", password)
    driver.find_element_by_name("login").click()
    driver.find_element_by_link_text("Logout").click()


def fill_element(driver, element_name, value):
    driver.find_element_by_name(element_name).click()
    driver.find_element_by_name(element_name).clear()
    driver.find_element_by_name(element_name).send_keys(value)
