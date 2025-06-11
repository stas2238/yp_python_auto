import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install(),
        options=options
    )
    yield driver
    driver.quit()
