from pages.connection_page import ConnectionPage
from behave import *

connection_page = ConnectionPage()


@when('connection: I click on the add button')
def step_impl(context):
    connection_page.click_add_button()
    connection_page.add_connection()


@when('connection: I create a connection')
def step_imp(context):
    connection_page.create_connection()


@when('connection: I add a new user "user"')
def step_imp(context):
    connection_page.insert_connection_name()


@then('connection: I click save and confirm')
def step_impl(context):
    connection_page.save_button()


@then('connection: I validate the connection')
def step_impl(context):
    connection_page.validate_addition()
    connection_page.finish()
    connection_page.search_button()


@when('connection: I click on the Connections button')
def step_impl(context):
    connection_page.click_connection_button()


@when('connection: I select the user I want to delete')
def step_impl(context):
    connection_page.select_connection()


@when('connection: I delete the user')
def step_impl(context):
    connection_page.delete_user_connection()


@then('connection: I go back to the household page')
def step_impl(context):
    connection_page.search_button()
