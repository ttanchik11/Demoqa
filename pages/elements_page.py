from components.components import WebElement
from pages.base_page import BasePage

class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.body_elements = WebElement(driver, "#app > div > div > div > div.col-12.mt-4.col-md-6")
        self.text_elements = WebElement(driver, "div.col-12:nth-child(2)")
        self.icon = WebElement(driver, "header > a > img")
        self.btn_sidebar_first = WebElement(driver, "div:nth-child(1) > span > div")
        self.btn_sidebar_first_texbox = WebElement(driver, "#item-0 > span")
        self.btn_sidebar_first_checkbox = WebElement(driver, "#item-1 > span")
        self.btns_first_menu = WebElement(driver, "div:nth-child(1) > div > ul > li")

