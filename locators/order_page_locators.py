from selenium.webdriver.common.by import By


class OrderLocators:

    # Верхняя кнопка заказа
    BUTTON_ORDER_UP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    # Нижняя кнопка заказа
    # BUTTON_ORDER_DOWN = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_ORDER_DOWN = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    # Поля ввода данных(первое меню)
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_ENTER = (By.XPATH, "//li[@class='select-search__row']")
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка Далее
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    
             # Оформление аренды(второе меню)
    # Дата
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Срок аренды
    RENTAL_PERIOD = (By.XPATH, "//span[@class='Dropdown-arrow']")
    # Комментарии
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    # Кнопка Заказать
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    
    # Кнопка ДА
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    
    # Кнопка Посмотреть статус
    VIEW_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
    
    
    # Возвращаем локатор срока аренды
    @staticmethod
    def period_locator(rental_period):
        return (By.XPATH, f"//div[text()='{rental_period}']")
    # Возвращаем локатор цвета самоката
    @staticmethod
    def color_locator(color):
        return (By.XPATH, f"//label[text()='{color}']")
    
