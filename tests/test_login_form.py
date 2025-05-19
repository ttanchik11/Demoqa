from pages.form_page import FormPage
import time

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(3)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies_checkbox_1.click_force()
    form_page.current_address.send_keys('chtotonarodnom')
    time.sleep(3)
    form_page.btn_submit.click_force()
    time.sleep(3)

    assert form_page.modal_dialog.exist()
    form_page.bnt_close_modale.click_force()

def test_state(browser):
    form_page = FormPage(browser)
    form_page.visit()
    time.sleep(3)

    # form_page.state_dropdown.scroll_to_element()
    # time.sleep(3)
    # form_page.btn_NCR.send_keys("NCR")
    # form_page.state_dropdown.send_keys(Keys.ENTER)
    # time.sleep(3)
    # form_page.city_dropdown.click()
    # form_page.btn_Delhi.send_keys("Delhi")
    # form_page.state_dropdown.send_keys(Keys.ENTER)

    form_page.state_dropdown.scroll_to_element()
    form_page.state_dropdown.click_force()
    form_page.btn_NCR.click_force()
    time.sleep(2)

    form_page.city_dropdown.click_force()
    form_page.state_option_ncr.select_city("Delhi")
