from pages.javascrip_alerts_page import JavaScriptAlerts
from TestData.testdata import JavaScriptAlertsData
from Content.content import JavaScriptAlertsContent


def test_js_alert(browser):
    page = JavaScriptAlerts(browser, JavaScriptAlertsContent.link)
    page.open()
    page.click_js_alert_button()
    page.close_js_alert()
    page.should_be_js_alert_close()


def test_js_confirm_alert(browser):
    page = JavaScriptAlerts(browser, JavaScriptAlertsContent.link)
    page.open()
    page.click_js_alert_confirm_button()
    page.dismiss_js_alert()
    page.should_be_js_alert_dismiss()


def test_js_promt_alert(browser):
    page = JavaScriptAlerts(browser, JavaScriptAlertsContent.link)
    page.open()
    page.click_js_alert_promt_button()
    page.send_message(JavaScriptAlertsData.message)
    page.should_be_message_sent()
