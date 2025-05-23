from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
from pages.alerts import Alerts
from pages.demoqa import DemoQa
import time
import  pytest

@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()

    time.sleep(2)
    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
