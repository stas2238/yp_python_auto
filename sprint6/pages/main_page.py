from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    def open(self):
        self.open_url(self.URL)

    def wait_for_load_home_page(self):
        self.wait_for_element_visible(MainPageLocators.SCOOTER_LOGO, timeout=5)

    def click_order_button_top(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    def click_order_button_bottom(self):
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def click_question(self, question_id):
        self.click(MainPageLocators.QUESTION(question_id))

    def wait_for_question_answer_visible(self, question_id, timeout=5):
        self.wait_for_element_visible(MainPageLocators.ANSWER(question_id), timeout)

    def get_answer_text(self, question_id):
        return self.get_text(MainPageLocators.ANSWER(question_id))

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def wait_for_main_url(self, timeout=5):
        self.wait_for_url(self.URL, timeout)

    def is_main_url(self):
        return self.is_url(self.URL)
