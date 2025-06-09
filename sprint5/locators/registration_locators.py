from selenium.webdriver.common.by import By

LOGIN_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")

REG_EMAIL_INPUT = (By.NAME, "email")
REG_PASSWORD_INPUT = (By.NAME, "password")
REG_REPEAT_PASSWORD_INPUT = (By.NAME, "confirmPassword")

REG_EMAIL_ERROR = (By.XPATH, "//input[@name='email']/following-sibling::div[contains(@class, 'error')]")
REG_PASSWORD_ERROR = (By.XPATH, "//input[@name='password']/following-sibling::div[contains(@class, 'error')]")
REG_REPEAT_PASSWORD_ERROR = (By.XPATH, "//input[@name='confirmPassword']/following-sibling::div[contains(@class, 'error')]")

USER_AVATAR = (By.XPATH, "//div[contains(@class, 'user-avatar')]")
USER_NAME = (By.XPATH, "//div[contains(@class, 'user-name') and contains(text(), 'User')]")