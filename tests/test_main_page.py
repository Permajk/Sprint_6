import allure
import pytest

from data import Urls, DataFAQ
from pages.main_page import MainPage


class TestMainPage:
    
    @allure.title('Переход на главную страницу по логотипу Самоката')
    def test_go_on_logo_scooter(self, driver):
        main = MainPage(driver)
        main.click_order_up()
        main.click_on_logo_scooter()
        assert main.get_current_url() == Urls.main_paige
            
    @allure.title('Переход на страницу Дзен по логотипу Яндекс')
    def test_logo_yandex_go_to_dzen(self, driver):
        main = MainPage(driver)
        main.click_on_logo_yandex_and_go_to_dzen()
        main.change_browser_tab()
        main.get_dzen_news_text()
        assert main.get_current_url() == Urls.dzen_paige

    @allure.title('Проверка выпадающего списка')
    @pytest.mark.parametrize(DataFAQ.param, DataFAQ.value)
    def test_question_and_answer(self, driver, number, expected_answer):
        main = MainPage(driver)
        question_text, answer_text = main.get_question_and_answer(number)
        assert answer_text == expected_answer

