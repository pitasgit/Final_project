  Feature: Interact with jules.app

  Background:
    Given household: I am on the household page

  @smoke
  Scenario Outline: I want to add a new person
    When people: I click on the add button
    When people: I add a new person <first_name> <last_name>
    Then people: I validate that the person was added

    Examples:
      | first_name | last_name |
      | Silviu     | Petre     |

  @smoke
  Scenario: I want to delete every person
    When people: I navigate to the People page
    When people: I want to delete any existing persons
    Then people: I validate that the persons were deleted
