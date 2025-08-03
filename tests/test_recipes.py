from pages.signin_page import SignIn
from pages.recipes_page import Recipes
from pages.recipes_create_page import RecipesCreate
from data import BASE_URL, test_user, test_recipe
import random

class TestAccount:
    def test_create_recipe(self, driver):
        signin_page = SignIn(driver)
        signin_page.open()
        signin_page.login(email=test_user["email"], password=test_user["password"])

        recipes_page = Recipes(driver)
        recipes_page.wait_for_url_to_be(f"{BASE_URL}/recipes")
        recipes_page.click_create_recipe_button()
        
        recipe_creation_page = RecipesCreate(driver)
        recipe_creation_page.wait_for_url_to_be(f"{BASE_URL}/recipes/create")
        recipe_creation_page.fill_recipe_form(test_recipe["name"], test_recipe["ingredient"], test_recipe["ingredient_weight"], test_recipe["cooking_time"], test_recipe["description"], test_recipe["image_path"])
        assert recipes_page.is_recipe_card_displayed(), "Карточка рецепта не отображается после создания"
        assert recipes_page.is_recipe_name_displayed(test_recipe["name"]), "Имя рецепта не отображается на странице рецептов"
        assert recipes_page.get_recipe_name() == test_recipe["name"], "Имя рецепта не совпадает с ожидаемым"
        

