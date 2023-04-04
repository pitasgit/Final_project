from pages.logout_page import LogoutPage
from behave import *

logout_page = LogoutPage()


@when('logout: I click on the My account button')
def step_impl(context):
    logout_page.account_button()


@when('logout: I click logout')
def step_impl(context):
    logout_page.log_out()


@then('logout: I confirm the home page')
def step_impl(context):
    logout_page.home_page()
