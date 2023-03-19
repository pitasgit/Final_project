from pages.household_page import HouseholdPage
from behave import *

household_page = HouseholdPage()


@when('household: I click on the add button')
def step_impl(context):
    household_page.click_add_button()


@when('household: I add a new person {first_name} {last_name}')
def step_impl(context, first_name, last_name):
    household_page.add_person()
    household_page.first_name_input(first_name)
    household_page.last_name_input(last_name)
    household_page.save_button()


@then('household: I validate that the person was added')
def step_impl(context):
    household_page.validate_addition()
    household_page.push_notification()
    household_page.finish()
