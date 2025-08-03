import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Recipes(BasePage):
    EXIT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//a[text()='Создать рецепт']")
    RECIPE_CARD = (By.XPATH, "//div[@class='styles_single-card__1yTTj']")
    RECIPE_NAME = (By.XPATH, "//h1[contains(@class, 'single-card__title')]")

    @allure.step("Проверяем, что кнопка 'Выйти' отображается")
    def is_exit_button_displayed(self):
        return self.wait_for_element(self.EXIT_BUTTON)
    
    @allure.step("Кликаем по кнопке 'Создать рецепт'")
    def click_create_recipe_button(self):
        self.click_element(self.CREATE_RECIPE_BUTTON)

    @allure.step("Проверяем, что карточка рецепта отображается")
    def is_recipe_card_displayed(self):
        return self.wait_for_element(self.RECIPE_CARD)
    
    @allure.step("Проверяем, что имя рецепта отображается")
    def is_recipe_name_displayed(self, recipe_name):
        return self.wait_for_text_to_be_present_in_element(self.RECIPE_NAME, recipe_name)

    @allure.step("Получаем имя рецепта")
    def get_recipe_name(self):
        self.wait_for_element(self.RECIPE_NAME)
        return self.get_element_text(self.RECIPE_NAME)
