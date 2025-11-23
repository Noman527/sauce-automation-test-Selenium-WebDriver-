from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_TEXT = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def fill_checkout_info(self, first, last, postal):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_TEXT)

    def is_cart_empty(self):
        # after checkout, cart badge usually disappears
        from selenium.common.exceptions import TimeoutException
        try:
            self.find(self.CART_BADGE)
            return False
        except TimeoutException:
            return True
