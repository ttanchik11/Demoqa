from pages.browser_tab import BrowserTab
import time

def test_alerts(browser):
    browser_tab = BrowserTab(browser)
    browser_tab.visit()

    assert len(browser.window_handles) == 1 # обращение к браузеру для посчета вкладок
    browser_tab.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)