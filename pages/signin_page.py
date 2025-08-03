import allure
from data import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SignIn(BasePage):
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[text()='Создать аккаунт']")
    SIGNIN_FORM = (By.CSS_SELECTOR, "form.styles_form__2nwxz")
    EMAIL_INPUT = (By.XPATH, "//div[text()='Электронная почта']/parent::label/input")
    PASSWORD_INPUT = (By.XPATH, "//div[text()='Пароль']/parent::label/input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    @allure.step("Открываем страницу логина")
    def open(self):
        self.open_url(f"{BASE_URL}/signin")

    @allure.step("Кликаем по кнопке 'Создать аккаунт'")
    def click_create_account_button(self):
        self.click_element(self.CREATE_ACCOUNT_BUTTON)

    @allure.step("Проверяем, что форма для входа отображается")
    def is_signin_form_displayed(self):
        return self.wait_for_element(self.SIGNIN_FORM)
    
    def fill_email(self, email):
        email_input = self.wait_for_element(self.EMAIL_INPUT)
        email_input.send_keys(email)

    def fill_password(self, password):
        password_input = self.wait_for_element(self.PASSWORD_INPUT)
        password_input.send_keys(password)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    @allure.step("Авторизуемся")
    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()
