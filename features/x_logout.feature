Feature: Log out of session

  Background:
    Given household: I am on the household page

  @smoke
  Scenario: I want to logout
    When logout: I click on the My account button
    And logout: I click logout
    Then logout: I confirm the home page