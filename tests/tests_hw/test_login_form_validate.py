from pages.form_page import FormPage
import time

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.user_email.get_dom_attribute('pattern') == r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'
    form_page.btn_submit.click_force()

    assert form_page.form_novalidate.get_dom_attribute('class') == 'was-validated'


