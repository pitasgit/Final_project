from pages.household_page import HouseholdPage
from behave import *

household_page = HouseholdPage()


@given('household: I am on the household page')
def step_impl(context):
    household_page.household_home()
@then('household: I am on the household page')
def step_impl(context):
    household_page.household_home()
    household_page.cookies()


