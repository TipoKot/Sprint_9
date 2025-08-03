from pages.signin_page import SignIn
from pages.signup_page import SignUp
from pages.recipes_page import Recipes
from data import BASE_URL, test_user
import random

class TestAccount:
    def test_create_account(self, driver):
        signin_page = SignIn(driver)
        signin_page.open()
        signin_page.click_create_account_button()

        signup_page = SignUp(driver)

        name = "Ivan"
        last_name = "Ivanov"
        login = f"ivanov{random.randint(1000, 9999)}"
        email = f"user{random.randint(1000, 9999)}@example.com"
        password = f"Password{random.randint(1000, 9999)}"

        signup_page.fill_registration_form(name, last_name, login, email, password)
        signup_page.click_create_account_button()
        signup_page.wait_for_url_to_be(f"{BASE_URL}/signin")

        assert f"{BASE_URL}/signin" in signin_page.get_current_url(), "Не удалось перейти на страницу входа после создания аккаунта"
        assert signin_page.is_signin_form_displayed(), "Форма входа не отображается после создания аккаунта"
    
    def test_login(self, driver):
        signin_page = SignIn(driver)
        signin_page.open()

        signin_page.login(email=test_user["email"], password=test_user["password"])

        recipes_page = Recipes(driver)
        recipes_page.wait_for_url_to_be(f"{BASE_URL}/recipes")

        assert f"{BASE_URL}/recipes" in signin_page.get_current_url(), "Не удалось авторизоваться после создания аккаунта"
        assert recipes_page.is_exit_button_displayed(), "Кнопка 'Выйти' не отображается после авторизации"
