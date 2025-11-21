import pytest

from selenium import webdriver
from data import Urls


# Настройка вебдрайвера
@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.main_paige)
    yield driver
    driver.quit()
    
