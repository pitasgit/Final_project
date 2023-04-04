Feature: Add health data

  Background:
    Given household: I am on the household page

  @smoke
  Scenario: I press Electronic Health Record data
    When ehr: I click add new ehr data
    Then ehr: I realise I misclicked and I go back to the household page