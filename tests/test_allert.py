from pages.alerts import Alerts
import time

def test_alerts(browser):
    alerts = Alerts(browser)
    alerts.visit()

    assert not alerts.alert()
    alerts.btn_alert.click()
    time.sleep(2)
    assert alerts.alert()