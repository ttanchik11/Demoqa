from components.components import WebElement
from pages.base_page import BasePage

class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElement(driver, "#userName")
        self.current_address_input = WebElement(driver, "#currentAddress")
        self.btn_submit = WebElement(driver, "#submit")
        self.output_name = WebElement(driver, "#name")
        self.output_address = WebElement(driver, "p#currentAddress")
        self.submit = WebElement(driver, "submit")

