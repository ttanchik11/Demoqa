from pages.koup_page import Koup
from pages.koup_add import KoupAdd
import time


def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)

    koup_page.visit()
    time.sleep(3)

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add.equal_url()

    assert koup_add.btn_add.get_text() == 'Add Element'

    assert koup_add.btn_add.get_dom_attribute('onclick') == "addElement()"

    """When rликнуть на кнопку 4 раза"""
    for i in range(4):
        koup_add.btn_add.click()

    assert koup_add.btns_delete.check_count_elements(4)

    #проверка всмех элементов
    for element in koup_add.btns_delete.find_element():
        assert element.text == 'Delete'

    # проверка только первого элемента
    assert koup_add.btns_delete.get_text() == 'Delete'

    """When кликнуть на каждую кнопуку Delete """
    # Удаляем все кнопки по одной
    while delete_buttons:  # Пока список не пуст
        delete_buttons[0].click()  # Кликаем первую
        delete_buttons = koup_add.btns_delete.find_elements()  # Обновляем список

    # Проверяем, что кнопок не осталось
    assert len(koup_add.btns_delete.find_elements()) == 0