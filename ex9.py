import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_sort_country(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    all_elements = len(driver.find_elements_by_xpath("//tr[@class='row']"))
    all_country = []
    for element in range(all_elements):
        all_elements_5 = driver.find_elements_by_xpath("//tr[@class='row']/td[5]/a")[element]
        all_country.append(all_elements_5.get_attribute("textContent"))
        all_elements_6 = driver.find_elements_by_xpath("//tr[@class='row']/td[6]")[element].text
        if int(all_elements_6) > 0:
            all_elements_5.click()
            # zone = len(driver.find_elements_by_xpath("//table[@class='dataTable']"))
            zone = len(driver.find_elements_by_css_selector('#table-zones tr'))
            zones = []
            for z in range(2, zone):
                # driver.find_elements_by_xpath(f"//*[@id='table-zones']/tbody/tr[{z}]/td[3]").text
                z_n = driver.find_element_by_xpath(f"//*[@id='table-zones']/tbody/tr[{z}]/td[3]").text
                zones.append(z_n)
            assert zones == sorted(zones)
            driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    assert all_country == sorted(all_country)


def test_sort_geo_zones(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    all_elements = len(driver.find_elements_by_xpath("//tr[@class='row']"))
    for element in range(all_elements):
        driver.find_element_by_xpath("//*[@class='row']/td[3]/a").click()
        zone = len(driver.find_elements_by_css_selector('#table-zones tr'))
        zones = []
        for z in range(2, zone):
            z_n = driver.find_element_by_xpath(f"//tr[{z}]/td[3]/select/option[@selected='selected']").text
            zones.append(z_n)
        assert zones == sorted(zones)
        driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')


