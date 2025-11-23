from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, ".inventory_item button")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "select[data-test='product_sort_container']")

    def is_on_products_page(self):
        # simple check: products container exists
        return len(self.finds(self.INVENTORY_ITEM)) > 0

    def add_first_two_items_to_cart(self):
        buttons = self.finds(self.ADD_TO_CART_BUTTONS)
        buttons[0].click()
        buttons[1].click()

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_all_prices(self):
        prices = self.finds(self.ITEM_PRICE)
        return [float(p.text.replace("$", "")) for p in prices]

    def sort_low_to_high(self):
        from selenium.webdriver.support.ui import Select
        dropdown = self.find(self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value("lohi")  # low to high
