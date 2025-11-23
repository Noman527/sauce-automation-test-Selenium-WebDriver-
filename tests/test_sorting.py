from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import os

def test_sort_low_to_high(driver, base_url, config):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.open_login_page(base_url)
    login_page.login(config["username"], config["password"])

    # Get prices before sort (not necessary, but possible)
    products_page.sort_low_to_high()
    prices = products_page.get_all_prices()

    sorted_prices = sorted(prices)
    assert prices == sorted_prices

    # Screenshot of sorted page
    os.makedirs("reports/screenshots", exist_ok=True)
    driver.save_screenshot("reports/screenshots/sorted_low_to_high.png")
