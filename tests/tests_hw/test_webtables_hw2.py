from pages.webtables import Webtables
import time
import pytest


@pytest.mark.flaky(reruns=3)  # Повторить тест до 3 раз при падении
def test_webtables_add(browser):
    test_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "age": "30",
        "salary": "50000",
        "department": "Engineering"
    }

    try:
        # 1. Инициализация и открытие страницы
        webtables = Webtables(browser)
        webtables.visit()
        time.sleep(2)  # Даем время для загрузки страницы

        # 2. Добавление записи
        webtables.btn_add.click()
        time.sleep(1)
        webtables.fill_form(test_data)
        webtables.btn_submit.click()
        time.sleep(3)

        # 3. Поиск добавленной записи
        webtables.search_by_name("John")
        time.sleep(2)

        # 4. Проверка видимости добавленной строки
        assert webtables.row_with_john.is_displayed(), "Добавленная запись не отображается"

        # 5. Проверка содержимого строки
        row_text = webtables.row_with_john.text
        for value in test_data.values():
            assert value in row_text, f"Значение '{value}' не найдено в строке"

    except Exception as e:
        # Делаем скриншот при ошибке
        browser.save_screenshot("error_screenshot.png")
        raise