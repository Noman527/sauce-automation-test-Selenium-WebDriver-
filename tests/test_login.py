from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_successful_login(driver, base_url, config):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.open_login_page(base_url)
    login_page.login(config["username"], config["password"])

    assert products_page.is_on_products_page()

def test_unsuccessful_login_invalid_password(driver, base_url, config):
    login_page = LoginPage(driver)

    login_page.open_login_page(base_url)
    login_page.login(config["username"], "wrong_password")

    error = login_page.get_error_message()
    assert "Username and password do not match" in error or "do not match" in error
