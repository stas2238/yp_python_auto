from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators

class MainPage:
    URL = "https://qa-scooter.praktikum-services.ru/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_order_button_top(self):
        self.driver.find_element(*MainPageLocators.TOP_ORDER_BUTTON).click()

    def click_order_button_bottom(self):
        self.driver.find_element(*MainPageLocators.BOTTOM_ORDER_BUTTON).click()

    def click_question(self, question_id):
        self.driver.find_element(*MainPageLocators.QUESTION(question_id)).click()

    def get_answer_text(self, question_id):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ANSWER(question_id))
        ).text

    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()
