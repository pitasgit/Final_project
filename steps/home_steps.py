from pages.home_page import HomePage
from behave import *

# folosim sintaxa Gherkin

# given - seteaza situatia initiala
# when - actiunea intermediara
# then - verificarea finala


home_page = HomePage()


@given('home: I am an user on the home page')
def step_impl(context):
    home_page.navigate_to_home_page()
