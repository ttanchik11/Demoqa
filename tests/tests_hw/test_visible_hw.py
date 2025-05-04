from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert accordion.section1_content.visible()
    accordion.section1_head.click()
    time.sleep(3)
    assert not accordion.section1_content.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert not accordion.section2_content.visible()
    assert not accordion.section3_content.visible()