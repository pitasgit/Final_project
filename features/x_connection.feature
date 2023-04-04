Feature: Connection Interaction

  Background:
    Given household: I am on the household page

  @smoke
  Scenario: I want to add a new connection
    When connection: I click on the add button
    And connection: I create a connection
    When connection: I add a new user "user"
    Then connection: I click save and confirm
    And connection: I validate the connection

  @smoke
  Scenario: I select and delete the connection user
    When connection: I click on the Connections button
    And connection: I select the user I want to delete
    And connection: I delete the user
    Then connection: I go back to the household page




