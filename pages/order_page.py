import allure

from locators.order_page_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Клик по верхней кнопке заказа')
    def click_button_order_up(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER_UP)

    @allure.step('Клик по нижней кнопке заказа')
    def click_button_order_down(self):
        self.scroll_to_element(OrderLocators.BUTTON_ORDER_DOWN)
        self.click_on_element(OrderLocators.BUTTON_ORDER_DOWN)    

    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        self.send_keys_to_input(OrderLocators.NAME, name) 

    @allure.step('Заполняем поле Фамилия')
    def set_surname(self, surname):
        self.send_keys_to_input(OrderLocators.SURNAME, surname)

    @allure.step('Заполняем поле Адрес')
    def set_address(self, address):
        self.send_keys_to_input(OrderLocators.ADDRESS, address)

    @allure.step('Заполняем поле Станция метро')
    def set_metro_station(self, metro):
        self.click_on_element(OrderLocators.METRO)
        self.send_keys_to_input(OrderLocators.METRO, metro)
        self.click_on_element(OrderLocators.METRO_ENTER)

    @allure.step('Заполняем поле Номер телефона')
    def set_phone_number(self, phone):
        self.send_keys_to_input(OrderLocators.TELEPHONE, phone)

    @allure.step('Кликаем кнопку далее')
    def click_button_next(self):
        self.click_on_element(OrderLocators.BUTTON_NEXT)

    @allure.step('Выбираем дату доставки')
    def set_delivery_date(self, delivery_day):
        self.send_keys_to_input(OrderLocators.DATE, delivery_day)

    @allure.step('Заполняем поле Срок Аренды')
    def set_rental_period(self, rental_period):
        self.click_on_element(OrderLocators.RENTAL_PERIOD)
        self.click_on_element(OrderLocators.period_locator(rental_period))

    @allure.step('Выбираем цвет самоката')
    def set_color_scooter(self, color):
        self.click_on_element(OrderLocators.color_locator(color))

    @allure.step('Заполняем комментарий')
    def set_commentary(self, comment):
        self.send_keys_to_input(OrderLocators.COMMENT, comment)

    @allure.step('Кликаем кнопку Заказать')
    def click_button_order(self):
        self.click_on_element(OrderLocators.BUTTON_ORDER)

    @allure.step('Подтверждаем заказ - Да')
    def click_button_yes(self):
        self.click_on_element(OrderLocators.BUTTON_YES)

    @allure.step('Получаем текст кнопки Посмотреть статус')
    def find_status_button(self):
        return self.get_text_on_element(OrderLocators.VIEW_STATUS)

    @allure.step('Заполняем информацию Для кого самокат')
    def set_order_scooter_info(self, name, surname, address, metro, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(metro)
        self.set_phone_number(phone)
        self.click_button_next()

    @allure.step('Заполняем информацию о периоде аренды')
    def set_rental_info(self, delivery_day, rental_period, color, comment):
        self.set_delivery_date(delivery_day)
        self.set_rental_period(rental_period)
        self.set_color_scooter(color)
        self.set_commentary(comment)
        self.click_button_order()
        self.click_button_yes()
        self.find_status_button()
        
