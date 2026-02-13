import pytest
from src.pages.login_page import LoginPage

def test_successful_login(driver):
    # 1. Инициализируем страницу
    login_page = LoginPage(driver)
    
    # 2. Выполняем экшн (Цепочка вызовов)
    # Мы логинимся под стандартным юзером SauceLabs
    login_page.open_login_screen().login_as("bob@example.com", "10203040")
    
    # 3. ПРОВЕРКА (Assertion)
    # Мы ждем, что после логина нас перебросит на главный экран каталога.
    # В Appium это можно проверить через заголовок или наличие кнопки корзины.
    # Давай найдем ID заголовка "Products" через инспектор или просто 
    # проверим текущую активность.
    
    expected_activity = ".view.activities.MainActivity"
    actual_activity = driver.current_activity
    
    print(f"Текущий экран: {actual_activity}")
    
    assert expected_activity in actual_activity, f"Ожидали экран {expected_activity}, но мы на {actual_activity}"