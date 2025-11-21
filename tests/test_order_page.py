import allure
import pytest

from data import DataOrder
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка заказа самоката через верхнюю кнопку')
    @pytest.mark.parametrize(DataOrder.param, DataOrder.value)
    def test_order_scooter_by_up_button(self, driver, name, surname, address, metro, phone, delivery_day, rental_period, color, comment):
        order = OrderPage(driver)
        order.click_button_order_up()
        order.set_order_scooter_info(name, surname, address, metro, phone)
        order.set_rental_info(delivery_day, rental_period, color, comment)
        assert 'Посмотреть статус' in order.find_status_button()


    @allure.title('Проверка заказа самоката через нижнюю кнопку')
    @pytest.mark.parametrize(DataOrder.param, DataOrder.value)
    def test_order_scooter_by_down_button(self, driver, name, surname, address, metro, phone, delivery_day, rental_period, color, comment):
        order = OrderPage(driver)
        order.click_button_order_down()
        order.set_order_scooter_info(name, surname, address, metro, phone)
        order.set_rental_info(delivery_day, rental_period, color, comment)
        assert 'Посмотреть статус' in order.find_status_button()
        