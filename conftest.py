import pytest
import data
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    data.browser_name = "Chrome"
    driver = webdriver.Chrome()
    yield driver
    driver.quit()