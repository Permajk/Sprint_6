import allure

from locators.main_page_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик на логотип Самоката')
    def click_on_logo_scooter(self):
        self.click_on_element(MainLocators.LOGO_SCOOTER)

    @allure.step('Клик на логотип Яндекса и переход на Дзен')
    def click_on_logo_yandex_and_go_to_dzen(self):
        self.click_on_element(MainLocators.LOGO_YANDEX)

    @allure.step('Получаем текст раздела Новости со страницы Дзен')
    def get_dzen_news_text(self):
        return self.get_text_on_element(MainLocators.DZEN_NEWS_TEXT)
        
    @allure.step('Клик по верхней кнопке заказа')
    def click_order_up(self):
        self.click_on_element(MainLocators.BUTTON_ORDER_UP)

    @allure.step('Скролл к разделу FAQ')
    def scroll_to_faq(self):
        self.scroll_to_element(MainLocators.FAQ_SECTION)

    @allure.step('Получаем текст вопроса и ответ по локаторам')
    def get_question_and_answer(self, number):
        self.scroll_to_faq()
        question_loc = MainLocators.FAQ_QUESTIONS[number]
        answer_loc = MainLocators.FAQ_ANSWERS[number]
        question_text = self.get_text_on_element(question_loc)
        self.click_on_element(question_loc)
        answer_text = self.get_text_on_element(answer_loc)
        return question_text, answer_text
    
