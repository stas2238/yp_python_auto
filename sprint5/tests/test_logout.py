from locators.logout_locators import *
from locators.login_locators import *

class TestLogout:
    def test_logout(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("testuser@mail.com")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*USER_MENU_BUTTON).click()
        driver.find_element(*LOGOUT_BUTTON).click()
        assert driver.find_element(*LOGIN_REGISTRATION_BUTTON).is_displayed()
