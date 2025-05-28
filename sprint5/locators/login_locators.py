from selenium.webdriver.common.by import By

LOGIN_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
LOGIN_EMAIL_INPUT = (By.NAME, "email")
LOGIN_PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

USER_AVATAR = (By.XPATH, "//div[contains(@class, 'user-avatar')]")
USER_NAME = (By.XPATH, "//div[contains(@class, 'user-name') and contains(text(), 'User')]")