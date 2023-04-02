from pages.login_page import LoginPage
from behave import *

login_page = LoginPage()


# @given('login: I am on the household page')
# def step_impl(context):
#     login_page.logged_in()


@when('login: I login with user "{user}" and pass "{pasw}"')
def step_impl(context, user, pasw):
    login_page.user_input(user)
    login_page.pass_input(pasw)
    login_page.click_login_button()


@then('login: I validate that error message is displayed or not')
def step_impl(context):
    login_page.validate_invalid_credentials_error()


# @when('login: I am on the household page')
# def step_impl(context):
#     login_page.logged_in()


