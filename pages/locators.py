from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_Form = (By.CSS_SELECTOR, "#login_form")
    LOGIN_Username = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_Password = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_Button = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name=\"login_submit\"]")
    REGISTRATION_Form = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_Username = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_Password1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_Password2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_Button = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[name=\"registration_submit\"]")
