from .base_page import BasePage
from .locators import BasketPageLocators

EMPTY_TEXT = "Your basket is empty."

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT)
        basket_text = basket_message.text
        assert EMPTY_TEXT in basket_text, "Wrong empty basket text"

