from pages.profile_page import ProfilePage
from behave import *

profile_page = ProfilePage()


@when('profile: I access my profile')
def step_impl(context):
    profile_page.people_profiles()


@when('profile: I want to check every tab')
def step_impl(context):
    profile_page.check_profile()


@when('profile: I click add tag')
def step_impl(context):
    profile_page.add_tag()


@then('profile: I go back to household page')
def step_impl(context):
    profile_page.household_back()
