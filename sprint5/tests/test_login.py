from locators.login_locators import *

class TestLogin:
    def test_successful_login(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("testuser@mail.com")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*LOGIN_BUTTON).click()
        assert driver.find_element(*USER_AVATAR).is_displayed()
        assert driver.find_element(*USER_NAME).is_displayed()
