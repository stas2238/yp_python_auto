from locators.create_locators import *
from locators.login_locators import *

class TestAdCreation:
    def test_create_ad_not_authorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*PLACE_AD_BUTTON).click()
        assert driver.find_element(*LOGIN_MODAL_TITLE).is_displayed()

    def test_create_ad_authorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTRATION_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("testuser@mail.com")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("Qwerty123!")
        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*PLACE_AD_BUTTON).click()
        driver.find_element(*AD_TITLE_INPUT).send_keys("Test Ad")
        driver.find_element(*AD_DESC_INPUT).send_keys("Test Description")
        driver.find_element(*AD_PRICE_INPUT).send_keys("1000")
        driver.find_element(*AD_CATEGORY_DROPDOWN).click()
        driver.find_element_by_xpath("//option[2]").click()
        driver.find_element(*AD_CITY_DROPDOWN).click()
        driver.find_element_by_xpath("//option[2]").click()
        driver.find_element(*AD_STATE_NEW_RADIO).click()
        driver.find_element(*AD_PUBLISH_BUTTON).click()
        driver.find_element(*PROFILE_BUTTON).click()
        assert driver.find_element(*MY_ADS_BLOCK).is_displayed()
        assert driver.find_element(*AD_TITLE_IN_LIST).text == "Test Ad"
