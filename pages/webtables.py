from pages.base_page import BasePage
from components.components import WebElement

class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.modal = WebElement(driver, "body > div.fade.modal.show > div > div > div.modal-body")
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')

        # Элементы таблицы
        self.table_rows = WebElement(driver, "div.rt-tbody > div.rt-tr-group:not(.-padRow)")  # Исключаем пустые строки

        # Добавляем локатор для ячеек
        self.row_cells = WebElement(driver, "div.rt-td")

        # Добавляем ожидание загрузки таблицы
        self.table_loaded = WebElement(driver, "div.rt-table")

        self.edit_btn = WebElement(driver, 'span[class="mr-2"]')
        self.no_rows_found = WebElement(driver, "div.rt-noData")
        self.btn_delete = WebElement(driver, "span[title='Удалить']")

        self.rows = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight'
        # self.row_data = WebElement(driver, ".rt-tbody > .rt-tr-group:not(.-padRow) > .rt-tr")
        self.cell_in_row = WebElement(driver, ".rt-td")  # Будет использоваться в контексте строки


    def fill_form(self, user_data):
        """Заполняет форму данными из словаря"""
        self.first_name.send_keys(user_data["first_name"])
        self.last_name.send_keys(user_data["last_name"])
        self.email.send_keys(user_data["email"])
        self.age.send_keys(user_data["age"])
        self.salary.send_keys(user_data["salary"])
        self.department.send_keys(user_data["department"])



