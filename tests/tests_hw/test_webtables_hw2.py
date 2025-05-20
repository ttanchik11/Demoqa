from pages.webtables import Webtables
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_webtables_add(browser):
    test_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "age": "30",
        "salary": "50000",
        "department": "Engineering"
    }
    webtables = Webtables(browser)
    wait = WebDriverWait(browser, 10)

    # 1. Открытие страницы
    webtables.visit()

    # 2. Клик по кнопке Add
    add_button = webtables.btn_add.find_element()
    wait.until(EC.element_to_be_clickable(add_button))
    add_button.click()

    # 3. Ожидание модального окна
    modal = webtables.modal.find_element()
    wait.until(EC.visibility_of(modal))
    assert modal.is_displayed()

    # 4. Проверка пустой формы
    submit_button = webtables.btn_submit.find_element()
    wait.until(EC.element_to_be_clickable(submit_button))
    submit_button.click()

    # Проверка что окно осталось открытым
    try:
        wait.until(EC.invisibility_of_element(modal))
        assert False, "Модальное окно неожиданно закрылось"
    except TimeoutException:
        pass

    # Проверка валидации - нужно проверить все обязательные поля
    required_fields = [
        webtables.first_name,
        webtables.last_name,
        webtables.email,
        webtables.age,
        webtables.salary,
        webtables.department
    ]


    assert webtables.modal.get_dom_attribute('class') == 'was-validated'

    # 5. Заполнение формы
    webtables.first_name.send_keys(test_data["first_name"])
    webtables.last_name.find_element().send_keys(test_data["last_name"])
    webtables.email.find_element().send_keys(test_data["email"])
    webtables.age.find_element().send_keys(test_data["age"])
    webtables.salary.find_element().send_keys(test_data["salary"])
    webtables.department.find_element().send_keys(test_data["department"])

    # 6. Отправка формы
    webtables.btn_submit.click()
    wait.until(EC.invisibility_of_element(modal))
    assert not modal.is_displayed()

    # 7. Проверка данных в таблице
    def get_rows():
        elements = webtables.rows.get_elements()
        return elements if elements else None

    rows = wait.until(lambda d: get_rows())
    last_row = rows[-1].text if rows else ""

    for value in test_data.values():
        assert str(value) in last_row, f"Значение {value} не найдено"

    # 8. Редактирование записи
    edit_button = webtables.edit_btn.find_element()
    wait.until(EC.element_to_be_clickable(edit_button))
    edit_button.click()
    wait.until(EC.visibility_of(modal))

    # Проверка данных формы
    assert first_name_field.get_attribute("value") == test_data["first_name"]
    assert webtables.last_name.find_element().get_attribute("value") == test_data["last_name"]
    assert webtables.email.find_element().get_attribute("value") == test_data["email"]
    assert webtables.age.find_element().get_attribute("value") == test_data["age"]
    assert webtables.salary.find_element().get_attribute("value") == test_data["salary"]
    assert webtables.department.find_element().get_attribute("value") == test_data["department"]

    # 9. Изменение имени
    new_name = "Michael"
    first_name_field.clear()
    first_name_field.send_keys(new_name)
    submit_button.click()
    wait.until(EC.invisibility_of_element(modal))

    # 10. Проверка обновления
    updated_rows = wait.until(lambda d: get_rows())
    last_row_updated = updated_rows[-1].text if updated_rows else ""
    assert new_name in last_row_updated
    assert test_data["first_name"] not in last_row_updated

    # 11. Удаление записи
    delete_button = webtables.btn_delete.find_element()
    wait.until(EC.element_to_be_clickable(delete_button))
    delete_button.click()

    # 12. Проверка удаления
    def is_row_deleted():
        current_rows = get_rows()
        return len(current_rows) < len(updated_rows) if current_rows and updated_rows else False

    wait.until(lambda d: is_row_deleted())
    assert new_name not in webtables.rows.get_text()