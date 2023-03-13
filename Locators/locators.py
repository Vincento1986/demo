from selenium.webdriver.common.by import By


class FormAuthenticationLocators():
    LOGIN_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    ALERT_SUCCESS = (By.CLASS_NAME, "flash.success")
    ALERT_ERROR = (By.CLASS_NAME, "flash.error")


class CheckBoxesLocators():
    CHECKBOX1 = (By.XPATH, "//*[@id='checkboxes']/input[1]")


class JavaScriptAlertsLocators():
    JS_ALERT = (By.XPATH, "//*[@onclick ='jsAlert()']")
    RESULT = (By.ID, "result")
    JS_ALERT_CONFIRM = (By.XPATH, "//*[@onclick ='jsConfirm()']")
    JS_ALERT_PROMT = (By.XPATH, "//*[@onclick ='jsPrompt()']")
