from pages.main_page import MainPage

def test_scooter_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.wait_for_load_home_page()
    main_page.click_order_button_top()
    main_page.click_scooter_logo()
    main_page.wait_for_main_url()
    assert main_page.is_main_url()

def test_yandex_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.wait_for_load_home_page()
    main_page.click_yandex_logo()
    main_page.switch_to_tab(1)
    current_url = main_page.get_current_url()
    assert "dzen.ru" in current_url
