from pages.ehr_page import EhrPage
from behave import *

ehr = EhrPage()


@when('ehr: I click add new ehr data')
def step_impl(context):
    ehr.click_add_button()
    ehr.add_ehr()


@then('ehr: I realise I misclicked and I go back to the household page')
def step_impl(context):
    ehr.back_button()
    ehr.back_to_hh()
