from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import OrderPageLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_order_form(self, data):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME).send_keys(data["first_name"])
        self.driver.find_element(*OrderPageLocators.LAST_NAME).send_keys(data["last_name"])
        self.driver.find_element(*OrderPageLocators.ADDRESS).send_keys(data["address"])
        self.driver.find_element(*OrderPageLocators.METRO_STATION).send_keys(data["metro"])
        self.driver.find_element(*OrderPageLocators.PHONE).send_keys(data["phone"])
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

        self.driver.find_element(*OrderPageLocators.DATE).send_keys(data["date"])
        self.driver.find_element(*OrderPageLocators.RENT_DAYS).click()
        self.driver.find_element(*OrderPageLocators.RENT_DAYS_OPTION).click()
        if data.get("color") == "black":
            self.driver.find_element(*OrderPageLocators.COLOR_BLACK).click()
        elif data.get("color") == "grey":
            self.driver.find_element(*OrderPageLocators.COLOR_GREY).click()
        self.driver.find_element(*OrderPageLocators.COMMENT).send_keys(data.get("comment", ""))
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()
        self.driver.find_element(*OrderPageLocators.CONFIRM_YES_BUTTON).click()

    def is_order_successful(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL)
        )
