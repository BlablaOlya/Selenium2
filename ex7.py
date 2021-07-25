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
    menu_main = len(driver.find_elements_by_css_selector("#box-apps-menu a"))
    count = 0
    while count < menu_main:
        for m in range(1, menu_main + 1):
            main = f'li#app-:nth-child({m})'
            driver.find_element_by_css_selector(main).click()
            menu_second = len(driver.find_elements_by_xpath("//ul[@class='docs']/li/a"))
            count += 1
        if menu_second > 0:
            for s in range(1, menu_second + 1):
                second = main + f' li:nth-child({s})'
                driver.find_element_by_css_selector(second).click()
                assert driver.find_elements_by_css_selector("#content > h1")
        else:
            assert driver.find_elements_by_css_selector("#content > h1")

    # def test_login(driver):
    #     driver.get("http://localhost/litecart/admin/")
    #     driver.find_element_by_name("username").send_keys("admin")
    #     driver.find_element_by_name("password").send_keys("admin")
    #     driver.find_element_by_name("login").click()
    #     menu_main = driver.find_elements_by_css_selector("#box-apps-menu a")
    #     count = 0
    #     while count < len(menu_main):
    #         for m in range(1, len(menu_main) + 1):
    #             driver.find_element_by_css_selector(f'li#app-:nth-child({m})').click()
    #
    #             # driver.find_elements_by_css_selector("#box-apps-menu a")[m].click()
    #             # driver.find_elements_by_xpath("//li//a[@herf]")[m].click()
    #             # menu_second = driver.find_elements_by_xpath(f'.//ul/li[{m}]/ul/li')
    #             # menu_second = driver.find_elements_by_xpath("//li//span[@id='app-']")
    #             menu_second = driver.find_elements_by_xpath("//ul[@class='docs']/li/a")
    #             count += 1
    #             # menu_second = driver.find_elements_by_xpath(".//li//a[href]/a")
    #
    #             # menu_second = driver.find_elements_by_css_selector()
    #         if len(menu_second) > 0:
    #             for s in range(1, len(menu_second) + 1):
    #                 driver.find_element_by_css_selector(f' li:nth-child({s})').click()
    #                 # driver.find_elements_by_xpath(".//span[@class='name']")[s].click()
    #                 # driver.find_element_by_xpath(f'.//ul/li[{s}]/ul/li').click()
    #
    #                 assert driver.find_elements_by_css_selector("#content > h1")
    #         else:
    #             assert driver.find_elements_by_css_selector("#content > h1")
    # # count = 0
    # while count < menu:
    #     for i in range(menu):
    #         driver.find_elements_by_css_selector("#box-apps-menu a")[i].click()
    #         count += 1
    #     print(i)

    # all_elements_5 = driver.find_elements_by_xpath("//tr[@class='row']/td[5]/a")[element]
