from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class WebElement:
    def __init__(self, driver, locator='', locator_type='css'):
        self.locator = locator
        self.driver = driver
        self.locator_type = locator_type

    def get_by_type(self):
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "css":
            return By.CSS_SELECTOR
        elif self.locator_type == "class":
            return By.CLASS_NAME
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + " not correct")
        return False


    def click(self):
        """ Click the element"""
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)
        self.find_element().send_keys(Keys.ENTER)  # выбрать

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + "a") #выделить все
        self.find_element().send_keys(Keys.DELETE) #удалить выделенное

    def input_text(self, text: str) -> None:
        """Вводит текст в поле поиска."""
        self.find_element().clear()  # Очищаем поле (если нужно)
        self.find_element().send_keys(text)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return  value
        return True

    def scroll_to_element(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight;",
            self.find_element()
        )

    def get_output_text(self) -> str:
        return self.find_element().get_text()

    def is_name_displayed_correctly(self, name):
        return f"Name:{name}" in self.output_name.get_text()

    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value