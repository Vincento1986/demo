from TestData.testdata import JavaScriptAlertsData


class FormAuthenticationContent():
    link = "http://the-internet.herokuapp.com/login"
    sucessfull_login_url = "http://the-internet.herokuapp.com/secure"
    sucessfull_login_data_alert = "You logged into a secure area!"
    invalid_username_alert = "Your username is invalid!"
    invalid_password_alert = "Your password is invalid!"


class CheckboxContent():
    link = "http://the-internet.herokuapp.com/checkboxes"


class StatusCodeContent():
    link200 = "http://the-internet.herokuapp.com/status_codes/200"
    link500 = "http://the-internet.herokuapp.com/status_codes/500"


class JavaScriptAlertsContent():
    link = "http://the-internet.herokuapp.com/javascript_alerts"
    result_js_alert_close = "You successfully clicked an alert"
    result_js_alert_dismiss = "You clicked: Cancel"
    result_js_alert_message = f"You entered: {JavaScriptAlertsData.message}"
