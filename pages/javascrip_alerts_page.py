from Content.content import JavaScriptAlertsContent
from Locators.locators import JavaScriptAlertsLocators
from pages.base_page import BasePage


class JavaScriptAlerts(BasePage):

    def click_js_alert_button(self):
        button_js_alert = self.browser.find_element(*JavaScriptAlertsLocators.JS_ALERT)
        button_js_alert.click()

    def close_js_alert(self):
        js_alert = self.browser.switch_to.alert
        js_alert.accept()

    def should_be_js_alert_close(self):
        result = self.browser.find_element(*JavaScriptAlertsLocators.RESULT)
        result = result.text
        assert JavaScriptAlertsContent.result_js_alert_close == result, "Alert is not closed"

    def click_js_alert_confirm_button(self):
        button_js_alert = self.browser.find_element(*JavaScriptAlertsLocators.JS_ALERT_CONFIRM)
        button_js_alert.click()

    def dismiss_js_alert(self):
        js_alert = self.browser.switch_to.alert
        js_alert.dismiss()

    def should_be_js_alert_dismiss(self):
        result = self.browser.find_element(*JavaScriptAlertsLocators.RESULT)
        result = result.text
        assert JavaScriptAlertsContent.result_js_alert_dismiss == result, "cancel not pressed"

    def click_js_alert_promt_button(self):
        button_js_alert = self.browser.find_element(*JavaScriptAlertsLocators.JS_ALERT_PROMT)
        button_js_alert.click()

    def send_message(self, message):
        js_alert = self.browser.switch_to.alert
        js_alert.send_keys(message)
        js_alert.accept()

    def should_be_message_sent(self):
        result = self.browser.find_element(*JavaScriptAlertsLocators.RESULT)
        result = result.text
        assert JavaScriptAlertsContent.result_js_alert_message == result, f"message not sent,Actual:{result}, Expected:{JavaScriptAlertsContent.result_js_alert_message}"
