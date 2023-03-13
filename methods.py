from base_page import BasePage
from Locators.locators import *
from Content.content import *
import requests


class FormAuthentication(BasePage):

    def should_be_login_field(self):
        assert self.is_element_present(*FormAuthenticationLocators.LOGIN_FIELD), "input login field is not presented"

    def input_login(self, login):
        login_field = self.browser.find_element(*FormAuthenticationLocators.LOGIN_FIELD)
        login_field.send_keys(login)

    def should_be_password_field(self):
        assert self.is_element_present(
            *FormAuthenticationLocators.PASSWORD_FIELD), "input Password field is not presented"

    def should_be_button_to_log_in(self):
        assert self.is_element_present(*FormAuthenticationLocators.LOGIN_BUTTON), "login button is not presented"

    def click_login_button(self):
        login_button = self.browser.find_element(*FormAuthenticationLocators.LOGIN_BUTTON)
        login_button.click()

    def input_password(self, password):
        password_field = self.browser.find_element(*FormAuthenticationLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def should_redirect_securepage(self):
        current_url = self.browser.current_url
        assert FormAuthenticationContent.sucessfull_login_url == current_url, "Uncorrect Url after sucessfull log in"

    def should_be_alert_success(self):
        alert = self.browser.find_element(*FormAuthenticationLocators.ALERT_SUCCESS)
        alert = alert.text[:-2]
        assert FormAuthenticationContent.sucessfull_login_data_alert == alert, f"Uncorrect alert.Expected = '{FormAuthenticationContent.sucessfull_login_data_alert}'.Actual = '{alert}'"

    def should_stay_on_the_login_page(self):
        current_url = self.browser.current_url
        assert FormAuthenticationContent.link == current_url, "Uncorrect Url after sucessfull log in"

    def should_be_alert_invalid_username(self):
        alert = self.browser.find_element(*FormAuthenticationLocators.ALERT_ERROR)
        alert = alert.text[:-2]
        assert FormAuthenticationContent.invalid_username_alert == alert, f"Uncorrect alert.Expected = '{FormAuthenticationContent.invalid_username_alert}'.Actual = '{alert}'"

    def should_be_alert_invalid_password(self):
        alert = self.browser.find_element(*FormAuthenticationLocators.ALERT_ERROR)
        alert = alert.text[:-2]
        assert FormAuthenticationContent.invalid_password_alert == alert, f"Uncorrect alert.Expected = '{FormAuthenticationContent.invalid_username_alert}'.Actual = '{alert}'"


class CheckBoxes(BasePage):

    def should_be_checkbox1_unchecked(self):
        checkbox1 = self.browser.find_element(*CheckBoxesLocators.CHECKBOX1)
        checkbox1_checked = checkbox1.get_attribute("checked")
        assert checkbox1_checked is None, "Checkbox1 is selected!"

    def tick_checkbox1(self):
        checkbox1 = self.browser.find_element(*CheckBoxesLocators.CHECKBOX1)
        checkbox1.click()

    def should_be_checkbox1_checked(self):
        checkbox1 = self.browser.find_element(*CheckBoxesLocators.CHECKBOX1)
        checkbox1_checked = checkbox1.get_attribute("checked")
        assert checkbox1_checked is not None, "Checkbox1 is not selected!"


class StatusCode(BasePage):

    def check_status_200(self, link):
        response = requests.get(link)
        assert response.status_code == 200, f"status code = {response.status_code}"


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
