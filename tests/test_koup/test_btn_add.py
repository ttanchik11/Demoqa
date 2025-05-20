from pages.koup_page import Koup
from pages.koup_add import KoupAdd
import time


def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add.equal_url()

    assert koup_add.btn_add.get_text() == 'Add Element'

    assert koup_add.btn_add.get_dom_attribute('onclick') == "addElement()"

    """When кликнуть на кнопку 4 раза"""
    for i in range(4):
        koup_add.btn_add.click()

    assert koup_add.btns_delete.check_count_elements(4)

    #проверка всмех элементов
    for element in koup_add.btns_delete.find_elements():
        assert element.text == 'Delete'

    # проверка только первого элемента
    assert koup_add.btns_delete.get_text() == 'Delete'

    """When кликнуть на каждую кнопуку Delete """
    while koup_add.btns_delete.exist():  # Пока список не пуст
        koup_add.btns_delete.click()

        # Проверяем что кнопок не осталось
    assert koup_add.btns_delete.check_count_elements(0)