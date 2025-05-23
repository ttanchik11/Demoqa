from pages.modal_dialogs import ModalDialogs
import  pytest

def test_modal_dialogs(browser):
    modal_dialogs = ModalDialogs(browser)

    if not modal_dialogs.visit():  # Если visit() возвращает False при неудаче
        pytest.skip("Страница недоступна")

    modal_dialogs.visit()
    modal_dialogs.small_modal_btn.click()
    modal_dialogs.small_modal_btn().dismiss()
    modal_dialogs.large_modal_btn.click()
    modal_dialogs.large_modal_btn().dismiss()