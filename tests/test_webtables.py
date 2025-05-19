from pages.webtables import Webtables
import time

def test_webtables(browser):
    webtables = Webtables(browser)

    webtables.visit()
    assert not webtables.no_data.exist()

    # Удаляем все строки в таблице
    while webtables.btn_delete.exist():
        webtables.btn_delete.click()

    time.sleep(2)
    assert webtables.no_data.exist()



# Then В таблице отображается блок No rows found