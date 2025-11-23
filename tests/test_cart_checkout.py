from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_add_to_cart_and_checkout(driver, base_url, config):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Login
    login_page.open_login_page(base_url)
    login_page.login(config["username"], config["password"])

    # Add items
    products_page.add_first_two_items_to_cart()
    products_page.go_to_cart()

    # Verify cart
    assert cart_page.get_cart_items_count() == 2

    # Checkout
    cart_page.click_checkout()
    checkout_page.fill_checkout_info("Test", "User", "12345")
    checkout_page.finish_checkout()

    # Verify success
    success_msg = checkout_page.get_success_message()
    assert "Thank you" in success_msg

    # Verify cart empty
    assert checkout_page.is_cart_empty()
