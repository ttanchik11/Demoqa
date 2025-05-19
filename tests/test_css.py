from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box = TextBox(browser)

    text_box.visit()
    assert text_box.submit.check_css('color','rgba(255, 255, 255, 1)')

    assert text_box.submit.check_css('borderColor', 'rgba(0, 123, 255, 1)')
    assert text_box.submit.check_css('backgroundColor', 'rgb(0, 123, 255)')