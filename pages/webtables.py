from pages.base_page import BasePage
from components.components import WebElement


class Webtables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, "div.rt-noData")
        self.btn_add = WebElement(driver, "#addNewRecordButton")
        self.modal = WebElement(driver, ".modal-content")
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, "#department")
        self.btn_submit = WebElement(driver, "#submit")

        self.input_search = WebElement(driver, "#searchBox")

        self.table = WebElement(driver, 'div.rt-tbody')  # локатор табличного поля
        # строки таблицы без пустых
        self.rows = WebElement(driver, "div.rt-tbody > div.rt-tr:not(.-padRow)")

        # Добавляем локатор для ячеек
        self.row_cells = WebElement(driver, "div.rt-td")
        # ячейки конкретной строки
        self.cells_in_row = WebElement(driver, "div.rt-tr-group:not(.-padRow) > div.rt-tr > div.rt-td")

        self.edit_btn = WebElement(driver, "span[title='Edit']")
        self.no_rows_found = WebElement(driver, "div.rt-noData")
        self.btn_delete = WebElement(driver, "span[title='Delete']")

    def fill_form(self, user_data):
        """Заполняет форму данными из словаря"""
        self.first_name.send_keys(user_data["first_name"])
        self.last_name.send_keys(user_data["last_name"])
        self.email.send_keys(user_data["email"])
        self.age.send_keys(user_data["age"])
        self.salary.send_keys(user_data["salary"])
        self.department.send_keys(user_data["department"])

