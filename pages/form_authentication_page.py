from Content.content import FormAuthenticationContent
from Locators.locators import FormAuthenticationLocators
from pages.base_page import BasePage


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
