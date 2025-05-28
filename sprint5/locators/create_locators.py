from selenium.webdriver.common.by import By

PLACE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
LOGIN_MODAL_TITLE = (By.XPATH, "//div[contains(@class, 'modal')]//h2[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]")

AD_TITLE_INPUT = (By.NAME, "title")
AD_DESC_INPUT = (By.NAME, "description")
AD_PRICE_INPUT = (By.NAME, "price")
AD_CATEGORY_DROPDOWN = (By.NAME, "category")
AD_CITY_DROPDOWN = (By.NAME, "city")
AD_STATE_NEW_RADIO = (By.XPATH, "//input[@type='radio' and @value='new']")
AD_STATE_USED_RADIO = (By.XPATH, "//input[@type='radio' and @value='used']")
AD_PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(),'Опубликовать')]")

PROFILE_BUTTON = (By.XPATH, "//a[contains(@href, '/profile')]")
MY_ADS_BLOCK = (By.XPATH, "//div[contains(@class, 'my-ads')]")
AD_TITLE_IN_LIST = (By.XPATH, "//div[contains(@class, 'my-ads')]//div[contains(@class, 'ad-title')]")