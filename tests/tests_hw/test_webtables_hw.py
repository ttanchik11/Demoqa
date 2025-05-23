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
    assert webtables.equal_url()

    webtables.btn_add.click()
    time.sleep(1)
    assert webtables.modal.exist()

    # c. Проверка, что нельзя сохранить пустую форму
    webtables.btn_submit.click()
    time.sleep(1)
    # Проверяем, что модальное окно осталось открытым (форма не отправлена)
    assert webtables.modal.exist()

    # Заполнение формы(используем значения из test_data)
    webtables.first_name.send_keys(test_data["first_name"])
    webtables.last_name.send_keys(test_data["last_name"])
    webtables.email.send_keys(test_data["email"])
    webtables.age.send_keys(test_data["age"])
    webtables.salary.send_keys(test_data["salary"])
    webtables.department.input_text(test_data["department"])
    time.sleep(2)

    webtables.btn_submit.click()
    time.sleep(2)

    # Проверяем, что модальное окно закрылось (форма отправлена)
    assert not webtables.modal.exist()
    time.sleep(2)

    # ii. Проверить, что в таблицу добавилась новая запись
    table_text = webtables.table.get_text()

    for key, value in test_data.items():
        assert value in table_text, f"Значение {value} ({key}) не найдено в таблице"


# e. Кликаем на карандаш (редактирование)
    webtables.input_search.send_keys("John")
    time.sleep(2)

    # Проверяем, что запись найдена и кнопка редактирования доступна
    assert webtables.edit_btn.exist()
    webtables.edit_btn.click()
    time.sleep(2)

    # Проверяем, что модальное окно редактирования открылось
    assert webtables.modal.exist()

    webtables.first_name.input_text('Tanya')
    webtables.btn_submit.click()

    table_text = webtables.table.get_text()

    assert "Tanya" in table_text, "Имя 'Tanya' не найдено в таблице"

    webtables.btn_delete.click()
    time.sleep(2)

    # 4. Проверяем что запись удалилась
    table_text = webtables.table.get_text()

    assert not "Tanya" in table_text
    print("записи нет")


    #
    # # Проверяем, что имя обновилось в таблице
    # updated_rows = webtables.rows.get_elements()
    # last_row_updated = updated_rows[-1].text
    # assert new_name in last_row_updated  # Новое имя есть в строке
    # assert test_data["first_name"] not in last_row_updated  # Старого имени нет
    #
    # # g. Удаляем запись (клик на корзину)
    # webtables.btn_delete.click()
    # time.sleep(1)
    #
    # # Проверяем, что запись исчезла
    # rows_after_delete = webtables.rows.get_elements()
    # assert len(rows_after_delete) < len(updated_rows)  # Количество строк уменьшилось
    # assert new_name not in webtables.rows.get_text()  # Удалённой записи нет в таблице