from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scooter_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_order_button_top()
    main_page.click_scooter_logo()
    WebDriverWait(driver, 5).until(EC.url_to_be(main_page.URL))
    assert driver.current_url == main_page.URL

def test_yandex_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_yandex_logo()
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(lambda d: "dzen.ru" in d.current_url)
    assert "dzen.ru" in driver.current_url
