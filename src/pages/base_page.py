from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Устанавливаем стандартное ожидание в 10 секунд
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        # Метод, который ждет, пока элемент ПОЯВИТСЯ и станет ВИДИМЫМ
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        # Метод, который сначала ждет, а потом кликает
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        # Метод для ввода текста
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)