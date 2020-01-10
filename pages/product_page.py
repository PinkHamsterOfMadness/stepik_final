from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        message_success_text = self.browser.find_element(*ProductPageLocators.ALERT_NAME_PRODUCT).text
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert message_success_text == product_name, "Product name in message is wrong"
        message_price_text = self.browser.find_element(*ProductPageLocators.ALERT_PRICE_PRODUCT).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert message_price_text == product_price, "Product price in message is wrong"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_success_message_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_NAME_PRODUCT)

    def is_success_message_disapeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_NAME_PRODUCT)