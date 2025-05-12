from pages.text_box import TextBox
import time

def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('tester')
    text_box.current_address_input.send_keys('testgorod')
    text_box.btn_submit.click_force()
    time.sleep(2)
    assert text_box.output_name.get_text() == f"Name:{'tester'}"
    assert text_box.output_address.get_text() == f"Current Address:{'testgorod'}"