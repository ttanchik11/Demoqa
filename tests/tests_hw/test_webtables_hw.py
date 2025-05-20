from pages.webtables import Webtables
import time

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


    webtables.visit()

    webtables.btn_add.click()
    time.sleep(1)
    assert webtables.modal.exist()

    # c. Проверка, что нельзя сохранить пустую форму
    webtables.btn_submit.click()
    time.sleep(1)
    # Проверяем, что модальное окно осталось открытым (форма не отправлена)
    assert webtables.modal.exist()
    assert webtables.modal.get_dom_attribute('class') == 'was-validated'

    # Заполнение  формы(используем значения из test_data)
    webtables.first_name.send_keys(test_data["first_name"])
    webtables.last_name.send_keys(test_data["last_name"])
    webtables.email.send_keys(test_data["email"])
    webtables.age.send_keys(test_data["age"])
    webtables.salary.send_keys(test_data["salary"])
    webtables.department.send_keys(test_data["department"])

    webtables.btn_submit.click()
    time.sleep(1)

    # Проверяем, что модальное окно закрылось (форма отправлена)
    assert not webtables.modal.exist()
    time.sleep(2)
    # ii. Проверка данных в таблице
    rows = webtables.rows.get_elements()
    last_row = rows[-1].text if rows else ""

    for value in test_data.values():
        assert str(value) in last_row, f"Значение {value} не найдено в строке таблицы"
    time.sleep(3)
    # e. Кликаем на карандаш (редактирование)
    webtables.edit_btn.click()
    time.sleep(2)
    assert webtables.modal.exist()

    # i. Проверяем, что данные в форме соответствуют записи
    assert webtables.first_name.get_attribute("value") == test_data["first_name"]
    assert webtables.last_name.get_attribute("value") == test_data["last_name"]
    assert webtables.email.get_attribute("value") == test_data["email"]
    assert webtables.age.get_attribute("value") == test_data["age"]
    assert webtables.salary.get_attribute("value") == test_data["salary"]
    assert webtables.department.get_attribute("value") == test_data["department"]

    # f. Меняем имя и сохраняем
    new_name = "Michael"
    webtables.first_name.clear()
    webtables.first_name.send_keys(new_name)
    webtables.btn_submit.click()
    time.sleep(2)

    # Проверяем, что имя обновилось в таблице
    updated_rows = webtables.rows.get_elements()
    last_row_updated = updated_rows[-1].text
    assert new_name in last_row_updated  # Новое имя есть в строке
    assert test_data["first_name"] not in last_row_updated  # Старого имени нет

    # g. Удаляем запись (клик на корзину)
    webtables.btn_delete.click()
    time.sleep(1)

    # Проверяем, что запись исчезла
    rows_after_delete = webtables.rows.get_elements()
    assert len(rows_after_delete) < len(updated_rows)  # Количество строк уменьшилось
    assert new_name not in webtables.rows.get_text()  # Удалённой записи нет в таблице