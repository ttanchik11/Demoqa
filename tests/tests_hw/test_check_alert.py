from pages.alerts import Alerts
import time

def test_alerts(browser):
    alerts = Alerts(browser)
    alerts.visit()

    alerts.btn_timerAlertButton.click()
    time.sleep(6)
    assert alerts.alert()