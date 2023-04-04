Feature: Login capability
  #smoke test este un sanity check - se ruleaza un login si putem sa incepem suita mai mare de teste

  Background:
    Given home: I am an user on the home page

  @smoke
  Scenario Outline: I login with invalid credentials
    When login: I login with user "<user>" and pass "<pasw>"
    Then login: I validate that error message is displayed or not

    Examples:
      | user                 | pasw                |
      | itfta32ups@gmail.com | Testareautomata123  |
      | itffta32ups@gmail.co | TestareAutomata123! |



  @smoke
  Scenario: I login with valid credentials
    When login: I login with user "tiwkpet@gmail.com" and pass "Testareautomata123!"
    Then household: I am on the household page


