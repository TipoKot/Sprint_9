import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.browser_version = "114.0"

    # Стандартные W3C-capabilities
    chrome_options.set_capability("browserName", "chrome")

    # Selenoid-specific capabilities
    chrome_options.set_capability("selenoid:options", {
        "enableVNC": True,
        # "enableVideo": True,  # если нужно
    })

    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        options=chrome_options
    )
    yield driver
    driver.quit()
