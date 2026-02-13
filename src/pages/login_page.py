from appium.webdriver.common.appiumby import AppiumBy
from src.pages.base_page import BasePage

class LoginPage(BasePage):
    # ЛОКАТОРЫ - Мы выносим их в начало класса, чтобы если они изменятся, 
    # нам не пришлось перерывать весь код.
    # Обрати внимание: мы используем кортежи (By, "value")
    MENU_BURGER = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV")
    MENU_LOGIN_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    USERNAME_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn") 

    # МЕТОДЫ - Это действия, которые может совершить пользователь
    def open_login_screen(self):
        self.click(self.MENU_BURGER)
        self.click(self.MENU_LOGIN_ITEM)
        return self # Мы возвращаем self, чтобы можно было строить цепочки

    def login_as(self, username, password):
        # Вводим данные
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        return self