from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "word \"login\" not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "NO registration email input"
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "NO registration password input"
        password_input_1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_input_1.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "NO registration password confirm input"
        password_input_2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password_input_2.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "NO registration button"
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()