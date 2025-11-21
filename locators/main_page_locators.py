from selenium.webdriver.common.by import By


class MainLocators:

    # Логотипы
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
    LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")

    # Дзен Новости
    DZEN_NEWS_TEXT = (By.XPATH, "//div[text()='Новости']")

    # Верхняя кнопка заказа
    BUTTON_ORDER_UP = (By.XPATH, "//button[@class='Button_Button__ra12g']")

    # Разрел FAQ
    FAQ_SECTION = (By.XPATH, "//div[@class='Home_FAQ__3uVm4']")

    # Вопросы FAQ
    FAQ_QUESTIONS = {
        0: (By.XPATH, "//div[@id='accordion__heading-0']"),
        1: (By.XPATH, "//div[@id='accordion__heading-1']"),
        2: (By.XPATH, "//div[@id='accordion__heading-2']"),
        3: (By.XPATH, "//div[@id='accordion__heading-3']"),
        4: (By.XPATH, "//div[@id='accordion__heading-4']"),
        5: (By.XPATH, "//div[@id='accordion__heading-5']"),
        6: (By.XPATH, "//div[@id='accordion__heading-6']"),
        7: (By.XPATH, "//div[@id='accordion__heading-7']"),
    }

    # Ответы FAQ
    FAQ_ANSWERS = {
        0: (By.XPATH, "//div[@id='accordion__panel-0']"),
        1: (By.XPATH, "//div[@id='accordion__panel-1']"),
        2: (By.XPATH, "//div[@id='accordion__panel-2']"),
        3: (By.XPATH, "//div[@id='accordion__panel-3']"),
        4: (By.XPATH, "//div[@id='accordion__panel-4']"),
        5: (By.XPATH, "//div[@id='accordion__panel-5']"),
        6: (By.XPATH, "//div[@id='accordion__panel-6']"),
        7: (By.XPATH, "//div[@id='accordion__panel-7']"),
    }
    