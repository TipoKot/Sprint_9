from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def wait_for_url_to_be(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(expected_url)
        )

    def get_current_url(self):
        return self.driver.current_url
    
    def wait_for_text_to_be_present_in_element(self, locator, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text