from locators.registration_locators import *
from utils import generate_email

class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        email = generate_email()
        driver.find_element(*REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REG_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*REG_REPEAT_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        assert driver.find_element(*USER_AVATAR).is_displayed()
        assert driver.find_element(*USER_NAME).is_displayed()

    def test_registration_invalid_email(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        driver.find_element(*REG_EMAIL_INPUT).send_keys("invalidemail")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        assert driver.find_element(*REG_EMAIL_ERROR).is_displayed()
        assert driver.find_element(*REG_PASSWORD_ERROR).is_displayed()
        assert driver.find_element(*REG_REPEAT_PASSWORD_ERROR).is_displayed()
        assert driver.find_element(*REG_EMAIL_ERROR).text == "Ошибка"

    def test_registration_existing_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()
        driver.find_element(*REG_EMAIL_INPUT).send_keys("testuser@mail.com")
        driver.find_element(*REG_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*REG_REPEAT_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()
        assert driver.find_element(*REG_EMAIL_ERROR).is_displayed()
        assert driver.find_element(*REG_PASSWORD_ERROR).is_displayed()
        assert driver.find_element(*REG_REPEAT_PASSWORD_ERROR).is_displayed()
        assert driver.find_element(*REG_EMAIL_ERROR).text == "Ошибка"
