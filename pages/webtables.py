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

        # Поиск и таблица
        self.input_search = WebElement(driver, "#searchBox")
        self.table = WebElement(driver, 'div.rt-tbody')
        self.rows = WebElement(driver, "div.rt-tr-group:not(.-padRow)")  # Группы строк
        self.cells = WebElement(driver, "div.rt-td")  # Все ячейки

        # Добавляем локатор для ячеек
        self.row_cells = WebElement(driver, "div.rt-td")

        self.edit_btn = WebElement(driver, "span[title='Edit']")
        self.btn_delete = WebElement(driver, "span[title='Delete']")

        self.first_name_column_header = WebElement(driver,"div.rt-th:nth-child(1)")
        self.last_name_column_header = WebElement(driver,"div.rt-th:nth-child(2)")
        self.age_column_header = WebElement(driver,"div.rt-th:nth-child(3)")
        self.email_column_header = WebElement(driver,"div.rt-th:nth-child(4)")
        self.salary_column_header = WebElement(driver,"div.rt-th:nth-child(5)")
        self.department_column_header = WebElement(driver,"div.rt-th:nth-child(6)")

    def fill_form(self, user_data):
        """Заполняет форму данными из словаря"""
        self.first_name.send_keys(user_data["first_name"])
        self.last_name.send_keys(user_data["last_name"])
        self.email.send_keys(user_data["email"])
        self.age.send_keys(user_data["age"])
        self.salary.send_keys(user_data["salary"])
        self.department.send_keys(user_data["department"])

    # def search_by_name(self, name: str):
    #     """Вводит текст в поле поиска"""
    #     self.input_search.clear()
    #     self.input_search.send_keys(name)
    #     time.sleep(1)