import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_product(driver):
    driver.get('http://localhost/litecart/en/')
    main_page_product = driver.find_element_by_xpath("//div[@id='box-campaigns']//ul[@class='listing-wrapper products']//li")
    # имя товара на гл стр
    product_name = main_page_product.find_element_by_xpath(".//div[@class='name']").text
    regular_price = main_page_product.find_element_by_xpath(".//s[@class='regular-price']")
    campaign_price = main_page_product.find_element_by_xpath(".//strong[@class='campaign-price']")
    # обычная цена товара на гл стр
    text_regular_price = regular_price.text
    # скидочная цена на гл стр
    text_campaign_price = campaign_price.text
    # цвет обычной цены на гл стр
    grey_color =[]
    color_product_regular_price = regular_price.value_of_css_property('text-decoration-color')
    grey_color.append(color_product_regular_price)
    assert color_product_regular_price in grey_color
    # цвет скидочной цены на гл стр
    red_color = []
    color_product_campaign_price = campaign_price.value_of_css_property('text-decoration-color')
    red_color.append(color_product_campaign_price)
    assert color_product_campaign_price in red_color
    # резмер текста обычной цена товара на гл стр
    size_product_regular_price = regular_price.value_of_css_property('font-size')
    # резмер текста скидочной цена товара на гл стр
    size_product_campaign_price = campaign_price.value_of_css_property('font-size')
    assert size_product_campaign_price > size_product_regular_price
    # обычная цена зачеркнута
    line_product_regular_price = regular_price.value_of_css_property('text-decoration-line')
    assert line_product_regular_price == 'line-through'
    # вес скидочной цены
    weight_product_campaign_price = campaign_price.value_of_css_property('font-weight')
    # click() на страницу
    main_page_product.click()
    # имя товара по ссылке
    page_product_name = driver.find_element_by_xpath(".//*[@id='box-product']/div[1]/h1").text
    assert product_name == page_product_name
    page = driver.find_element_by_xpath("//div[@class='information']")
    page_regular_price = page.find_element_by_xpath(".//s[@class='regular-price']")
    page_campaign_price = page.find_element_by_xpath(".//strong[@class='campaign-price']")
    text_page_regular_price = page_regular_price.text
    assert text_regular_price == text_page_regular_price
    text_page_campaign_price = page_campaign_price.text
    assert text_campaign_price == text_page_campaign_price
    color_page_regular_price = page_regular_price.value_of_css_property('text-decoration-color')
    grey_color.append(color_page_regular_price)
    assert color_page_regular_price in grey_color
    color_page_campaign_price = page_campaign_price.value_of_css_property('text-decoration-color')
    red_color.append(color_page_campaign_price)
    assert color_page_campaign_price in red_color
    size_page_campaign_price = page_campaign_price.value_of_css_property('font-size')
    size_page_regular_price = page_regular_price.value_of_css_property('font-size')
    assert size_page_campaign_price > size_page_regular_price
    line_page_regular_price = page_regular_price.value_of_css_property('text-decoration-line')
    assert line_page_regular_price == 'line-through'


