from pages.alerts import Alerts
import time

def test_alerts(browser):
    alerts = Alerts(browser)
    alerts.visit()

    assert not alerts.alert()
    alerts.btn_alert.click()
    time.sleep(2)
    assert alerts.alert()
    alerts.alert().accept()

def test_alert_text(browser):
    alerts = Alerts(browser)
    alerts.visit()

    alerts.btn_alert.click()
    time.sleep(2)
    assert alerts.alert().text == 'You clicked a button'

    alerts.alert().accept()
    assert not alerts.alert()

def test_confirm(browser):
    alerts = Alerts(browser)
    alerts.visit()

    alerts.btn_confirm.click()
    time.sleep(2)
    alerts.btn_confirm().dismiss()

    assert alerts.confirm_result.get_text() == 'You selected Cancel'

def test_prompt(browser):
    alerts = Alerts(browser)
    name ="NAME"
    alerts.visit()

    alerts.prompt_btn.click()
    time.sleep(2)
    alerts.alert().input_text(name)
    alerts.alert().accept()
    assert alerts.prompt_result.get_text() == f'You entered { name }'