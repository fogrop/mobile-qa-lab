import pytest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    # Настраиваем опции для Android
    options = UiAutomator2Options()
    options.platform_name = "Android"
    
    # Имя девайса (посмотри в adb devices, обычно emulator-5554)
    options.device_name = "emulator-5554"
    
    # Путь к твоему APK. Мы используем os.path.abspath, чтобы 
    # путь был верным на любом компе.
    options.app = os.path.abspath("apps/mda-2.2.0-25.apk") 
    
    # Модель драйвера
    options.automation_name = "UIAutomator2"
    
    # Соединяемся с сервером Appium (он должен быть запущен!)
    # По умолчанию он слушает порт 4723
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    yield driver # Здесь запускается сам тест
    
    # А здесь мы всё убираем за собой
    driver.quit()