from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        self.wait_for_element_clickable(locator, timeout).click()

    def fill(self, locator, value, timeout=10):
        el = self.wait_for_element_visible(locator, timeout)
        el.clear()
        el.send_keys(value)

    def get_text(self, locator, timeout=10):
        return self.wait_for_element_visible(locator, timeout).text

    def is_url(self, url):
        return self.driver.current_url == url

    def switch_to_tab(self, tab_index):
        self.driver.switch_to.window(self.driver.window_handles[tab_index])
