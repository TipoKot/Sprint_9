import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SignUp(BasePage):
    
    NAME_INPUT = (By.XPATH, "//div[text()='Имя']/parent::label/input")
    
    LAST_NAME_INPUT = (By.XPATH, "//div[text()='Фамилия']/parent::label/input")
    LOGIN_INPUT = (By.XPATH, "//div[text()='Имя пользователя']/parent::label/input")
    EMAIL_INPUT = (By.XPATH, "//div[text()='Адрес электронной почты']/parent::label/input")
    PASSWORD_INPUT = (By.XPATH, "//div[text()='Пароль']/parent::label/input")
    СREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")

    @allure.step("Заполняем поле 'Имя'")
    def fill_name(self, name):
        input_field = self.wait_for_element(self.NAME_INPUT)
        input_field.send_keys(name)

    @allure.step("Заполняем поле 'Фамилия'")
    def fill_last_name(self, last_name):
        input_field = self.wait_for_element(self.LAST_NAME_INPUT)
        input_field.send_keys(last_name)

    @allure.step("Заполняем поле 'Имя пользователя'")
    def fill_login(self, login):
        input_field = self.wait_for_element(self.LOGIN_INPUT)
        input_field.send_keys(login)

    @allure.step("Заполняем поле 'Email'")
    def fill_email(self, email):
        input_field = self.wait_for_element(self.EMAIL_INPUT)
        input_field.send_keys(email)

    @allure.step("Заполняем поле 'Пароль'")
    def fill_password(self, password):
        input_field = self.wait_for_element(self.PASSWORD_INPUT)
        input_field.send_keys(password)

    @allure.step("Заполняем форму регистрации")
    def fill_registration_form(self, name, last_name, login, email, password):
        self.fill_name(name)
        self.fill_last_name(last_name)
        self.fill_login(login)
        self.fill_email(email)
        self.fill_password(password)

    @allure.step("Кликаем по кнопке 'Создать аккаунт'")
    def click_create_account_button(self):
        self.click_element(self.СREATE_ACCOUNT_BUTTON)
