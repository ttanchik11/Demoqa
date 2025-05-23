import pytest
from pages.webtables import Webtables
import time

@pytest.mark.parametrize("column", ["first_name", "last_name",
                                    "age", "email", "salary", "department"])
def test_column_sorting(browser, column):
    page = Webtables(browser)
    page.visit()

    column_header = getattr(page, f"{column}_column_header")
    print(f"Локатор для {column}: {column_header}")  # Проверьте, что это валидный объект Locator
    column_header.click()


    # Кликаем первый раз - сортировка по возрастанию
    column_header.click()
    time.sleep(2)
    assert "-sort-desc" in column_header.get_dom_attribute("class")
    print('успех')
    print(column_header.get_dom_attribute("outerHTML"))  # Проверьте HTML после клика
    time.sleep(2)

    # Кликаем второй раз - сортировка по убыванию
    column_header.click()
    time.sleep(2)
    assert "-sort-asc" in column_header.get_dom_attribute("class")
    print('успех')

