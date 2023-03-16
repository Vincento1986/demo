from methods import FormAuthentication
from TestData.testdata import FormAuthenticationData
from Content.content import FormAuthenticationContent

link = "http://the-internet.herokuapp.com/login"


def test_sucessfull_authentication(browser):
    page = FormAuthentication(browser, FormAuthenticationContent.link)
    page.open()
    page.should_be_login_field()
    page.should_be_button_to_log_in()
    page.should_be_password_field()
    page.input_login(FormAuthenticationData.valid_login)
    page.input_password(FormAuthenticationData.valid_password)
    page.click_login_button()
    page.should_redirect_securepage()
    page.should_be_alert_success()


def test_unvalid_login_valid_password(browser):
    page = FormAuthentication(browser, FormAuthenticationContent.link)
    page.open()
    page.input_login(FormAuthenticationData.unvalid_login)
    page.input_password(FormAuthenticationData.valid_password)
    page.click_login_button()
    page.should_stay_on_the_login_page()
    page.should_be_alert_invalid_username()


def test_valid_login_unvalid_password(browser):
    page = FormAuthentication(browser, FormAuthenticationContent.link)
    page.open()
    page.input_login(FormAuthenticationData.valid_login)  #
    page.input_password(FormAuthenticationData.unvalid_password)
    page.click_login_button()
    page.should_stay_on_the_login_page()
    page.should_be_alert_invalid_password()


def test_empty_login_valid_password(browser):
    page = FormAuthentication(browser, FormAuthenticationContent.link)
    page.open()
    page.input_login(FormAuthenticationData.empty_login)
    page.input_password(FormAuthenticationData.valid_password)
    page.click_login_button()
    page.should_stay_on_the_login_page()
    page.should_be_alert_invalid_username()


def test_valid_login_empty_password(browser):
    page = FormAuthentication(browser, FormAuthenticationContent.link)
    page.open()
    page.input_login(FormAuthenticationData.valid_login)
    page.input_password(FormAuthenticationData.empty_password)
    page.click_login_button()
    page.should_stay_on_the_login_page()
    page.should_be_alert_invalid_password()
