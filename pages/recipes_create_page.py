import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RecipesCreate(BasePage):
    NAME_INPUT = (By.XPATH, "//div[text()='Название рецепта']/parent::label/input")
    INGREDIENT_INPUT = (By.XPATH, "//div[text()='Ингредиенты']/parent::label/input")
    INGREDIENT_DROPDOWN = (By.XPATH, "//div[@class='styles_container__3ukwm']")
    INGREDIENT_WEIGHT_INPUT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    COOKING_TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/parent::label/input")
    DESCRIPTION_INPUT = (By.XPATH, "//div[text()='Описание рецепта']/parent::label/textarea")
    UPLOAD_IMAGE_BUTTON = (By.XPATH, "//input[@type='file']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")

    @allure.step("Заполняем поле 'Название рецепта'")
    def fill_name(self, name):
        input_field = self.wait_for_element(self.NAME_INPUT)
        input_field.send_keys(name)

    @allure.step("Заполняем ингредиент")
    def fill_ingredient(self, ingredient):
        input_field = self.wait_for_element(self.INGREDIENT_INPUT)
        input_field.send_keys(ingredient)
        self.click_element(self.INGREDIENT_DROPDOWN)

    @allure.step("Заполняем количество ингредиента")
    def fill_ingredient_weight(self, weight):
        input_field = self.wait_for_element(self.INGREDIENT_WEIGHT_INPUT)
        input_field.send_keys(weight)

    @allure.step("Кликаем по кнопке 'Добавить ингредиент'")
    def click_add_ingredient_button(self):
        self.click_element(self.ADD_INGREDIENT_BUTTON)

    @allure.step("Заполняем время приготовления")
    def fill_cooking_time(self, time):
        input_field = self.wait_for_element(self.COOKING_TIME_INPUT)
        input_field.send_keys(time)

    @allure.step("Заполняем описание рецепта")
    def fill_description(self, description):
        input_field = self.wait_for_element(self.DESCRIPTION_INPUT)
        input_field.send_keys(description)

    @allure.step("Загружаем изображение рецепта")
    def upload_image(self, image_path):
        upload_button = self.wait_for_element(self.UPLOAD_IMAGE_BUTTON)
        upload_button.send_keys(image_path)

    @allure.step("Кликаем по кнопке 'Создать рецепт'")
    def click_create_recipe_button(self):
        self.click_element(self.CREATE_RECIPE_BUTTON)

    @allure.step("Создаем рецепт")
    def fill_recipe_form(self, name, ingredient, weight, time, description, image_path):
        self.fill_name(name)
        self.fill_ingredient(ingredient)
        self.fill_ingredient_weight(weight)
        self.click_add_ingredient_button()
        self.fill_cooking_time(time)
        self.fill_description(description)
        self.upload_image(image_path)
        self.click_create_recipe_button()