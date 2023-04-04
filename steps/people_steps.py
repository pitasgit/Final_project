from pages.people_page import DeletePersons
from behave import *

people_page = DeletePersons()


@when('people: I click on the add button')
def step_impl(context):
    people_page.click_add_button()


@when('people: I add a new person {first_name} {last_name}')
def step_impl(context, first_name, last_name):
    people_page.add_person()
    people_page.first_name_input(first_name)
    people_page.last_name_input(last_name)
    people_page.save_button()


@then('people: I validate that the person was added')
def step_impl(context):
    people_page.validate_addition()
    people_page.finish()


@when('people: I navigate to the people page')
def step_impl(context):
    people_page.click_people()


@when('people: I want to delete any existing persons')
def step_impl(context):
    people_page.click_select_all()
    people_page.delete_persons()
    people_page.click_delete()


@then('people: I validate that the persons were deleted')
def step_impl(context):
    people_page.delete_confirmation()
