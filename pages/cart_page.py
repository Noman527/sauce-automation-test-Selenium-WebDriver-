from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items_count(self):
        return len(self.finds(self.CART_ITEM))

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
