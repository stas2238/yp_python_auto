from .base_page import BasePage
from .locators import OrderPageLocators

class OrderPage(BasePage):
    def wait_for_order_page(self):
        self.wait_for_element_visible(OrderPageLocators.FIRST_NAME, timeout=5)

    def fill_order_form(self, data):
        self.fill(OrderPageLocators.FIRST_NAME, data["first_name"])
        self.fill(OrderPageLocators.LAST_NAME, data["last_name"])
        self.fill(OrderPageLocators.ADDRESS, data["address"])
        self.fill(OrderPageLocators.METRO_STATION, data["metro"])
        self.fill(OrderPageLocators.PHONE, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)
        self.fill(OrderPageLocators.DATE, data["date"])
        self.click(OrderPageLocators.RENT_DAYS)
        self.click(OrderPageLocators.RENT_DAYS_OPTION)
        if data.get("color") == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif data.get("color") == "grey":
            self.click(OrderPageLocators.COLOR_GREY)
        self.fill(OrderPageLocators.COMMENT, data.get("comment", ""))
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def wait_for_order_success_modal(self, timeout=5):
        self.wait_for_element_visible(OrderPageLocators.SUCCESS_MODAL, timeout)
