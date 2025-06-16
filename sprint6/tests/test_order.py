import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

order_data_sets = [
    {
        "first_name": "Иван",
        "last_name": "Иванов",
        "address": "Москва, ул. Ленина, 1",
        "metro": "Черкизовская",
        "phone": "+79998887766",
        "date": "10.06.2025",
        "color": "black",
        "comment": "Позвонить за час"
    },
    {
        "first_name": "Анна",
        "last_name": "Петрова",
        "address": "Санкт-Петербург, Невский пр., 10",
        "metro": "Площадь Восстания",
        "phone": "+79991112233",
        "date": "11.06.2025",
        "color": "grey",
        "comment": ""
    }
]

@pytest.mark.parametrize("button", ["top", "bottom"])
@pytest.mark.parametrize("order_data", order_data_sets)
def test_order_flow(driver, button, order_data):
    main_page = MainPage(driver)
    main_page.open()
    main_page.wait_for_load_home_page()
    if button == "top":
        main_page.click_order_button_top()
    else:
        main_page.click_order_button_bottom()
    order_page = OrderPage(driver)
    order_page.wait_for_order_page()
    order_page.fill_order_form(order_data)
    order_page.wait_for_order_success_modal()
