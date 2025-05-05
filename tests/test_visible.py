from pages.elements_page import ElementsPage
import time

def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    #клик для раскрытия сайдбара
    # elements_page.btn_sidebar_first.click()
    # time.sleep(3)
    # assert elements_page.btn_sidebar_first_texbox.exist()
    assert elements_page.btn_sidebar_first_texbox.visible()  #проверка что элемент виден
    #assert not elements_page.btn_sidebar_first_texbox.visible() #проверка что элемент не виден

def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_checkbox.visible()

