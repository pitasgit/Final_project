Feature: Check out my profile

  Background:
    Given household: I am on the household page

  @smoke
  Scenario: I check out my profile
    When profile: I access my profile
    And profile: I want to check every tab
    And profile: I click add tag
    Then profile: I go back to household page