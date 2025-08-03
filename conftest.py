import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.browser_version = "114.0"
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("enableVNC", True)  # если надо видеть браузер в UI
    # chrome_options.set_capability("enableVideo", True)  # если хочешь видео

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=chrome_options
    )
    yield driver
    driver.quit()
