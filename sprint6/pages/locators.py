from selenium.webdriver.common.by import By

class MainPageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')][1]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')][2]")
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    QUESTION = lambda qid: (By.ID, f"accordion__heading-{qid}")
    ANSWER = lambda qid: (By.ID, f"accordion__panel-{qid}")

class OrderPageLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.CLASS_NAME, "select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DAYS = (By.CLASS_NAME, "Dropdown-placeholder")
    RENT_DAYS_OPTION = (By.XPATH, "//div[@class='Dropdown-menu']/div[1]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать') and not(ancestor::div[contains(@class, 'Order_NextButton')])]")
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
